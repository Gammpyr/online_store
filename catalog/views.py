from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_category_products
from config.settings import CACHE_ENABLED


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        return get_category_products(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('name')
        category_id = self.kwargs.get('category_id')
        # category_id = self.request.GET.get('category_id')
        context['current_category'] = Category.objects.filter(id=category_id).first()
        return context

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        user = self.request.user
        context['is_moderator'] = user.is_superuser or user.groups.filter(name='Модератор продуктов').exists()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    # permission_required = 'catalog.change_product'
    #
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset=queryset)
    #     if obj.owner != self.request.user:
    #         raise PermissionDenied("У вас нет прав на редактирование этого продукта")
    #     return obj

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser or obj.owner != self.request.user or not self.request.user.groups.filter(name='Модератор продуктов').exists():
            raise PermissionDenied("У вас нет прав на удаление этого продукта")
        return obj


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return render(request, 'catalog/answer.html', {'name': name, 'phone': phone})


class IndexView(TemplateView):
    template_name = "catalog/index.html"


class ProductTogglePublishView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.owner != request.user and not (
                self.request.user.is_superuser or
                self.request.user.groups.filter(name='Модератор продуктов').exists()
        ):
            raise PermissionDenied("У вас нет прав на изменение статуса публикации")

        is_published = request.POST.get('is_published') == 'true'
        product.is_published = is_published
        product.save()
        return redirect('catalog:product_detail', pk=pk)
