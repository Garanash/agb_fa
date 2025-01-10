# agb server for database and api

для запуска приложения на сервере введите команды:
```bash

docker build -t myimage .  
docker run -d --name mycontainer -p 80:80 myimage
```