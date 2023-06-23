# Slack Bot using AWS Lambda

<p align="center">
	<a href="https://join.slack.com/t/yrisgroupe/shared_invite/zt-1q51z8dmv-GC0XzUSclzBnUQ0tpKhznw"><img alt="Slack Shield" src="https://img.shields.io/badge/slack-yris-brightgreen.svg?logo=slack"></a>
	<a href="https://github.com/Yris-ops/slack-bot-aws-lambda"><img alt="Repo size" src="https://img.shields.io/github/repo-size/Yris-ops/slack-bot-aws-lambda"></a>
	<a href="https://github.com/Yris-ops/slack-bot-aws-lambda"><img alt="Stars" src="https://img.shields.io/github/stars/Yris-ops/slack-bot-aws-lambda"></a>
	<a href="https://twitter.com/cz_antoine"><img alt="Twitter" src="https://img.shields.io/twitter/follow/cz_antoine?style=social"></a>
	<a href="https://www.linkedin.com/in/antoine-cichowicz-837575b1"><img alt="Linkedin" src="https://img.shields.io/badge/-Antoine-blue?style=flat-square&logo=Linkedin&logoColor=white"></a>
<p>

This AWS CloudFormation template creates a simple Slack bot using AWS Lambda, Amazon API Gateway HTTP API, and AWS Identity and Access Management (IAM).

The Lambda function in this template receives an event from the HTTP API Gateway, extracts the body of the Slack event, and returns the challenge answer back to Slack.

## Setup 

You can find the details of the installation on this [blog post](https://medium.com/@antoinecichowicz/how-to-create-a-slack-bot-using-aws-lambda-in-10-minutes-665a9d6ae58e)

## Prerequisites

You will need:

- AWS account
- Slack Account and Slack Workspace

## How to Use

To use this CloudFormation template, follow these steps:

1. Upload the CloudFormation template to your AWS account.
1. Create a stack with the template in your AWS account.
1. When creating the stack, provide the Slack bot token and AWS account number as parameters.
1. After the stack is created, you can find the HTTP API endpoint in the stack output. Use this endpoint to configure your Slack bot's event subscriptions.
1. `python.py` file to update the Lambda function.

## CloudFormation Resources

This template creates the following resources:

- IAM role for the Lambda function
- Lambda function
- API Gateway HTTP API
- Lambda function resource permission for the API Gateway HTTP API

## Template Parameters

This template uses the following parameters:

- BotToken: The Slack bot token.
- AccountNumber: The AWS account number.
- AppName (optional): The name of the application. The default value is apigw-http-slack-lambda.

## Template Outputs

This template creates the following output:

- HttpApiEndpoint: The default endpoint for the HTTP API.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This repository is licensed under the Apache License 2.0. See the LICENSE file.