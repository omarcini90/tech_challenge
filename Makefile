.PHONY: help install test run down clean

help:
	@echo "Comandos disponibles:"
	@echo "  make install   Instala los requisitos"
	@echo "  make test      Ejecuta los tests"
	@echo "  make run       Levanta el servicio y dependencias en Docker"
	@echo "  make down      Detiene los servicios en Docker"
	@echo "  make clean     Elimina todos los contenedores y volúmenes"

install:
	docker-compose build

test:
	docker-compose run --rm api pytest

run:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down -v --remove-orphans
	docker system prune -f
	docker volume prune -f