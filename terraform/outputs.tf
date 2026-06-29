output "network_name" {
  value = docker_network.retailiq_network.name
}

output "postgres_volume" {
  value = docker_volume.postgres_data.name
}

output "redis_volume" {
  value = docker_volume.redis_data.name
}

output "grafana_volume" {
  value = docker_volume.grafana_data.name
}

output "jenkins_volume" {
  value = docker_volume.jenkins_data.name
}