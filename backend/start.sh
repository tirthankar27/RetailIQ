#!/bin/sh

echo "Waiting for PostgreSQL..."

until pg_isready -h postgres -p 5432 -U postgres
do
    echo "PostgreSQL is unavailable - sleeping..."
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

exec uvicorn app.main:app --host 0.0.0.0 --port 8000