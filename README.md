
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

Certainly! Below is the markdown file with detailed technical documentation and an explanation of each part of the Kubernetes YAML file. The document also includes key comments and technical notes to guide you through the process.

---


# 3 Deploy to Azure Kubernetes Service (AKS)

## Overview

This guide walks you through the steps to deploy the **Staff-Service Microservice** to **Azure Kubernetes Service (AKS)**. We will be using a Kubernetes YAML file to define both the **Deployment** and **Service** for the application, exposing it via a **LoadBalancer** to provide a **public endpoint**. This setup allows the microservice to be accessed externally for testing and interacting with CRUD operations.

---

## Steps to Deploy the Service

### 1. **Create AKS Cluster**

Certainly! Below is the markdown documentation for creating an Azure Kubernetes Service (AKS) cluster using the **Azure Portal (UI)**:

---

# Creating an Azure Kubernetes Service (AKS) Cluster via Azure Portal (UI)

## Overview

Azure Kubernetes Service (AKS) is a managed Kubernetes service that simplifies deploying and managing containerized applications using Kubernetes. In this guide, we will walk you through the process of creating an AKS cluster using the **Azure Portal**.

---

## Steps to Create an AKS Cluster via Azure Portal

### 1. **Log in to Azure Portal**

First, log in to the **Azure Portal** using your Azure account credentials.

- Navigate to [https://portal.azure.com](https://portal.azure.com) in your browser.
- Enter your credentials and click **Sign In**.

---

### 2. **Create a Resource Group**

A **Resource Group** is a container that holds related resources for your Azure solution. It’s a best practice to group your AKS cluster and associated resources together in one resource group.

To create a resource group, follow these steps:

1. In the Azure Portal, click **Create a resource** from the left sidebar.
2. In the search bar, type **Resource group** and select it from the list.
3. Click **Create**.
4. In the **Resource Group** creation page:
   - **Subscription**: Select your Azure subscription.
   - **Resource group name**: Enter a name for your resource group (e.g., `my-aks-rg`).
   - **Region**: Select the region where you want to create your AKS cluster (e.g., `East US`).
5. Click **Review + Create**, and then click **Create** once the validation passes.

---

### 3. **Create the AKS Cluster**

Once your resource group is created, proceed to create the AKS cluster:

1. In the Azure Portal, click **Create a resource** from the left sidebar.
2. In the search bar, type **Kubernetes Service** and select it from the list.
3. Click **Create**.
4. In the **Create Kubernetes Cluster** page:
   - **Subscription**: Choose your Azure subscription.
   - **Resource Group**: Select the resource group you just created.
   - **Kubernetes Cluster Name**: Enter a name for your AKS cluster (e.g., `my-aks-cluster`).
   - **Region**: Select the region where your AKS cluster will be deployed (e.g., `East US`).
   - **Kubernetes version**: Select the version of Kubernetes that you want to use (use the default version unless you have specific version requirements).

---

### 4. **Configure Node Pools**

In this step, you’ll configure the worker nodes for your AKS cluster. Follow these instructions:

1. Under the **Node pools** section:
   - **Node pool name**: Enter a name for your node pool (e.g., `master`).
   - **Node size**: Select the size for your nodes (e.g., `Standard_DS2_v4`).
   - **Node count**: Enter `1` for the number of nodes (you can scale later).
   - **OS disk size**: Select the disk size (default is 100 GB).
   


### 5. **Review + Create**

Before finalizing the creation of your AKS cluster, review all the settings:

1. Review all the settings for your AKS cluster.
2. If everything looks correct, click **Create** to start the deployment.

Azure will now create your AKS cluster. The process may take a few minutes.

---

Certainly! Below is the updated section for accessing your AKS cluster using the `az aks get-credentials` command, as you're using the Azure CLI instead of downloading the Kubeconfig from the Azure Portal:

---

### 6. **Access Your AKS Cluster**

Once the AKS cluster has been successfully created, you can access it using the Azure CLI:

1. Open your terminal or command prompt.
2. Run the following command to get the credentials for your AKS cluster:

   ```bash
   az aks get-credentials --resource-group finalexam --name <cluster name> --overwrite-existing
   ```

   - Replace `finalexam` with your resource group name.
   - Replace `bestbuycluster` with the name of your AKS cluster.
   - The `--overwrite-existing` flag ensures that if you have any existing configurations, they will be overwritten with the new configuration.

3. Once the credentials are successfully configured, you can verify the connection by running:

   ```bash
   kubectl get nodes
   ```

   This will list the nodes in your AKS cluster and confirm that you're connected.

---

This concludes the updated steps for accessing your AKS cluster using the Azure CLI.
---

### 7. **Verify the Cluster**

You can now verify that your AKS cluster is successfully running:

1. In the **Azure Portal**, go to your AKS cluster page.
2. Under **Settings**, click **Nodes**.
3. You should see your node(s) listed here.

---

```bash
az aks get-credentials --resource-group <resource-group-name> --name <aks-cluster-name>
```

This will allow you to interact with your AKS cluster from the command line.

---

### 2. **Write the Kubernetes Deployment YAML**

The **Deployment** YAML file defines the specifications for deploying your microservice in Kubernetes. It includes the container image, the number of replicas, and the port configuration. The **Service** YAML part defines how the service will be exposed to the outside world.

Here’s a breakdown of the key sections:

#### Deployment Section
- **Replicas**: Specifies the number of pod replicas. For simplicity, we are using a single replica.
- **Selector**: Ensures the Kubernetes system identifies the correct pods based on the labels.
- **Template**: Defines the pod template, including metadata and the container specifications.

#### Service Section
- **Selector**: The service uses the label defined in the deployment (`app: staff-service`) to route traffic to the appropriate pods.
- **Ports**: Defines the ports that will be exposed. Port 80 is exposed externally, and traffic is forwarded to port 5000 inside the container.
- **Type**: The service type is set to `LoadBalancer` to provision an external IP and expose the service to the public.

---

### 3. **Deploy the YAML File to AKS**

Once the YAML file is ready, apply it to the AKS cluster with the following command:

```bash
kubectl apply -f staff-service-deployment.yaml
```

This command will create the necessary resources (Deployment and Service) on the AKS cluster.

---

### 4. **Retrieve the Public IP Address**

Once the service is deployed, you can get the external IP assigned by the LoadBalancer. This can be done by running:

```bash
kubectl get services
```

Look for the `EXTERNAL-IP` column under your `staff-service-service`. It may take a few minutes for the IP to be assigned. Once you have the IP, you can use it to access the service publicly.

---

## Explanation of the YAML File

The YAML file is composed of two main sections: **Deployment** and **Service**. Below is a breakdown with comments explaining each part.

### Deployment

```yaml
apiVersion: apps/v1                # The API version for deployments
kind: Deployment                   # The kind of resource, which is Deployment
metadata:
  name: staff-service-deployment   # Name of the deployment
spec:
  replicas: 1                       # Number of pod replicas to run
  selector:
    matchLabels:
      app: staff-service            # Label selector to match the pods for this deployment
  template:
    metadata:
      labels:
        app: staff-service          # Labels for the pod template, used for identifying pods
    spec:
      containers:
      - name: staff-service         # Name of the container within the pod
        image: <your-dockerhub-username>/bestbuy-staff-service:latest  # Docker image for the service
        ports:
        - containerPort: 5000       # Expose port 5000 inside the container to communicate with the application
```

#### Key Points:
- **`apiVersion: apps/v1`**: Specifies the API version for the deployment resource.
- **`kind: Deployment`**: Specifies the kind of resource we are defining. In this case, it's a `Deployment`, which manages the application pods.
- **`metadata: name: staff-service-deployment`**: This defines the name of the deployment for identification.
- **`replicas: 1`**: Ensures that only one replica of the pod is running. You can scale this up later if needed.
- **`selector: matchLabels: app: staff-service`**: The selector ensures that the deployment manages the pods labeled with `app: staff-service`.
- **`containerPort: 5000`**: Exposes port 5000 from the container, where the microservice is listening.

---

### Service

```yaml
apiVersion: v1                     # The API version for services
kind: Service                       # The kind of resource, which is Service
metadata:
  name: staff-service-service       # Name of the service
spec:
  selector:
    app: staff-service              # Match the pods with the label `app: staff-service`
  ports:
    - protocol: TCP
      port: 80                       # Expose port 80 externally
      targetPort: 5000               # Forward the traffic to port 5000 on the container
  type: LoadBalancer                 # Expose the service via a LoadBalancer (external IP)
```

#### Key Points:
- **`apiVersion: v1`**: Specifies the API version for services.
- **`kind: Service`**: Specifies the kind of resource being defined, which is a `Service`. This allows the deployment to be accessible from the outside.
- **`selector: app: staff-service`**: This ensures the service routes traffic to the pods labeled `app: staff-service`.
- **`port: 80`**: Exposes the service on port 80 for external access.
- **`targetPort: 5000`**: The traffic on port 80 is forwarded to port 5000 inside the container.
- **`type: LoadBalancer`**: Configures the service to create an external LoadBalancer and assign a public IP.

---

## Testing the Service

After deploying the service and obtaining the **external IP**, you can test the service using **Send HTTP** or any HTTP client.

1. **Get the public IP**: 
   ```
   kubectl get services
   ```

2. **Test the service**: Use the external IP (e.g., `http://<external-ip>:80`) to test the CRUD operations exposed by the microservice.

---

## Conclusion

By following these steps, you have successfully deployed the **Staff-Service Microservice** to **Azure Kubernetes Service (AKS)**. The service is now publicly accessible via a **LoadBalancer**, allowing external access for testing and interaction via HTTP requests.


# Set Up CI/CD Pipeline (3 Marks)

### Objective:
The goal is to configure a CI/CD pipeline using **GitHub Actions** to automate the process of building, testing, and deploying the `staff-service` application.

### Steps:

1. **Configure the CI/CD Pipeline**

    - Create a `.github/workflows` directory in your project repository if it does not exist.
    - In this directory, create a file named `ci_cd.yaml` (or modify the provided file if it already exists).

    The **GitHub Actions workflow** (`ci_cd.yaml`) will define the steps for the CI/CD process:
    
    1. **Build**: Build the Docker image.
    2. **Test**: Run the necessary tests (e.g., unit tests, integration tests).
    3. **Push**: Push the Docker image to Docker Hub.
    4. **Deploy**: Deploy the application to the Azure Kubernetes Service (AKS) cluster.
    
    Push the **ci_cd.yaml** file to the repository with the commit message: `Adding CI/CD pipeline`.

2. **Set Up Secrets in GitHub**

    GitHub Actions requires several **secrets** for authentication and secure access to Docker Hub and Kubernetes. To add these secrets:
    
    - Go to **Settings** > **Secrets and variables** > **Actions** in your GitHub repository.
    
    Add the following repository secrets:
    
    - **DOCKER_USERNAME**: Your **Docker Hub username**.
    - **DOCKER_PASSWORD**: Your **Docker Hub password**.
    - **KUBE_CONFIG_DATA**: The **base64-encoded content** of your Kubernetes configuration file (`kubeconfig`). This is used for authentication with your Kubernetes cluster.
    
    To obtain `KUBE_CONFIG_DATA`:
    
    1. After connecting to your AKS cluster using `az aks get-credentials`, run the following command:
       ```bash
       cat ~/.kube/config | base64 -w 0 > kube_config_base64.txt
       ```
    2. Use the **content** of `kube_config_base64.txt` as the value for the **KUBE_CONFIG_DATA** secret in GitHub.

3. **Set Up Environment Variables (Repository Variables)**

    In **GitHub Actions**, set up the following **repository variables** to configure the deployment:
    
    - **DOCKER_IMAGE_NAME**: The name of the Docker image that will be built, tagged, and pushed. (Example: `bestbuy-staff-service`).
    - **DEPLOYMENT_NAME**: The name of the **Kubernetes deployment** to update. (Example: `staff-service-deployment`).
    - **CONTAINER_NAME**: The name of the **container** within the Kubernetes deployment to update. (Example: `staff-service`).
    
    Go to **Settings** > **Secrets and variables** > **Actions** in your GitHub repository and add these environment variables.

---

### Technical Overview of CI/CD Pipeline (ci_cd.yaml):

The `ci_cd.yaml` file will contain multiple stages, including build, test, push, and deploy. Here's a general structure:

- **Build Stage**:
    - Pulls the Dockerfile.
    - Builds the Docker image using `docker build`.
    - Tags the image with the version number.

- **Test Stage**:
    - Runs the tests using a testing framework (e.g., `pytest`).

- **Push Stage**:
    - Logs in to Docker Hub using the credentials stored in GitHub Secrets.
    - Pushes the built Docker image to your Docker Hub repository.

- **Deploy Stage**:
    - Uses Kubernetes CLI (`kubectl`) to deploy the updated image to the AKS cluster.
    - Updates the Kubernetes deployment with the new image.
    - Exposes the application to the internet via a LoadBalancer service.

---

### Conclusion:

By following the above steps, you will have a fully automated CI/CD pipeline that can build, test, push, and deploy the `staff-service` application using GitHub Actions and Azure Kubernetes Service (AKS).



## Test the CI/CD Pipeline (2 Marks)

### Objective:
Trigger the CI/CD workflow to ensure the process works as expected and verify the progress of the workflow jobs.

### Steps:

1. **Add a New User**:
   In your `app.py` file, add a new user to the data to test the CI/CD trigger. Here's an example of how the new user can be added:
   
   ```python
   # Adding one more data to test CI/CD Trigger
   "4": {
       "id": "4",
       "name": "Updated User",
       "position": "Updated Manager",
       "department": "Management",
       "email": "upd.johnson@bestbuy.com",
       "phone": "010-123-4567"
   }
   ```

2. **Commit and Push Changes**:
   Commit the changes made to the `app.py` file and push them to your repository:
   
   ```bash
   git add app.py
   git commit -m "Testing the triiger CI/CD pipeline"
   git push origin main
   ```

3. **Verify the CI/CD Pipeline**:
   - After pushing the changes, GitHub Actions will automatically trigger the pipeline.
   - Go to the **Actions** tab in your GitHub repository to view the progress of the workflow jobs.
   - Verify that the build, test, push, and deploy stages are running successfully.

4. **Check Deployment**:
   After successful deployment, you can verify that the new user data is available on the live service by accessing the exposed endpoint.

Here’s the README.md file based on your request:

---

# 6. BestBuy Staff Service Microservice

## Overview

The **BestBuy Staff Service** is a RESTful microservice that allows managing staff information within the organization. It supports basic CRUD operations (Create, Read, Update, Delete) for staff data, including details like name, position, department, email, and phone number. The microservice is designed for internal use and does not require a database, as it stores data in memory.

## Functionality

This microservice provides the following CRUD operations through REST APIs:

- **Create** a new staff member
- **Read** staff details (single or all)
- **Update** staff information
- **Delete** a staff member

## Endpoints

### 1. **Create a New Staff Member**

- **Endpoint**: `POST /staff`
- **Request Body**:
    ```json
    {
        "id": "4",
        "name": "Updated User",
        "position": "Updated Manager",
        "department": "Management",
        "email": "upd.johnson@bestbuy.com",
        "phone": "010-123-4567"
    }
    ```
- **Description**: Adds a new staff member to the system.

### 2. **Get All Staff Members**

- **Endpoint**: `GET /staff`
- **Response**:
    ```json
    {
        "1": { "id": "1", "name": "John Doe", "position": "Manager", "department": "Sales", "email": "john.doe@bestbuy.com", "phone": "123-456-7890" },
        "2": { "id": "2", "name": "Jane Smith", "position": "Assistant", "department": "Marketing", "email": "jane.smith@bestbuy.com", "phone": "987-654-3210" }
    }
    ```
- **Description**: Retrieves a list of all staff members.

### 3. **Get a Staff Member by ID**

- **Endpoint**: `GET /staff/{id}`
- **Example**: `GET /staff/1`
- **Response**:
    ```json
    {
        "id": "1",
        "name": "John Doe",
        "position": "Manager",
        "department": "Sales",
        "email": "john.doe@bestbuy.com",
        "phone": "123-456-7890"
    }
    ```
- **Description**: Retrieves information for a specific staff member based on the provided ID.

### 4. **Update Staff Information**

- **Endpoint**: `PUT /staff/{id}`
- **Request Body**:
    ```json
    {
        "name": "John Doe Updated",
        "position": "Senior Manager",
        "department": "Sales",
        "email": "john.doe.updated@bestbuy.com",
        "phone": "123-456-7890"
    }
    ```
- **Description**: Updates information for a specific staff member based on the provided ID.

### 5. **Delete a Staff Member**

- **Endpoint**: `DELETE /staff/{id}`
- **Description**: Deletes a staff member from the system based on the provided ID.

---

## Tasks Completed

1. **Developed the Staff-Service Microservice**:
   - Created a simple RESTful microservice to manage staff information using Python (Flask).
   - Implemented CRUD operations for staff data.
   - Test using `test_CRUD.http`

2. **Containerized the Service**:
   - Created a Dockerfile and containerized the application.
   - Pushed the Docker image to Docker Hub.

3. **Deployed the Service to AKS**:
   - Created an Azure Kubernetes Service (AKS) cluster.
   - Deployed the microservice on AKS using a Kubernetes deployment YAML file.

4. **Set Up CI/CD Pipeline**:
   - Configured GitHub Actions for building, testing, and deploying the staff service.

5. **Trigger the CI/CD pipeline**

---

## Technical Issues Encountered

- **Issue with Secrets**: Once the Secret and variables updated in repo and re rerun the jobs it was successfull

- **Docker Hub Password**: Reset Docker hub password to solved the issue.

---

