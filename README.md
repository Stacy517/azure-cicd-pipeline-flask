# Overview

This project is a machine learning microservice for house price prediction using Flask and Scikit-learn, deployed with Azure CI/CD pipelines.

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>
![alt text](./screenshot/arch_image.png)

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

# Create a web app
Go to Azure protal, click app service, then create a app service named songyang
Set up the app service:
Using the exsiting resource group
Set the Runtime stack as python 3.9 
Set the Pricing plan as Free F1 # very important
![alt text](./screenshot/create_web_service.png)

# Setup Azure Cloud Shell
Setup Azure Cloud Shell
![alt text](./screenshot/azure_cloud_shell.png)

# Clone the project in Azure Cloud Shell and Run initial setup(This following steps are for the Github Action to run the test, not for the Azure Pipelines.)
* clone the project in Azure Cloud Shell
git clone https://github.com/Stacy517/azure-cicd-pipeline-flask.git
![alt text](./screenshot/screenshot-git-clone.png)

* Go to the project directory
cd azure-cicd-pipeline-flask/flask-sklearn

* Create a python virtual environment
python3 -m venv ~/.devops
source ~/.devops/bin/activate

* Run initial setup
make all

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![alt text](./screenshot/makeall_test.png)

[![Python application test with Github Actions](https://github.com/Stacy517/azure-cicd-pipeline-flask/actions/workflows/myapp.yml/badge.svg)](https://github.com/Stacy517/azure-cicd-pipeline-flask/actions/workflows/myapp.yml)

# Setup Azure Pipelines
<!-- * First, create a managed identity for the app service
Because we create the app service as free F1, we need to create a user assigned  identity for the app service.
![alt text](./screenshot/create_identity.png)

* Assign the managed identity to the app service
Go to the app service, click settings > identity, click user assigned, then assign the managed identity to the app service.

* Add role assignment to the managed identity
Click the Access control (IAM) in the left menu, click Add > Add role assignment
choose the role as Website contributor, go next, then choose the managed identity, select the user assigned identity you created, then click assign -->

<!-- Go to the exsiting resource group, click the Access control (IAM) in the left menu, click Add > Add role assignment. Choose the role as Managed Identity Contributor, go next, then choose the managed identity, select the user assigned identity you created, then click assign. If you don't do this step, you will get the error message: "The identity does not have access to perform action blabla". -->

<!-- * Finally, you can setup the deployment center for the app service
Go to the app service, click settings > deployment center, then choose the source as GitHub, login your Github account, then choose the repository and branch you want to deploy, choose the user-assigned identity you created, then click save -->

* Setup the deployment center of the app service
Go to the app service, click settings > deployment center, then choose the source as GitHub, change the provider as "Building with Azure Pipelines". 

* Setup the Azure pipeline
Go to  Azure DevOps portal, click Pipelines > New pipeline, then choose the GitHub as the source, then choose the repository and branch you want to deploy.
Choose the exsiting Azure Pipeline YAML file. 
![alt text](./screenshot/setup_azure_pipeline.png)

# Configure self-hosted agents
In the last step, you may get the error message:No hosted parallelism has been purchased or granted. To request a free parallelism grant, please fill out the following form https://aka.ms/azpipelines-parallelism-request

You can request a free parallelism grant or configure a self-hosted agent by this following steps:
* create a VM
az vm create \
--name DevOpsAgentVM \
--resource-group Azuredevops \
--image Ubuntu2204 \
--size Standard_B1s \
--admin-username azureuser \
--generate-ssh-keys \
--public-ip-address-dns-name devops-agent-sg
* login to the VM
ssh azureuser@<vm_ip_address>

* install the dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl gnupg2 software-properties-common unzip
sudo apt install -y python3 python3-pip

* download the agent 
mkdir myagent && cd myagent
wget https://vstsagentpackage.azureedge.net/agent/3.242.0/vsts-agent-linux-x64-3.242.0.tar.gz
tar zxvf vsts-agent-linux-x64-3.242.0.tar.gz

* run the agent
./config.sh --unattended \
--url https://dev.azure.com/{your_org_name} \  
--auth pat \
--token {your PAT} \ 
--pool Default \
--agent devops-vm-agent \
--replace \
--acceptTeeEula


# Setup the pipeline project
Go to Azure DevOps portal, click the left below button: project settings
Go to the Pipelines > Service connections, click New service connection, then choose the Azure Resource Manager, then choose the subscription, resource group.
then input the Service Connection Name, this name should be the same as the name you used in the Azure Pipeline YAML file.

# Push the code to GitHub to trigger the pipeline
After git push the code to GitHub, you will see the pipeline running.
You may need to permit the job manually.
* Successful deploy of the project in Azure Pipelines.  
* Running Azure App Service from Azure Pipelines automatic deployment
![alt text](./screenshot/deploy_success.png)

# Project running on Azure App Service
# Run the prediction test script to access the web service
modify the test script in make_predict_azure_app.sh, update the url to make sure the domain is correct.

* Monitor the app log
Open the cloud shell, run this command:
az webapp log tail --name songyang --resource-group Azuredevops

* Run this following command: (you can run this command in the cloud shell or in the local terminal, if your web app enable public access.)
chmod +x make_predict_azure_app.sh
./make_predict_azure_app.sh
![alt text](./screenshot/prediction.png)


* Output of streamed log files from deployed application
![alt text](./screenshot/app_log.png)


## Enhancements

<TODO: A short description of how to improve the project in the future>
1. **Advanced Monitoring** - Integrate Application Insights for detailed performance tracking
2. **Auto-scaling** - Implement VM scale sets for the prediction service during peak loads
3. **Model Versioning** - Add ML model registry instead of hardcoding the model file

## Demo 
<TODO: Add link Screencast on YouTube>
I cannot access YouTube from China. So I upload the video to screenrec.com.
It limit 5 minutes for unregistered users. I hope I have recode the key steps...

https://screenrec.com/share/1i5ApOx6uS


