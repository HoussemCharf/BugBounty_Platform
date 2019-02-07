# BugBounty Platform

BugBounty platform is platform made under the suporvision of Mr.Ahmed Chabchoub, Mr.Mostfa Hamza for the purpose of Isetcom security event.
the platform is bug reporting interface for contesters to report vunerabilities and proof of concept 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python3
Flask
Postgres
```

### Installing

Please follow these steps to successfully deploy the webapp in your local enviroment.


Step1: cloning the repository in your machine.

```
git clone https://github.com/HoussemCharf/BugBounty_Platform.git
```
Step2: start bin
```
source env/bin/activate
```
Step3: start posgresql service

```
service postgresql start
```


### Coding style

Please follow those coding style techniques for a better code readability  


Variable names:
```
UserCurrentName="Houssem"
```
Function name:
```
def encode_auth_token(self, user_id):
```
Comments:
```
def encode_auth_token(self, user_id):
"""
Generates the Auth Token
:return: string
"""

```


## Deployment

Notes
## Built With

* [Flask](http://flask.pocoo.org/) - Flask (A Python Microframework)



## Versioning

For the versions available, see the [tags on this repository](https://github.com/HoussemCharf/BugBounty_Platform/tags). 

## Authors

* **Houssem Charfeddine** - *BBP* - [HoussemCharf](https://github.com/HoussemCharf)



## Acknowledgments

Many thanks for the following people because they made this Happen:

* Mr.Ahmed Chabchoub
* Mr.Mostfa Hamza

