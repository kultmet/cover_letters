# cover_letters
Telegram-bot cover_letters
собрать образ

docker build -t cover_letters .

запустить контейнер
docker 
```
run --name cover_letters -d -p 80:80 cover_letters
```

rabbitMQ
```
docker run --rm -p 15672:15672 rabbitmq:3.10.7-management
После этого можно открыть веб-интерфейс RabbitMQ в браузере по ссылке http://127.0.0.1:15672/
