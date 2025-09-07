from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['title', 'is_published', 'image', 'content']

    # success_url = reverse_lazy("blogs:blogs_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", kwargs={'pk': self.object.pk})


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['title', 'is_published', 'image', 'content']

    # success_url = reverse_lazy("blogs:blogs_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", kwargs={'pk': self.object.pk})


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        show_all = self.request.GET.get('show_all')
        if show_all == 'true':
            return Blog.objects.all()
        return Blog.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_all'] = self.request.GET.get('show_all') == 'true'
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy("blogs:blogs_list")
