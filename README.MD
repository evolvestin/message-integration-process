# Инструкция по работе с проектом

## Шаг 1: Создание базы данных

Необходимо создать базу данных в PostgreSQL. Выполните следующую команду:

```sql
CREATE DATABASE db_name;
```

## Шаг 2: Настройка `settings.py`

Откройте файл `settings.py` вашего проекта Django и измените секцию `DATABASES` на следующее:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',         # Имя вашей базы данных
        'USER': 'postgres',        # Ваше имя пользователя PostgreSQL
        'PASSWORD': 'postgres',    # Пароль пользователя
        'HOST': 'localhost',       # Адрес сервера (обычно localhost)
        'PORT': '5432',            # Порт PostgreSQL
    }
}
```

Убедитесь, что вы изменили эти поля на настройки вашей системы.

## Шаг 3: Создание виртуального окружения

1. Создайте виртуальное окружение:

   ```bash
   python -m venv venv
   ```

2. Активируйте виртуальное окружение:

   - Для Windows:

     ```bash
     venv\Scripts\activate
     ```

3. Установите зависимости из `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Шаг 4: Запуск сервера

Откройте терминал и перейдите в папку проекта по следующему пути
Теперь вы можете запустить сервер командой:

```bash
python manage.py runserver
```

## Шаг 5: Доступ к приложению

После того как сервер запущен без ошибок, откройте веб-браузер и перейдите по адресу:

```
http://127.0.0.1:8000/app/mail
```
