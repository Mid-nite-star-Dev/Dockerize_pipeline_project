
# Dockerized pipeline project

## Project Overview

This project implements Extract, Transform, and Load (ETL) pipeline that extracts, processes, and stores data into a docker container to ensure its portability and reproducibility.
The pipeline is designed in two phases, phase I The extraction and transformation then phase II designing a pipeline automation to load inside a docker container.


## Requirements

- Python
- Docker
- Pandas
- Jupyter Notebook
- Gitbash
- Vscode

# Getting Started phase I

● For this phase I, use Jupyter Notebook
● Install pandas
● Import pandas as pd

# Getting Started phase II
To get started, you will need to have Docker installed. Once you have Docker installed then you can start building the project.

● Create a directory on Gitbash with the following naming convention: de4_{your_first_name}. For example: de4_collins

● Open vscode in that directory your current path (.) and create the following files: Dockerfile, Pipeline.py

● Copying all your codes from the notebook (phase I) and paste them in the pipeline.py file

● The Dockerfile should contain the following instructions:

○ Download the base image python

○ The WORKDIR as /app

○ Run the necessary installations based on your imports from your notebook

○ Apply a default command using CMD[“python”,”pipeline.py”] This will (Automate) the pipeline.py output  


# **Note**
Build the image with {your_name}:pipeline, example: docker build -t collins:pipeline .

Don’t forget to indicate your current path (.)

When the Docker image is being run, it should output all the answers in the following format:

My name is {Your name}, and here are my answers:

1. Country with the highest population: {answer}
2. Average GDP across all countries: {answer}
3. Country with the lowest unemployment rate: {answer}
4. Total population of the top 5 countries by GDP: {answer}
5. Number of countries with a GDP higher than 5 trillion: {answer}
6. Country with the lowest GDP per capita: {answer}


## Contribution and Feedback

Contributions are welcomed to enhance and extend this ETL pipeline further. Feel free to submit pull requests, raise issues, or provide feedback to help us improve the project.


