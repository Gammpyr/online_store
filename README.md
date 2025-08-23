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

Запустите сервер разработки:

```bash
    python manage.py runserver
```
Откройте в браузере:

Главная страница: [ http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Структура проекта
```
config/                     # Главные настройки проекта
├── settings.py
├── urls.py
└── wsgi.py

catalog/                    # Основное приложение
├── migrations/        
├── templates/              
│   └── contacts.html       # Страница с контактами
│   └── home.html           # Главная страница
├── static/           
├── admin.py          
├── apps.py           
├── models.py         
├── tests.py          
├── urls.py           
└── views.py          

manage.py                   
requirements.txt            # Зависимости проекта
poetry.lock                 # Файл конфигурации проекта (poetry)
pyproject.toml              # Файл блокировки зависимостей (poetry)

```
Доступные URL-адреса

[/admin/](http://127.0.0.1:8000/admin/) - Административная панель

[/home/](http://127.0.0.1:8000/) - Домашняя страница

[/contacts/](http://127.0.0.1:8000/contacts/) - Контакты






