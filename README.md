# kidney-disease-detection-mlops

Kidney Disease Detection using CNN, MLflow, DVC, Docker, and AWS deployment.

## Workflows

1.Update config.yaml
2.Update secrets.yaml [Optional]
3.Update params.yaml
4.Update the entity
5.Update the configuration manager in src config
6.Update the components
7.Update the pipeline
8.Update the main.py
9.Update the dvc.yaml
10.app.py

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/Gavesh99324/kidney-disease-detection-mlops
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.9 -y
```

```bash
conda activate cnncls
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

### AWS-CICD-Deployment-with-Github-Actions

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws

#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
