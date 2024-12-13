
# Staff-Service Microservice

This is a simple **Staff-Service Microservice** developed to manage staff information for Best Buy. The service provides REST APIs for handling CRUD operations (Create, Read, Update, Delete) on staff data, which is stored in memory for simplicity. The project adheres to the **12-Factor App** principles to ensure scalability, maintainability, and portability.

## 1. Develop the Staff-Service Microservice (4 Marks)

### Overview

The **Staff-Service Microservice** provides a RESTful API to manage staff information. The service allows for the following operations:
- **Create**: Add a new staff member.
- **Read**: Retrieve information about all staff or a specific staff member.
- **Update**: Modify the details of an existing staff member.
- **Delete**: Remove a staff member from the system.

### Technical Documentation

The service is implemented using **Python** and the **Flask** web framework. Here's a breakdown of how the microservice is built and configured:

#### 1.1 Project Structure

The project is organized as follows:
```
staff-service/
│
├── app.py              # Main application file with API logic
├── requirements.txt    # Lists required Python dependencies
├── .env                # Stores environment variables (e.g., port number)
└── README.md           # This file, providing an overview and technical details
```

#### 1.2 Dependencies

The microservice uses the following Python libraries:
- **Flask**: A lightweight WSGI web application framework for Python.
- **python-dotenv**: A Python library to read key-value pairs from `.env` files and add them to environment variables.

The dependencies are listed in the `requirements.txt` file, and can be installed using the command:

```bash
pip install -r requirements.txt
```

#### 1.3 Environment Configuration

To configure the port number dynamically, an `.env` file is used. It stores the environment variable for the port as follows:

```ini
PORT=5000
```

The `python-dotenv` library loads this value into the Flask app, making it easy to adjust the port when deploying to different environments.

#### 1.4 API Endpoints

The microservice provides the following CRUD operations as RESTful API endpoints:

1. **Create Staff**
   - **POST** `/staff`
   - Request Body (JSON):
     ```json
     {
       "name": "John Doe",
       "position": "Sales Associate",
       "department": "Sales",
       "email": "john.doe@bestbuy.com",
       "phone": "555-555-5555"
     }
     ```


### 12-Factor App Principles Applied

1. **Codebase**: The app uses a single GitHub repository with one codebase deployed across multiple environments.
2. **Dependencies**: All dependencies are listed in `requirements.txt` to ensure isolation and easy environment setup.
3. **Config**: Configuration like the port number is stored in the `.env` file, loaded at runtime via `python-dotenv`.
4. **Backing Services**: No external services are used, but in a real-world scenario, backing services like databases would be configured via environment variables.

---

2. **Read All Staff**
   - **GET** `/staff`
   - Returns a list of all staff members.

3. **Read Staff by ID**
   - **GET** `/staff/{id}`
   - Returns details of a staff member based on their ID.

4. **Update Staff**
   - **PUT** `/staff/{id}`
   - Request Body (JSON):
     ```json
     {
       "id": "1",
       "name": "Jane Doe",
       "position": "Senior Sales Associate",
       "department": "Sales",
       "email": "jane.doe@bestbuy.com",
       "phone": "555-555-1234"
     }
     ```

5. **Delete Staff**
   - **DELETE** `/staff/{id}`
   - Deletes the staff member with the specified ID.

#### 1.5 Codebase and GitHub Repository

The source code for the microservice is tracked in a **GitHub repository**. The initial codebase was pushed with the following commit message:

```bash
Initial Commit
```

The repository is located at: [bestbuy-staff-service](https://github.com/yourusername/bestbuy-staff-service)

#### 1.6 Running the Service

To run the microservice locally:
1. Ensure that you have Python installed and the dependencies are set up using `pip install -r requirements.txt`.
2. Run the Flask app:
   ```bash
   flask run
   ```
3. The service will be available at `http://localhost:5000`.

You can test the CRUD operations using an HTTP client like **Postman** or by using a `.http` file with a REST Client in **VS Code**.

#### 1.7 Sample Data

The microservice can be tested with the following sample data for staff:

1. Staff 1:
   - Name: **Michael Scott**
   - Position: **Regional Manager**
   - Department: **Sales**
   - Email: **michael.scott@bestbuy.com**
   - Phone: **555-555-5555**

2. Staff 2:
   - Name: **Jim Halpert**
   - Position: **Sales Associate**
   - Department: **Sales**
   - Email: **jim.halpert@bestbuy.com**
   - Phone: **555-555-1234**

---


### Conclusion

This simple **Staff-Service Microservice** offers a scalable, stateless way to manage staff information. By following the **12-factor app** principles and storing configuration in environment variables, this service can easily be deployed and maintained in various cloud environments.

---


# 2. Containerize the Service (4 Marks)

### Dockerizing the Staff-Service Microservice

To make the **Staff-Service Microservice** portable and easily deployable, I containerized the application using Docker. Below are the steps taken:

### 2.1 Docker Image Creation

A `Dockerfile` was created to containerize the **Staff-Service Microservice**. This file contains the instructions for building the Docker image, including setting up the Python environment, installing dependencies, and defining the commands to run the Flask application.

### 2.2 Build the Docker Image

After creating the `Dockerfile`, the following command was used to build the Docker image:

```bash
docker build -t bestbuy-staff-service .
```

This command builds the Docker image from the current directory (`.`), tagging it with the name `bestbuy-staff-service`.

### 2.3 Push the Docker Image to Docker Hub

Once the Docker image was built, it was pushed to my personal Docker Hub account for easy access and deployment.

1. **Login to Docker Hub**:
   
   ```bash
   docker login
   ```

   Enter your Docker Hub credentials to log in.

2. **Tag the Docker Image**:

   ```bash
   docker tag bestbuy-staff-service <your-dockerhub-username>/bestbuy-staff-service
   ```

   Replace `<your-dockerhub-username>` with your actual Docker Hub username.

3. **Push the Docker Image**:

   ```bash
   docker push <your-dockerhub-username>/bestbuy-staff-service
   ```

   This uploads the image to Docker Hub, where it can be accessed from anywhere.

### 2.4 Docker Hub Link

After pushing the image to Docker Hub, you can access it using the following link. Please replace `<your-dockerhub-username>` with your actual username:

Link to docker hub image: [Docker Hub - bestbuy-staff-service](https://hub.docker.com/repository/docker/thoufeekx/bestbuy-staff-service/general)

### 2.5 Commit the Dockerfile

The `Dockerfile` was added to the repository and committed with the following message:

```
"Adding Dockerfile"
```
