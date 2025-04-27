# Variables por defecto
FILE ?= palabras.txt
SORT ?= yes
ORDER ?= asc

# Definición de objetivos phony
.PHONY: run task3

# Regla principal
run:
	docker run --rm --volume "$$(pwd):/opt/app" --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py $(FILE) $(SORT) $(ORDER)

# Ejecutar el programa con palabras.txt y sin ordenar
task3:
	docker run --rm --volume "$$(pwd):/opt/app" --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py palabras.txt no desc