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
└── README.md

## Tech used
- Python
- FastAPI
- Docker

## What do you need?
Before starting, make sure you have:
- Docker installed
- Git installed

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
To remove the Docker image:

docker rmi visitor-app