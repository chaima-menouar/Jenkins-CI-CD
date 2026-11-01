# Jenkins CI/CD Flask Demo

This project uses Jenkins to test and deploy a Python Flask demo application.

## Features
- Personalized welcome message
- Sum calculator
- Automated Python tests

## Pipeline
1. Checkout from GitHub main branch
2. Create Python virtual environment and install dependencies
3. Run test_app.py and test_app_2.py in parallel and publish JUnit results
4. Start Flask with Gunicorn on port 5000 and check the HTTP response

## Local tests
Run: `.venv/bin/python -m pytest test_app.py test_app_2.py -v`

## Jenkins setup
Create a Pipeline job using Pipeline script from SCM. Choose Git, branch `*/main`, and script path `Jenkinsfile`.

The Jenkinsfile configures a periodic trigger and a GitHub push trigger. Immediate push automation requires a working webhook. Confirm a new Jenkins build after a GitHub commit before considering this verified.

## Demo evidence
Earlier screenshots show two successful Jenkins builds, green stages, eight passing tests, a working greeting, and calculator output 30.0. A later commit changes the page title for an automation test. Confirm the new build in Jenkins.

Note: Codespaces is an ephemeral development environment, not permanent production hosting.
