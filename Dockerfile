FROM python:3.12.3-slim

WORKDIR /app


COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only=main --no-root


COPY . .

EXPOSE 8000

CMD ["python", "dj_drf_hotel_proj/manage.py", "runserver", "0.0.0.0:8000"]