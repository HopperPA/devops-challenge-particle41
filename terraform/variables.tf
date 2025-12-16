variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "app_name" {
  description = "Application name"
  default     = "visitor-app"
}

variable "container_port" {
  description = "Port the container listens on"
  default     = 8080
}
