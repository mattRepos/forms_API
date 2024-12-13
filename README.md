

 Для инициализации БД надо использовать команду: 

    python manage.py initialize_forms
    
## При использовании данной команды происходит очищение и добавление базовых шаблонов форм в БД.
    Форма Contact Form имеет следующие поля: 
        email": "email", 
        "phone_number": "phone"
    Форма Order Form имеет следующие поля: 
        "order_date": "date", 
        "user_email": "email"

# Для выполнения тестов необходимо использовать команду:

    python manage.py test

## Тесты выполены с помощью встроенных в Django функций тестирования.

    test_post_without_formkey:

Проверяет, что если в запросе отсутствует обязательное поле "form", сервер вернет ошибку с кодом 400 и соответствующим сообщением: {"form":["This field is required."]}.

    test_post_form:

Проверяет, что если форма отправлена корректно с обязательными полями, сервер вернет успешный ответ с кодом 200 и ожидаемую структуру с типами полей.

    test_post_form_not_identificate_form:

Проверяет, что если форма отправлена с корректными полями, сервер все равно возвращает правильную структуру данных с типами полей и статусом 200.

    test_post_form_with_1_field:

Проверяет, что если форма отправлена с одним полем, сервер правильно идентифицирует тип этого поля (например, дата) и возвращает успешный ответ с кодом 200.

    test_post_form_with_text:

Проверяет, что если форма отправлена с текстовым значением в одном поле, сервер правильно идентифицирует тип поля как текст и возвращает успешный ответ.
