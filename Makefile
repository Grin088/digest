POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=main

.PHONY: up_api up_db make_migration apply_migration load_stubs deploy_all build_api run_tests restart_api


build_api:
	docker-compose up --build -d main_app

run_worker:
	docker-compose up --build -d celery_worker

apply_migration:
	docker-compose exec main_app alembic upgrade head

load_stubs:
	docker-compose exec -T postgres_db psql -p 5432 -U $(POSTGRES_USER) -d $(POSTGRES_DB) < .docker/db/init.sql

up_api:
	docker-compose up -d main_app

restart_api:
	docker-compose restart main_app

up_db:
	docker-compose up -d postgres_db




deploy_all: build_api run_worker apply_migration load_stubs