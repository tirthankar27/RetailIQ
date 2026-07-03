resource "azurerm_virtual_network" "retailiq" {
  name                = "${var.project_name}-vnet"
  location            = azurerm_resource_group.retailiq.location
  resource_group_name = azurerm_resource_group.retailiq.name

  address_space = [
    "10.0.0.0/16"
  ]

  tags = {
    Project = "RetailIQ"
  }
}

resource "azurerm_subnet" "retailiq" {
  name                 = "${var.project_name}-subnet"
  resource_group_name  = azurerm_resource_group.retailiq.name
  virtual_network_name = azurerm_virtual_network.retailiq.name

  address_prefixes = [
    "10.0.1.0/24"
  ]
}

resource "azurerm_public_ip" "retailiq" {
  name                = "${var.project_name}-public-ip"
  location            = azurerm_resource_group.retailiq.location
  resource_group_name = azurerm_resource_group.retailiq.name

  allocation_method = "Static"

  sku = "Standard"

  tags = {
    Project = "RetailIQ"
  }
}

resource "azurerm_network_interface" "retailiq" {
  name                = "${var.project_name}-nic"
  location            = azurerm_resource_group.retailiq.location
  resource_group_name = azurerm_resource_group.retailiq.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.retailiq.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.retailiq.id
  }

  tags = {
    Project = "RetailIQ"
  }
}