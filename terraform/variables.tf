variable "project_name" {
  description = "Project Name"
  type        = string
  default     = "retailiq"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "Central India"
}

variable "vm_size" {
  description = "Azure VM Size"
  type        = string
  default     = "Standard_B2s"
}

variable "os_disk_type" {
  description = "OS Disk Type"
  type        = string
  default     = "Standard_LRS"
}

variable "admin_username" {
  description = "Linux VM Username"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key_path" {
  description = "Path to SSH Public Key"
  type        = string
}