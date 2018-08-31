## Project Title

Stackoverflow-lite
## Travis Badge
[![Build Status](https://travis-ci.org/johnkegz/StackOverflow-lite.svg?branch=api)](https://travis-ci.org/johnkegz/StackOverflow-lite)
## Coveralls Badge
[![Coverage Status](https://coveralls.io/repos/github/johnkegz/StackOverflow-lite/badge.svg?branch=api)](https://coveralls.io/github/johnkegz/StackOverflow-lite?branch=api)
## Code climate Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/45d40c4afbecf21ca937/maintainability)](https://codeclimate.com/github/johnkegz/StackOverflow-lite/maintainability)

## gh-pages link
https://johnkegz.github.io/StackOverflow-lite/
## heroku app link
https://stackoverflow-lite-johnkegz.herokuapp.com/
## github repo link
https://github.com/johnkegz/StackOverflow-lite

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
 #Users Interface
 *  A browser installed which is uptodate
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
### Installing
#Users Interface
 * Download and install a browser
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
## Deployment

The system is deployed on github which is integrated with TravisCl for continuous integration, then integrated with coverall.io to show the percentage of code that is tested, the integrated with code climate for maintainability and finally hosted on heroku in order for the user(Developer) to use.

## Built With
User interface
* Visual studio code
* css, html and javascript
API
* python
* Flask framework
|END POINTS                           | METHOD  | FUNCTION                              |
|_____________________________________|_________|_______________________________________|
|/api/v1/questions                    |GET      |Gets all the questions                 |
|/api/v1/questions/<int:question_id>  |GET      |Gets one question                      |
|/api/v1/questions                    |POST     |Posts one question                     |
|/questions/<int:question_id>/answers |POST     |Posts an answer to a specific question |
## Versioning

 * I use git hub for versioning.

## Authors

* **KALYANGO JOHN** -(https://github.com/johnkegz)

## Acknowledgments

* Thanks to Andela
