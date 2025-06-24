FROM python:3.11-slim as base

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app


# === Dev/Test Stage ===
FROM base AS test

COPY requirements/requirements-test.txt .
RUN pip install --no-cache-dir -r requirements-test.txt

COPY tests ./tests
CMD ["pytest", "tests/"]


# === Production Stage ===
FROM base AS prod

CMD ["uvicorn", "app.handler:app", "--host", "0.0.0.0", "--port", "8000"]