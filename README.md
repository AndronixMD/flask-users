# Установка и запуск
При первом запуске будет создан админ с email admin@admin.com и паролем admin123.
- Установить Python3
- (Опционально) создать виртуальную среду
    ```
    python3 -m venv venv
    ```
    Активировать venv
    ```
    . venv/bin/activate
    ```
- Установить необходимые пакеты
    ```
    pip3 install -r requirements.txt
    ```
- Сделать миграцию
    ```
    python3 manage.py db init
    python3 manage.py db migrate
    python3 manage.py db upgrade
    ```
- Запустить приложение
    ```
    python3 app.py
    ```

