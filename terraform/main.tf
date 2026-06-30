provider "docker" {}

resource "docker_network" "retailiq_network" {
  name = "retailiq-network"
}

resource "docker_volume" "postgres_data" {
  name = "retailiq-postgres-data"
}

resource "docker_volume" "redis_data" {
  name = "retailiq-redis-data"
}

resource "docker_volume" "grafana_data" {
  name = "retailiq-grafana-data"
}

resource "docker_volume" "backend_uploads" {
  name = "retailiq-backend-upload-data"
}

output "backend_uploads_volume" {
  value = docker_volume.backend_uploads.name
}