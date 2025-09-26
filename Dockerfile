FROM python:3.12.3-slim

WORKDIR /app

# Копируем зависимости
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only=main

# Копируем весь код (включая manage.py)
COPY . .

EXPOSE 8000

CMD ["python", "dj_drf_hotel_proj/manage.py", "runserver", "0.0.0.0:8000"]