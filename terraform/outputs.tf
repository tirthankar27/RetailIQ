output "resource_group_name" {
  description = "Azure Resource Group"

  value = azurerm_resource_group.retailiq.name
}

output "virtual_network_name" {
  description = "Virtual Network"

  value = azurerm_virtual_network.retailiq.name
}

output "subnet_name" {
  description = "Subnet"

  value = azurerm_subnet.retailiq.name
}

output "public_ip_address" {
  description = "VM Public IP"

  value = azurerm_public_ip.retailiq.ip_address
}

output "virtual_machine_name" {
  description = "Virtual Machine Name"

  value = azurerm_linux_virtual_machine.retailiq.name
}

output "ssh_connection" {
  description = "SSH Command"

  value = "ssh ${var.admin_username}@${azurerm_public_ip.retailiq.ip_address}"
}