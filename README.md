## Table of contents
1. [Description](#description)
2. [Services provided](#services-provided)
3. [Routes](#routes)
4. [Technologies](#technologies)
5. [Installation](#installation)
6. [Create author](#create-author)
7. [Author](#author)

## Description:
Health Check is a web application developed to provide varios services. The web application uses varios API to request data for multiple sites at the same time.

## Services provided
1. Data about different drugs that were approved by fda. this information includes Description, Precaustions, and instructions to use. 
2. Diagnosis services. one can select his/her symptoms from a provided list. The diagnosis for such symptoms is hence presented.
3. Articles. the site provides large range of Articles with medicine related topics, with the ability of adding Articles if the user has a role of an author. 

## routes
three different main routes include:  
1. '/medicines'  
    '/medicines/health-checker': url that detremines the symptoms
2. '/user'  
    '/user/login': to login a new user  
    '/user/reg': to register a new user
3. '/articles'
    '/articles/articles': for all articles
    '/articles/articles/id': for a specific article

## Technologies
A list of technologies used within the project:  
* Flask: Version 3.0.0
* Python: Version 3.8.10 
* REDIS: Version 5.0.7
* MYSQL: Version  8.0.35
* FLASKFORM, FLASKLOGIN
* HTML, CSS, JS, JQUERY

## Installation
$ Clone the repository: `git clone https://github.com/AhmedElSaeedTalat/health_check.git`  
$ Move to the app directory: `cd healthapp`  
$ Run the app: `python3 -m healthapp.runapp`

## Create author
**To create a new author run mycmd module:**
$ Run the cmd: `python3 -m mycmd`  
$ Use command: `create_author`   
$ A prompt will appear to add the username, email, and password  
* username:  
* email:  
* password:  
$ Use quit command to quiet `quit`  

## Author:
Ahmed Talat [Github](https://github.com/AhmedElSaeedTalat) | [twitter](https://twitter.com/AhmedElsaeed105)
