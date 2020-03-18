<div align="center">
    <img height="200" src="assets/pypassgen-logo.svg" />
    <h1>pyPassGen</h1>
    <p>Python Password Generator</p>
</div>

## Description

pyPassGen is a password generator application built on Python and uses PyQt5. Passwords are created by using random mixes of lowercase, uppercase, special characters, and numbers to create a unique password. The lenght of the password can be specified by the user although a lenght of at least 10 characters is recommended.

Passwords are *currently* stored in a JSON file created and stored only on your local machine.

## In Development

This app is still in active developement and is currently in early stages. If you have suggestions for features and/or would like to contribute please feel free to fork and create a pull request.

## Running pyPassGen

You will need Python and PyQt5 installed on your machine to run this app.

You can install Python [here](https://www.python.org/downloads/)

Installing PyQt5
`pip install PyQt5`

> Mac & Linux users may need to use pip3 instead

You can read more on PyQt5 [here](https://pypi.org/project/PyQt5/)

To run the app simply navigate to the root project directory and type the following command into a CLI:

`pip passgen.py` or `pip3 passgen.py`
