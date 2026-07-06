#!/bin/sh

echo "Waiting for PostgreSQL..."

until pg_isready \
    -h "$POSTGRES_HOST" \
    -p "$POSTGRES_PORT" \
    -U postgres
do
    echo "PostgreSQL is unavailable..."
    sleep 2
done

echo "PostgreSQL is ready."

echo "Running Alembic migrations..."

alembic upgrade head

if [ $? -ne 0 ]; then
    echo "Alembic migration failed."
    exit 1
fi

echo "Starting FastAPI..."

exec uvicorn app.main:app \
    --host "$BACKEND_HOST" \
    --port "$BACKEND_PORT"