## Домашнее задание 6

**questions.conf**:

```nginx
server {
    listen       80;
    server_name  questions.com www.domain2.com;
    access_log   /var/log/nginx/questions.access.log;
    error_log    /var/log/nginx/questions.error.log;

    location ~ ^/(media|static) {
        expires max;
        root '/home/ldk/VK-Technopark-WEB/Project';
    }
    
    # pass requests for dynamic content to rails/turbogears/zope, et al
    location / {
        proxy_pass      http://127.0.0.1:8080;
    
        proxy_cache question_zone;
        proxy_cache_valid 200 5m;
        proxy_ignore_headers Set-Cookie;
        proxy_hide_header Set-Cookie;


        proxy_set_header  Host                $host;
        proxy_set_header  X-Real_IP           $remote_addr;
        proxy_set_header  X-Forwarded-Proto   $scheme;
        proxy_set_header  X-Forwarded-For     $proxy_add_x_forwarded_for;
    }

}
```



### django commands

```bash
python3 -m venv venv               - установка окружения

pip list                           - отображение списка пакетов

source venv/bin/activate           - активация окружения

django-admin startproject askme .  - создание проекта askme

python manage.py startapp app

python manage.py runserver         - запуск сервера на локальном хосте
```

### models.py:

```bash
python manage.py makemigrations

python manage.py migrate
```

### gunicorn
```bash
gunicorn askme.wsgi

```

### nginx
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04-ru


### Apache test
```bash
ab -n 100 -c 2  "http://127.0.0.1/"


```



### Проблемы:



- [x] нет лайков и рейтинга в листингах 
- [x] нет ответов на странице одного вопроса
- [x] сверстать ошибку в форме 

- [ ] Контролер и роут до hot

- [ ] вставка данных
- [x] unique_together в лайках
- [x] прикрутить к контроллерам
