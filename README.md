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


