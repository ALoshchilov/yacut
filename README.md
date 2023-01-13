# YaCut. Проект сервиса для создания коротких ссылок
На большинстве сайтов адреса страниц довольно длинные, например, как у той страницы, на которой вы сейчас находитесь. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно. 
Удобнее использовать короткие ссылки.

Сервис позволяет самостоятельно задать код-сокращение для ссылки. Если код-сокращение не предоставлен, сервис сгенерирует ссылку самостоятельно.

## Информация об авторе
[Александр Лощилов](mailto:loshchilov.aleksandr@gmail.com?subject=[GitHub]Yacut)
Факультет Python Backend. Когорта 10+.

## Примененный стек технологий
* Python
* Flask
* SQLAlchemy
* HTML
* CSS
* Jinja2


## Развертывание проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ALoshchilov/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

При первом запуске проекта создать базу данных:

```
flask shell
from yacut import db
db.create_all()
exit()
```


В случае первичной миграции создать репозиторий для хранения миграций:

```
flask db init
```

Провести миграции:

```
flask db migrate
```

Запустить веб-приложение Flask:

```
flask run
```

## Документация API

Полная документация локально развернутого проекта доступна по [ссылке](http://127.0.0.1:5000/api/docs)

Примеры вызовов API

* Получение оригинальной ссылки по коду-сокращению.
```
GET http://127.0.0.1:5000/api/id/<short_id>
```

Тело запроса:
```
{
    "short_id": "myshort"
} 
```

Тело ответа:
```
{
    "url": "https://somesite.com/"
}
```

* Создание сокращения ссылки с заданным кодом-сокращением (custom_id)
```
POST http://127.0.0.1:5000/api/id/
```
Тело запроса:
```
{
    "url": "https://somesite.com/",
    "custom_id": "myshort"
} 
```
Тело ответа:
```
{
    "short_link": "http://127.0.0.1:5000/myshort",
    "url": "https://somesite.com/"
}
```

* Создание сокращения ссылки без заданного кода-сокращения(custom_id)
```
POST http://127.0.0.1:5000/api/id/
```
Тело запроса:
```
{
    "url": "https://somesite.com/"
} 
```
Тело ответа:
```
{
    "short_link": "http://127.0.0.1:5000/VKxoiL",
    "url": "https://somesite.com/"
}
```

## Описание переменных окружения

FLASK_APP - имя приложения Flask

```
FLASK_APP=yacut
```

FLASK_ENV - режим работы приложения Flask

```
FLASK_ENV=development
```

DATABASE_URI - URI подключения к БД

```
DATABASE_URI=sqlite:///db.sqlite3
```

SECRET_KEY - "соль", используемая для создания шифрованных cookie

```
SECRET_KEY='Qwerty123!@#'
```