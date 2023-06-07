# End-to-End Text-Summarizer

This repository contains an end-to-end implementation of a Text-Summarizer, which aims to generate concise summaries of input text documents. The summarization process is performed using a pipeline consisting of several components that work together to extract key information and generate a summary.

Please note that the model in this repository has not been trained on my machine as it does not have a GPU :( . Therefore, no evaluation or prediction can be performed. However, all the modules required for the Text-Summarizer have been written completely.

## Workflow

To use this Text-Summarizer, follow the workflow outlined below:

1. Update `config.yaml`: Modify the configuration file to specify any required settings and parameters for the summarization process.

2. Update `params.yaml`: Customize the parameters file to adjust various options and settings specific to your summarization requirements.

3. Update `entity`: Modify the entity file to define the entities or topics of interest for summarization.

4. Update the configuration manager in `src config`: Make any necessary updates to the configuration manager module to ensure it reflects your desired configuration.

5. Update the components: Modify the individual components of the summarization pipeline to tailor the summarization process to your specific needs.

6. Update the pipeline: Customize the pipeline module to define the sequence of steps and components involved in the summarization process.

7. Update `main.py`: Make necessary modifications to the main script file to incorporate any changes made in the previous steps.

8. Update `app.py`: Customize the application script to define the interface or integration points for interacting with the Text-Summarizer.

## AWS-CICD-Deployment-with-Github-Actions

Continuous Integration and Continuous Deployment (CI/CD) with GitHub Actions provides an automated and streamlined approach for deploying your application or project to AWS. It offers several advantages, including improved development efficiency, faster release cycles, and reliable deployment processes.

CI/CD involves the integration of code changes, building the application, running tests, and deploying it to the target environment automatically. GitHub Actions, combined with AWS services, allows you to set up a CI/CD pipeline that automates the entire software delivery process.


This section provides instructions for deploying the Text-Summarizer using AWS services and GitHub Actions.

1. Login to the AWS console.

2. Create an IAM user for deployment with the necessary access permissions. Grant the following access:

   - EC2 access: Allows managing virtual machines.
   - ECR: Enables saving the Docker image in AWS Elastic Container Registry.

   Ensure you note down the access key and secret access key for the IAM user.

3. Create an ECR repository to store the Docker image. Save the repository URI for later use.

   Example URI: `162741883631.dkr.ecr.eu-north-1.amazonaws.com/text-s`

4. Create an EC2 machine (Ubuntu) for deployment.

5. Open the EC2 instance and install Docker:

   ```shell
   # Optional updates
   sudo apt-get update -y
   sudo apt-get upgrade

   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

6. Configure the EC2 instance as a self-hosted runner:

   - Go to EC2 instance settings > Actions > Runner > New self-hosted runner.
   - Choose the operating system and follow the provided commands to configure the runner.

7. Set up GitHub secrets for the repository:

   - `AWS_ACCESS_KEY_ID`: The access key ID of the IAM user created for deployment.
   - `AWS_SECRET_ACCESS_KEY`: The secret access key corresponding to the IAM user.
   - `AWS_REGION`: The AWS region for deployment (e.g., `us-east-1`).
   - `AWS_ECR_LOGIN_URI`: The ECR login URI, such as `demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com`.
   - `ECR_REPOSITORY_NAME`: The name of the ECR repository for storing the Docker image (e.g., `simple-app`).

Adapt the steps as needed for your specific deployment requirements.

Feel free to explore the code and adapt it to your specific use cases or requirements. If you have any questions or encounter any issues, please reach out.

## Disclaimer

Please note that the information and instructions provided in this README are for educational and informational purposes only. The deployment process outlined in the "AWS-CICD-Deployment-with-Github-Actions" section may not cover all possible scenarios or configurations, and it is recommended to refer to official AWS documentation and consult with experienced professionals when implementing a CI/CD pipeline for your specific project.

Deploying applications and utilizing AWS services involve potential risks and considerations related to security, cost, and compliance. It is essential to thoroughly review and understand the implications of deploying your application on AWS and follow best practices to ensure the security and stability of your infrastructure.

Users are solely responsible for their actions and decisions related to the deployment process and usage of AWS services.

Always exercise caution and refer to official documentation and expert advice when working with AWS services and implementing CI/CD pipelines.

