# Сайт с достопримечательностями Москвы

Интерактивная карта Москвы, на которой можно добавить виды активного отдыха с подробными описаниями и комментариями, на что обратить внимание на прогулке по Москве.

 - [Основной сайт](https://dumbturtle.pythonanywhere.com/)
 - [Панель администрирования сайта](https://dumbturtle.pythonanywhere.com/admin)

## Установка и настройка

### Установка 

Скачать скрипт с [github](https://github.com/dumbturtle/). Установить необходимые пакеты: 
     
```
$ pip install -r requirements.txt
```

Создайте внутри папки ```where_to_go``` папки ```/static/``` и ```/media/```.

Запустите применение миграций:

```
$ python manage.py migrate
```

Создайте пользователя с правами администрирования сайта:

```
$ python manage.py createsuperuser
```

Запустите:
```
$ python manage.py runserver
```

После запуска сайт будет доступен локально по адресу: [```http://127.0.0.1:8000```](http://127.0.0.1:8000). Панель администрирования сайта:[```http://127.0.0.1:8000/admin```](http://127.0.0.1:8000/admin)

### Настройка

Для настройки сайта используются переменные окружения. Шаблон файла настройки: ```.env-tmp```.

Доступны следующие настройки:
```
SECRET_KEY='change-me'
DEBUG=True
ALLOWED_HOSTS= 127.0.0.1, *.com
CSRF_COOKIE_SECURE=True
```
Подробное описание: 
 - ```SECRET_KEY``` - секретный ключ. Используется для криптографической подписи, должен быть случайным и сложным для подбора. Набор любых символов длинной не менее 50 символов.
 - ```DEBUG``` - включение отладочного режима.
 - ```ALLOWED_HOSTS``` - список хостов/доменов, для которых может работать текущий сайт. 
 - ```CSRF_COOKIE_SECURE``` - указывает, использовать ли безопасные куки для CSRF. 


 ### Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).