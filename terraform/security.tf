resource "azurerm_network_security_group" "retailiq" {
  name                = "${var.project_name}-nsg"
  location            = azurerm_resource_group.retailiq.location
  resource_group_name = azurerm_resource_group.retailiq.name

  tags = {
    Project = "RetailIQ"
  }
}

# SSH
resource "azurerm_network_security_rule" "ssh" {
  name                        = "Allow-SSH"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"

  source_port_range           = "*"
  destination_port_range      = "22"

  source_address_prefix       = "*"
  destination_address_prefix  = "*"

  resource_group_name         = azurerm_resource_group.retailiq.name
  network_security_group_name = azurerm_network_security_group.retailiq.name
}

# HTTP
resource "azurerm_network_security_rule" "http" {
  name                        = "Allow-HTTP"
  priority                    = 110
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"

  source_port_range           = "*"
  destination_port_range      = "80"

  source_address_prefix       = "*"
  destination_address_prefix  = "*"

  resource_group_name         = azurerm_resource_group.retailiq.name
  network_security_group_name = azurerm_network_security_group.retailiq.name
}

# HTTPS
resource "azurerm_network_security_rule" "https" {
  name                        = "Allow-HTTPS"
  priority                    = 120
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"

  source_port_range           = "*"
  destination_port_range      = "443"

  source_address_prefix       = "*"
  destination_address_prefix  = "*"

  resource_group_name         = azurerm_resource_group.retailiq.name
  network_security_group_name = azurerm_network_security_group.retailiq.name
}

resource "azurerm_network_security_rule" "nodeport" {
  name                        = "Allow-NodePort"
  priority                    = 140
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"

  source_port_range           = "*"
  destination_port_range      = "30080"

  source_address_prefix       = "*"
  destination_address_prefix  = "*"

  resource_group_name         = azurerm_resource_group.retailiq.name
  network_security_group_name = azurerm_network_security_group.retailiq.name
}

# Jenkins
resource "azurerm_network_security_rule" "jenkins" {
  name                        = "Allow-Jenkins"
  priority                    = 130
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"

  source_port_range           = "*"
  destination_port_range      = "8080"

  source_address_prefix       = "*"
  destination_address_prefix  = "*"

  resource_group_name         = azurerm_resource_group.retailiq.name
  network_security_group_name = azurerm_network_security_group.retailiq.name
}

resource "azurerm_network_interface_security_group_association" "retailiq" {
  network_interface_id      = azurerm_network_interface.retailiq.id
  network_security_group_id = azurerm_network_security_group.retailiq.id
}