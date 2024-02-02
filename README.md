Pytest BDD Selenium Framework
=============================

## Introduction

### Pytest

Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. Its features include parametrized testing, fixtures, and assert re-writing.

### Pytest BDD

Pytest-bdd is a pytest plugin that allows you to write behavior-driven development (BDD) style tests using the Gherkin syntax. Here are some key points and rules to keep in mind when using pytest-bdd: Gherkin Syntax: pytest-bdd uses the Gherkin syntax to define scenarios and steps

### Selenium

Selenium is an open-source automation tool that is used to automate web applications and perform various tests like parallel testing, cross-browser testing, end-to-end testing, etc. In this project, we used version Selenium 4, and it is integrated with W3C protocal to communicate web drivers to real browsers.

## Installation

1) Python
2) PyCharm CE IDE or Inteliji IDEA CE IDE or VS Code
3) Python Virtual Environment
4) Windows-Run Install Libraries.bat
5) Mac or Linux-Run Install Libraries.sh

## Python Virtual Environment

#### Create Python Virtual Environment
Step 1: Change project directory

Step 2: Open terminal

Step 3: Type Below commands
```bash
python3 -m venv venv
```

Step 4: Activate Virtual Environment

```bash
source venv/bin/activate
```
for Windows
```bash
source venv\Scripts\activate
```
Step 5: Deactivate Virtual Environment
```bash
deactivate
```

## Execution
### Execute Single Test
```bash
pytest ./tests/features/steps/test_login.py
```
### Execuute All Suite
```bash
pytest
```

### Run Suite With Different Environment
#### Default Environmment is QA
#### Run Suite On DEV Environmment
```bash
pytest --env "dev"
```
#### Run Suite On Stage Environmment
```bash
pytest --env "stage"
```
### Run Suite With Different Browser
#### Default Browser is Chrome
#### Run Suite On Edge Browser
```bash
pytest --browser "edge"
```
#### Run Suite On Edge Browser In Headless Mode
```bash
pytest --browser "edge" --headmode "headless"
```