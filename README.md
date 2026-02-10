Rick & Morty Cloud-Native API 🚀
This project demonstrates a production-grade CI/CD pipeline and Kubernetes orchestration for a Flask-based API. The application integrates with the Rick & Morty API, filtering data to return specific character information.

🛠 Tech Stack
    
    • Language: Python (Flask)
    
    • Containerization: Docker

    • Orchestration: Kubernetes (K8s)

    • Package Management: Helm

    • CI/CD: GitHub Actions

    • Local Cluster: Kind / Minikube

🚀 Getting Started
1. Running with Docker
To build and run the application locally using Docker:
- docker build -t rick-morty-app:latest .
- docker run -p 5000:5000 rick-morty-app:latest

2. Deployment with Kubernetes (Manual)
The raw Kubernetes manifests are located in the /yamls directory:
- kubectl apply -f yamls/deployment.yaml
- kubectl apply -f yamls/service.yaml

3. Deployment with Helm
The project includes a modular Helm Chart for easier configuration management:
- helm install rick-release ./Helm/rick-morty-app

🛣 API Endpoints
    • GET /characters: Returns a filtered JSON list of characters who are Human, Alive, and from Earth.
      
    • GET /healthcheck: Returns a 200 OK status to verify the application and connectivity are healthy.

🔄 CI/CD Pipeline (GitHub Actions)
The project utilizes GitHub Actions to ensure code quality and deployment stability on every push.

The pipeline performs the following steps:
    1. Cluster Creation: Provisions a local Kubernetes cluster using Kind.
    2. Docker Build: Builds the container image from the Dockerfile.
    3. Image Loading: Sideloads the image into the Kind nodes.
    4. Helm Deployment: Installs the application using the Helm Chart.
    5. Automated Testing:
    • Waits for the Deployment rollout to complete.
    • Performs a port-forward to the service.
    • Executes curl commands to validate both the /healthcheck and /characters endpoints.

📁 Project Structure
    • .github/workflows/: CI/CD pipeline configuration.
      
    • Helm/: Modular Helm Chart templates and values.
      
    • yamls/: Static Kubernetes manifests.
      
    • app.py: Flask application logic.
      
    • Dockerfile: Container build instructions.
