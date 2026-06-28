FROM python:3.12-slim

WORKDIR /app

# Install PostgreSQL client (provides pg_isready)
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY start.sh .

RUN chmod +x start.sh

EXPOSE 8000

CMD ["./start.sh"]