Система управления сотрудниками компании

# Django Company Project

Проект для управления сотрудниками и рабочими местами компании с использованием Django.

---

## Структура проекта

django_company/
│
├── company_management/ # Настройки Django
├── employees/ # Приложение сотрудников
├── workplaces/ # Приложение рабочих мест
├── templates/ # Шаблоны HTML
├── static/ # Статические файлы
├── manage.py # Главный скрипт Django
└── README.md # Этот файл

yaml
Копировать
Редактировать

---

## Установка

1. Клонируйте репозиторий:

```bash
git clone <URL_репозитория>
cd django_company
Создайте виртуальное окружение и активируйте его:

bash
Копировать
Редактировать
python -m venv venv
source venv/Scripts/activate   # Windows
# или
source venv/bin/activate       # Linux/Mac
Установите зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Миграции и база данных
Создайте миграции для приложений:

bash
Копировать
Редактировать
python manage.py makemigrations employees
python manage.py makemigrations workplaces
Примените миграции:

bash
Копировать
Редактировать
python manage.py migrate
Создайте суперпользователя для доступа в админку:

bash
Копировать
Редактировать
python manage.py createsuperuser
Запуск сервера
bash
Копировать
Редактировать
python manage.py runserver
Сервер будет доступен по адресу: http://127.0.0.1:8000/

Админка
Для управления сотрудниками и рабочими местами перейдите в http://127.0.0.1:8000/admin и войдите под суперпользователем.

Полезные команды
Запустить оболочку Django:

bash
Копировать
Редактировать
python manage.py shell
Очистить базу данных (удалить db.sqlite3) и пересоздать миграции:

bash
Копировать
Редактировать
rm db.sqlite3
rm employees/migrations/0*.py
rm workplaces/migrations/0*.py
python manage.py makemigrations
python manage.py migrate
Создать тестовые данные (по желанию можно добавить фикстуры)

Контакты
Проект ведёт: Анна Платошина
Email: example@example.com

# Employees App

В приложении `employees` реализованы следующие модели:

- **CustomUser** — пользователь
- **Employee** — сотрудник
- **Skill** — навык
- **EmployeeSkill** — связь сотрудника и навыка
- **Workplace** — место работы
- **EmployeeImage** — изображения сотрудников
