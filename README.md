# Overview

This project is a machine learning microservice for house price prediction using Flask and Scikit-learn, deployed with Azure CI/CD pipelines.

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

# Create a web app
Go to Azure protal, click app service, then create a app service named songyang
Set up the app service:
Using the exsiting resource group
Set the Runtime stack as python 3.9 
Set the Pricing plan as Free F1 # very important

# Setup Azure Cloud Shell and clone the project
Setup Azure Cloud Shell
![alt text](./screenshot/azure_cloud_shell.png)


* clone the project in Azure Cloud Shell
git clone https://github.com/Stacy517/azure-cicd-pipeline-flask.git
![alt text](./screenshot/screenshot-git-clone.png)

* Go to the project directory
cd azure-cicd-pipeline-flask/flask-sklearn

* Create a python virtual environment
python3 -m venv ~/.devops
source ~/.devops/bin/activate

# Project running on Azure App Service
chmod +x make_predict_azure_app.sh
./make_predict_azure_app.sh
![alt text](./screenshot/running_app.png)


# Run initial setup
make all

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![alt text](./screenshot/makeall_test.png)


* Output of a test run

* Successful deploy of the project in Azure Pipelines.  


* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  
[![Python application test with Github Actions](https://github.com/Stacy517/azure-cicd-pipeline-flask/actions/workflows/myapp.yml/badge.svg)](https://github.com/Stacy517/azure-cicd-pipeline-flask/actions/workflows/myapp.yml)


The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


