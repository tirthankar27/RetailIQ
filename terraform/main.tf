provider "docker" {}

resource "docker_network" "retailiq_network" {
  name = "${var.project_name}-network"
}

resource "docker_volume" "postgres_data" {
  name = "${var.project_name}-postgres-data"
}

resource "docker_volume" "redis_data" {
  name = "${var.project_name}-redis-data"
}

resource "docker_volume" "grafana_data" {
  name = "${var.project_name}-grafana-data"
}

resource "docker_volume" "jenkins_data" {
  name = "${var.project_name}-jenkins-data"
}