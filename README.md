# Cloud-Security-Analyzer

## Description
The **Cloud Security Analyzer** is a tool designed to scan cloud environments (AWS, GCP) for potential security misconfigurations and policy violations. This script automates the process of risk assessment, identifies vulnerabilities in cloud infrastructure, and generates compliance reports. It also provides real-time alerts when security risks are found.

The tool is primarily used for:
- Scanning AWS and GCP environments for misconfigured resources, such as unencrypted storage buckets, overly permissive IAM roles, and insecure network configurations.
- Automatically alerting users of identified risks.
- Generating compliance reports to aid in auditing and security assessments.

> **Important**: This tool is meant to be used on your own cloud environments. Ensure you have the necessary access credentials (tokens) set up for AWS and GCP to use the tool effectively.

## Features
- **AWS Security Checks**: Automatically scans AWS environments for misconfigured S3 buckets, IAM roles, security groups, etc.
- **GCP Security Checks**: Identifies insecure storage buckets, misconfigured permissions, and other GCP-specific issues.
- **Automated Alerts**: Receives notifications and alerts in case of any security issues or misconfigurations.
- **Compliance Reporting**: Generates detailed reports for identified security issues.

## Installation

### Requirements
- Python 3.x
- AWS CLI configured with access keys
- Google Cloud SDK

### Steps to Install:

1. Clone the repository and navigate to the project folder.
2. Install dependencies by running the command to install all the required packages listed in the `requirements.txt` file.
3. Set up cloud credentials for AWS and GCP. You’ll need to configure the access tokens for these services to allow the tool to scan your cloud environments. See below for how to obtain and set up your credentials for each service:

#### AWS:
   - Set up the AWS CLI and configure your credentials by running "aws configure".
   - Enter your `AWS Access Key ID`, `AWS Secret Access Key`, and default region when prompted.

#### GCP:
   - Install the Google Cloud SDK and authenticate using your credentials.
   - Set your project in the configuration by exporting the path to the generated JSON file.

4. Run the script to start the analysis.

## Usage
- The script automatically scans your cloud accounts (AWS, GCP) for misconfigurations and security violations.
- After running, results will be printed with a list of identified issues. Each issue will specify the cloud provider, resource type, and the nature of the security concern.
- The script will also send notifications of security risks if configured.

## Security Tokens and API Keys
This tool works by authenticating with AWS and GCP using your personal cloud credentials. These credentials (tokens and keys) allow the tool to access and scan your cloud environments. Do **not** share your tokens with anyone. Keep your credentials secure and use them only with trusted tools.

## Contributing
Feel free to fork the repository and contribute improvements. If you find bugs or would like to suggest new features, please open an issue or create a pull request.

