#  Local Hatch Commands
.PHONY: dev test lint shell format

dev:
	hatch run dev

lint:
	hatch run lint

format:
	hatch run format

shell:
	hatch shell

# Docker Commands
.PHONY: build up down logs test

build:
	docker-compose build

test:
	docker-compose run --rm test

up:
	docker-compose up

down:
	docker-compose down

logs:
	docker-compose logs -f
