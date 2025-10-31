# cloudify-serverless-app
A fully functional Serverless Web Application built on AWS using S3, CloudFront, Lambda, API Gateway, and DynamoDB. This project demonstrates how to deploy a scalable, cost-efficient, and serverless web application to store and retrieve data through RESTful APIs.
# AWS Serverless Web Application with CloudFront

## Overview
This project demonstrates a complete **serverless web application** deployed on AWS. The app allows users to save and view data (Employee details or any structured data) using **AWS S3**, **API Gateway**, **AWS Lambda**, and **DynamoDB**. The static frontend is globally delivered via **Amazon CloudFront** for optimized performance and HTTPS access.

**Key AWS Services Used:**
- **Amazon S3** – Hosts the static HTML/JS frontend.
- **Amazon CloudFront** – Distributes the frontend globally with low latency.
- **Amazon API Gateway** – Handles HTTP requests and routes them to Lambda functions.
- **AWS Lambda** – Executes backend logic (inserting and retrieving data).
- **Amazon DynamoDB** – Stores and retrieves structured data.
  
---

## Features
- **Insert Data:** Add new entries via a simple web form.
- **View Data:** Display all stored entries dynamically on the web page.
- **Serverless Architecture:** No servers to manage; scales automatically with demand.
- **Global Access:** Delivered through CloudFront for high availability and low latency.
- **Secure & Cost-Efficient:** Pay-per-use architecture without maintaining infrastructure.

---

## Architecture

<img width="940" height="390" alt="severless drawio" src="https://github.com/user-attachments/assets/ba0eeffc-fad3-4f51-adfe-6bef8fbc0e6a" />

Frontend (HTML/JS hosted on S3)
|
v
API Gateway (REST endpoints)
/insert --> Lambda (Insert Data) --> DynamoDB
/employees --> Lambda (Get Data) --> DynamoDB
|
v
CloudFront (Global Distribution)


*(Add architecture diagram screenshot here)*

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Omkar8284/cloudify-serverless-app/
cd /cloudify-serverless-app/

2. Configure Frontend

Open index.html.

Update apiBaseUrl with your API Gateway invoke URL:

const insertUrl = "https://<invoke url>.execute-api.ap-south-1.amazonaws.com/prod/insert";
    const getUrl = "https://<invoke url>.execute-api.ap-south-1.amazonaws.com/prod/employees";

<img width="1712" height="406" alt="image" src="https://github.com/user-attachments/assets/0816697f-91de-4803-9529-730fd248d9de" />

3. Deploy Frontend to S3

Create a new S3 bucket (e.g., my-serverless-webapp) and enable static website hosting.

Upload index.html and other assets.

4. Create DynamoDB Table

Table Name: employeedata

Partition Key: employeeid (String)

5. Create Lambda Functions

insertEmployeeData – Inserts data into DynamoDB.

getEmployees – Fetches data from DynamoDB.

Runtime: Python 3.13

Attach AmazonDynamoDBFullAccess and AWSLambdaBasicExecutionRole.

6. Configure API Gateway

REST API with two resources:

/insert → POST → insertEmployeeData

/employees → GET → getEmployees

Enable CORS for both resources.

Deploy to stage prod.

7. Optional: CloudFront

Create a CloudFront distribution with the S3 bucket as origin.

Enable HTTPS and caching for faster global delivery.

Usage: 

Open your CloudFront or S3 website URL in a browser.

Fill out the form and click Save Data.

Click View All Data to fetch and display entries.

• Technologies

AWS S3
AWS CloudFront
AWS Lambda (Python 3.13)
Amazon API Gateway
Amazom DynamoDB
HTML / JavaScript

Contributing

Contributions are welcome! Feel free to submit pull requests for improvements, bug fixes, or additional features.
