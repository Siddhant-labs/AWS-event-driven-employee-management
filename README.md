# AWS Event-Driven Employee Management System

## About the Project

I built this project to get hands-on experience with Python Flask and AWS services by creating a simple employee management application.

The application runs on an EC2 instance and uses DynamoDB to store employee information. I integrated DynamoDB Streams with AWS Lambda so that database changes can trigger automatic processing. CloudWatch is used to check Lambda execution logs and troubleshoot issues.

## Architecture

**Application Flow:**

User → Flask Application (EC2) → DynamoDB → DynamoDB Streams → Lambda → CloudWatch

Amazon S3 is planned for storing employee resumes as a future enhancement.

## AWS Services Used

- **EC2:** Hosts the Flask web application.
- **DynamoDB:** Stores employee records.
- **DynamoDB Streams:** Captures changes made to employee records.
- **AWS Lambda:** Processes INSERT, MODIFY, and REMOVE events.
- **CloudWatch:** Helps monitor Lambda execution and debug errors.
- **IAM:** Manages permissions required for AWS service integration.
- **S3:** Planned for employee resume storage.

## How It Works

1. A user interacts with the Flask web application.
2. Employee information is stored or updated in DynamoDB.
3. DynamoDB Streams captures changes to the records.
4. Lambda is triggered to process the database events.
5. CloudWatch logs help verify execution and identify errors.

## Technologies

Python, Flask, AWS EC2, Amazon DynamoDB, DynamoDB Streams, AWS Lambda, Amazon CloudWatch, IAM, and Amazon S3 (planned).

## What I Learned

While working on this project, I gained practical experience with:

- Deploying a Python Flask application on EC2.
- Connecting a web application to DynamoDB.
- Using DynamoDB Streams to capture database changes.
- Triggering Lambda functions through database events.
- Managing IAM permissions between AWS services.
- Using CloudWatch logs for monitoring and troubleshooting.

