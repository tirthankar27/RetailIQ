resource "azurerm_resource_group" "retailiq" {
  name     = "${var.project_name}-rg"
  location = var.location

  tags = {
    Project     = "RetailIQ"
    Environment = "Development"
    ManagedBy   = "Terraform"
  }
}