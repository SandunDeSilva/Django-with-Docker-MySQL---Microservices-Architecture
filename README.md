# Django-with-Docker-MySQL---Microservices-Architecture
A microservices-based Django application containerized with Docker, using MySQL as the database. This project demonstrates how to structure a Django application with two separate apps (app1 and app2), each running on different ports (8000 &amp; 8001).

# Django with Docker and MySQL

This project demonstrates how to containerize a Django application with MySQL using Docker. The application consists of two apps (`app1` and `app2`), each running on different ports.

---

## **Prerequisites**
Before running this project, ensure you have the following installed:
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (for Windows/macOS)
- Python (latest stable version)
- VS Code or any code editor

---

## **Getting Started**

### **Step 1: Open Docker Desktop**
1. Launch Docker Desktop on your Windows machine.
2. Ensure Docker is running by executing:
   ```sh
   docker --version
It should return the installed Docker version.

Step 2: Clone the Repository
If you haven’t already, clone this project:

git clone https://github.com/SandunDeSilva/Django-with-Docker-MySQL---Microservices-Architecture.git

cd myproject

Step 3: Build and Run the Containers
To start the Django and MySQL services, run:

docker-compose up --build

This will:
Start the MySQL database container.
Build and start the Django application container.

Step 4: Apply Migrations and Create Superuser
Once the containers are running, open a new terminal and run:

# Run makemigrations

docker exec -it django_container python manage.py makemigrations

# Apply migrations

docker exec -it django_container python manage.py migrate

# Create a superuser (follow the prompts)

docker exec -it django_container python manage.py createsuperuser

Step 5: Access the Application
Once everything is running, you can access:

App1 (Items API) → http://localhost:8000/app1/items/
App2 (Products API) → http://localhost:8001/app2/products/
Django Admin Panel → http://localhost:8000/admin/

