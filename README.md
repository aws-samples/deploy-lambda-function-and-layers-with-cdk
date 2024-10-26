# Deploy Lambda Function and Layers with CDK

This project demonstrates how to deploy an AWS Lambda function along with its layers using the AWS Cloud Development Kit (CDK).

## Project Overview

This CDK project automates the deployment of a Lambda function and its associated layers. It showcases best practices for structuring Lambda projects and managing dependencies through layers.

## Prerequisites

- AWS CLI configured with appropriate permissions
- Node.js and npm installed
- AWS CDK CLI installed (`npm install -g aws-cdk`)
- Python 3.8 or later

## Setup and Deployment

1. Clone the repository:

2. Install dependencies:


3. Build your Lambda function and place it in the `app/build/` directory.

4. Deploy the CDK stack:

```cdk deploy```


## Configuration

The main stack is defined in `infra/infra_stack.py`. Key configurations include:

- Lambda function settings (runtime, handler, etc.)
- Layer definitions
- Artifact packaging (`app/build/*` into `LambdaLayer.zip`)

## Customization

- Modify the Lambda function code in the `app/` directory.
- Adjust layer configurations in the CDK stack file as needed.
- Update the artifact packaging in the stack if your build output location changes.

## Cleanup

To remove all resources created by this stack:

```cdk destroy```


## Contributing

Contributions to improve the project are welcome. Please follow the standard GitHub pull request process to propose changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

