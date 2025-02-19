# Stage 1: Build Stage
FROM python:3.10-alpine AS builder

WORKDIR /app

RUN apk update && apk add --no-cache postgresql-dev build-base

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY src src

RUN rm -rf /app/*.sha256 /app/resolve /app/transferring /app/writing

# Stage 2: Final Image
FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache libpq

COPY --from=builder /app /app

EXPOSE 5000
ENV FLASK_APP=/src/app:create_app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
