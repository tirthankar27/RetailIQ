resource "azurerm_linux_virtual_machine" "retailiq" {
  name                = "${var.project_name}-vm"
  resource_group_name = azurerm_resource_group.retailiq.name
  location            = azurerm_resource_group.retailiq.location
  size                = var.vm_size

  admin_username = var.admin_username

  network_interface_ids = [
    azurerm_network_interface.retailiq.id
  ]

  disable_password_authentication = true

  admin_ssh_key {
    username   = var.admin_username
    public_key = file(var.ssh_public_key_path)
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = var.os_disk_type
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "ubuntu-24_04-lts"
    sku       = "server"
    version   = "latest"
  }

  computer_name = "${var.project_name}-vm"

  tags = {
    Project     = "RetailIQ"
    Environment = "Development"
    ManagedBy   = "Terraform"
  }
}