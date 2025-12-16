# Particle41 DevOps Challenge

## What is this?
This repository contains a small web application created as part of the Particle41 DevOps challenge.
The goal is to build something simple, containerize it properly, and make sure anyone on the team
can run it without confusion.

The application returns:
- The current timestamp
- The IP address of the visitor

## What does the app return?
When you access the application, it responds in the following format:

{
  "timestamp": "<current date and time>",
  "ip": "<the IP address of the visitor>"
}

## Project layout
├── structure/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── terraform/
│ ├── main.tf
│ ├── variables.tf
│ ├── provider.tf
│ ├── iam.tf
│ ├── logs.tf
│ └── outputs.tf
└── README.md

## Tech used
- Python
- FastAPI
- Docker- Python (FastAPI)
- Docker
- AWS ECR
- AWS ECS (Fargate)
- Application Load Balancer (ALB)
- Terraform

## What do you need?
Before starting, make sure you have:
- Docker installed
- Git installed Docker installed
- AWS CLI configured
- Terraform installed
- An AWS account

No cloud account or extra tools are required to run the app locally.

## How to build the container
From the root of the repository, run:

```bash
docker build -t visitor-app ./structure
docker run -p 8080:8080 visitor-app

Open your browser and go to:

http://localhost:8080

Result be

{
  "timestamp": "2025-12-16T14:38:23.912039",
  "ip": "172.17.0.1"
}

To stop the container, press CTRL + C.

Pushing the image to Amazon ECR
Create the ECR repository (one-time)
aws ecr create-repository --repository-name visitor-app --region us-east-1

To Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 \
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

To Tag and push the image
docker tag visitor-app:latest <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/visitor-app:latest
docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/visitor-app:latest

To remove the Docker image:

docker rmi visitor-app

Deploy the infrastructure
cd terraform
terraform init
terraform plan
terraform apply


After the apply completes, Terraform outputs the public ALB URL:

application_url = visitor-app-xxxxxx.us-east-1.elb.amazonaws.com

Accessing the deployed application

Open the ALB URL in a browser:

http://visitor-app-2031529899.us-east-1.elb.amazonaws.com


You should receive a response similar to:

{
  "timestamp": "2025-12-16T14:35:19.239611",
  "ip": "x.x.x.x"
}

To Cleanup 

To avoid ongoing AWS charges, destroy all resources when finished:

cd terraform
terraform destroy


---

## Code References

The following official documentation and references were used while designing and implementing this project:

### Application & Framework
- FastAPI documentation  
  https://fastapi.tiangolo.com/

- Uvicorn ASGI server  
  https://www.uvicorn.org/

### Docker
- Dockerfile best practices  
  https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

- Running containers as a non-root user  
  https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user

### AWS ECS & Fargate
- Amazon ECS Developer Guide  
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html

- ECS task definitions  
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html

- ECS Fargate launch type  
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html

### Application Load Balancer
- Application Load Balancer documentation  
  https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html

- Target groups for ALB  
  https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html

### Amazon ECR
- Amazon Elastic Container Registry documentation  
  https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html

- Authenticating Docker to ECR  
  https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html

### Terraform
- Terraform documentation  
  https://developer.hashicorp.com/terraform/docs

- AWS Provider for Terraform  
  https://registry.terraform.io/providers/hashicorp/aws/latest/docs

- terraform-aws-modules VPC module  
  https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest

### Logging & Monitoring
- CloudWatch Logs for Amazon ECS  
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_cloudwatch_logs.html
