output "application_url" {
  description = "Public URL of the application"
  value       = aws_lb.this.dns_name
}
