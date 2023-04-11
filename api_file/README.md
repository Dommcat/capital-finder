## 401 Python 
## LAB - Class 16
## Project: Capital finder
## Author: Dominick Martin 
## About this Lab:
- Deploy a serverless function to the cloud.



## Feature Tasks and Requirements:
### This project involves creating a serverless function that interacts with the REST Countries API using the Python requests library. The function will handle two types of queries, as outlined below:


## Tasks:
- Sign up with Vercel and create a new project.

- Create a repository on GitHub and link it to your Vercel account.

- Use the requests library to interact with the REST Countries API.

- Create a serverless function that handles the following two types of queries:

- GET http request with a given country name that responds with a string with the form: "The capital of X is Y". For example, a request to /capital-finder?country=Chile should generate an http response of "The capital of Chile is Santiago."

- GET http request with a given capital that responds with a string with the form: "X is the capital of Y". For example, a request to /capital-finder?capital=Santiago should generate an http response of "Santiago is the capital of Chile."

- Follow the Vercel's get-started directions to deploy and test the serverless function.


## Working example urls for deployed function:



## Links and resources:
[Requests](https://requests.readthedocs.io/en/latest/)



## SETUP
```
python3 -m venv .venv
python3 .venv/bin/activate

pip Freeze >requirements.txt 

pip install pytest

``` 

## Tests:



## Link to code:
[capital_finder](/api_file/capital_finder.py)
