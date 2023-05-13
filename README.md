# cover_letters
cover_letters

Запустить локально
```
uvicorn main:app --reload
```

собрать образ

docker build -t cover_letters .

запустить контейнер
```
docker run --name cover_letters --rm -d -p 80:80 kultmet/cover_letters:1.1
```

rabbitMQ
```
docker run --rm -p 15672:15672 rabbitmq:3.10.7-management

это лучше!!
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

После этого можно открыть веб-интерфейс RabbitMQ в браузере по ссылке http://127.0.0.1:15672/


Сделано

    эндпоинты:
        для получения и добавления скиллов в стек пользователя
        для получения всех доступных (общих) скиллов
        поменял алгоритм распознавания требований

Задачи 
    настроить автодеплой
