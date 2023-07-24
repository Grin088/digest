# About app
Приложения для формирования дайджеста контента для пользователя на основании его подписок.
Приложение выполнено c использованием framework FastAPI c использованием базы данных PostgreSQL, воркерa Celery и брокера сообщений RabbitMQ.
После добавления пользователю подписки на какой-либо контент, в Celery отправляется задача по созданию дайджеста для этого пользователя.
# How to run app
- Для запуска приложения в docker создайте .env файл в основной директории по образу "docker_example.env"
- Для запуска приложения в shell создайте .env файл по образцу "shell_example.env"

# How to get user digest
По умолчанию у пользователя уже созданы подписки, что бы запустить процесс по созданию дайджеста, необходимо создать дополнительную подписку.
После успешного запуска приложения перейдите в браузер по адресу:
- http://localhost:8000/docs если приложение запущено в shell;
- http://localhost:8001/docs если приложение запущено в docker;
- Используйте endpoint subscriptions/ POST method для создания подписки пользователя;
- доступные по умолчанию user_id values [1, 2, 3];
- доступные по умолчанию category_id values [1, 2, 3, 4, 5, 6, 7, 8, 9];
- для получения дайджеста контента используйте endpoint digest/ GET method;
- введите user_id, результат будет доступен только для пользователя, для которого был отправлен запрос на подписку;

### Required Software
 - Docker
 - docker-compose
 - python
 - Unix-like OS

### How to deploy application
start command to fully deploys a local application
```shell
make deploy_all
```

# Start app without dokcer-compose:
## all command must start from main directory
install requirements
```shell
pip install -r requirements.txt
```
start rabbit_mq
```shell
docker run -d --hostname rabbit --name rabbit -e RABBITMQ_DEFAULT_VHOST=vhost -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest -p 15673:15672 -p 5672:5672  rabbitmq:3-management

```
start db in docker container
```shell
docker run --name db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=main -p 5432:5432 -d postgres
```
add env data to console
```shell
set -o allexport
source .env
set +o allexport
```
apply migrations
```shell
alembic upgrade head
```
add data to psql db
```shell
docker cp .docker/db/init.sql db:/init.sql
docker exec  db psql -U user -d main -f /init.sql
```

start app
```shell
uvicorn api.main:app
```

start celery worker
```shell
set -o allexport
source .env
set +o allexport
celery --app api.celery_tasks.tasks:app worker --loglevel=info
```