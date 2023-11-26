## Project Title

Health Check

## Table of contents
1. [Description](#description)
2. [Services provided](#services-provided)
3. [Routes](#routes)
4. [Technologies](#technologies)

## Description:
Health Check is a web application developed to provide varios services. The web application uses varios API to request data for multiple sites at the same time.

## Services provided
1. Data about different drugs that were approved by fda. this information includes Description, Precaustions, and instructions to use. 
2. Diagnosis services. one can select his/her symptoms from a provided list. The diagnosis for such symptoms is hence presented.
3. Articles. the site provides large range of Articles with medicine related topics, with the ability of adding Articles if the user has a role of an authro. 

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
