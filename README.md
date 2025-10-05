# Django Project: Online Store

"Веб-приложение для онлайн магазина на Django."


## Установка и настройка

### Установка

Клонируйте репозиторий:
```bash
    git clone https://github.com/Gammpyr/online_store
```
Создайте виртуальное окружение и активируйте его:

```bash
    poetry init
```
Установите зависимости:
```bash
    poetry install
```

Импортируйте тестовые данные:
```
    python manage.py loaddata fixtures/data_name.json
```


Запустите сервер разработки:

```bash
    python manage.py runserver
```
Откройте в браузере:

Главная страница: [ http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Доступные URL-адреса

[/admin/](http://127.0.0.1:8000/admin/) - Административная панель

[/home/](http://127.0.0.1:8000/) - Домашняя страница

[/contacts/](http://127.0.0.1:8000/contacts/) - Контакты

[/products/list/](http://127.0.0.1:8000/products/list/) - Список продуктов

[/blogs/list/](http://127.0.0.1:8000/blogs/list/) - Страница блога

Структура проекта
```
Online_store/
├── blogs/                      # Приложение блогов
│   ├── migrations/             # Миграции модели
│   ├── templates/              # Шаблоны приложения
│   │   └── blogs/              # Шаблоны блогов
│   ├── __init__.py
│   ├── admin.py                # Регистрация моделей в админке
│   ├── apps.py                 # Конфигурация приложения
│   ├── models.py               # Модели блогов
│   ├── tests.py                # Тесты
│   ├── urls.py                 # URL-маршруты
│   └── views.py                # Представления
│
├── catalog/                    # Приложение товаров
│   ├── management/             # Управление командами
│   │   └── commands/           # Пользовательские команды
│   ├── migrations/             # Миграции модели
│   ├── templates/              # Шаблоны приложения
│   │   └── catalog/            # Шаблоны каталога
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                # Формы для создания/редактирования
│   ├── models.py               # Модели товаров
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/                     # Основная конфигурация проекта
│   ├── __init__.py
│   ├── asgi.py                 # ASGI-конфигурация
│   ├── settings.py             # Настройки Django
│   ├── urls.py                 # Общие маршруты
│   └── wsgi.py                 # WSGI-конфигурация
│
├── fixtures/                   # Тестовые данные
│   ├── blogs_data.json         # Данные блогов
│   └── catalog_data.json       # Данные каталога
│
├── media/                      # Загрузка медиа (изображения)
│
├── static/                     # Статические файлы (CSS, JS)
│
├── users/                      # Приложение пользователей
│   ├── migrations/             # Миграции модели
│   ├── templates/              # Шаблоны приложения
│   │   └── users/              # Шаблоны пользователей
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                # Формы регистрации и входа
│   ├── models.py               # Кастомная модель пользователя
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .env                        # Переменные окружения
├── .env.sample                 # Пример .env
├── .gitignore                  # Игнорируемые файлы Git
├── manage.py                   # Утилита Django
├── poetry.lock                 # Фиксированные версии зависимостей
├── pyproject.toml              # Конфигурация Poetry
├── README.md                   # Документация проекта
└── requirements.txt            # Требуемые пакеты

```







