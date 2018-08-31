## Project Title

Stackoverflow-lite
## Travis Badge

## Coveralls Badge

## Code climate Maintainability Badge

## github repo link
https://github.com/johnkegz/StackOverflow-lite2

## Description
Stackoverflow-lite product enables user to.
*  create an account
*  singin
*  view questions
*  post a question
*  view number of answers
*  view number of questions
*  comment on an answer
*  up vote or down vote an answer
*  delete question posted by user
*  fetch all questions ever asked by the user
*  accept an answer

### Prerequisites

 #API
 * Postman
 * Virtual environment
 * pytest
 * pytest--cov
 * pylint
 * python
 * flask frame work
 * gunicorn
 * coveralls
 * coverage
 * vscode
 * postgres
 * JWT
### Installing

#API
* download and install vscode
* download and install python(3.6.6)
* download and virtual environment
* use pip to install flask in the terminal
* use pip to install pytest in the terminal
* use pip to install pytest--cov inthe terminal
* use pip to install pylint in the terminal
* use pip to install coverage in the terminal
* use pip to install coveralls
* install vscode
* Download and install postgres
## Deployment

The system is deployed on github which is integrated with TravisCl for continuous integration, then integrated with coverall.io to show the percentage of code that is tested, the integrated with code climate for maintainability and finally hosted on heroku in order for the user(Developer) to use.

## Built With

API
* python
* Flask framework
* JWT
### END POINTS                            METHOD   FUNCTION                              
* /api/v1/questions                     GET       Gets all the questions                 
* /api/v1/questions/<int:question_id>   GET       Gets one question                      
* /api/v1/questions                     POST      Posts one question                     
* /questions/<int:question_id>/answers  POST      Posts an answer to a specific question 
## Versioning

 * I use git hub for versioning.

## Authors

* **KALYANGO JOHN** -(https://github.com/johnkegz)

## Acknowledgments

* Thanks to Andela
