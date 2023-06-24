# Firefly home assignment


## Description
The service fetch articales from engadget website, counts the words from all the essays combiend and returns the top 10 words.
 

## Prerequisites
In order to run this project.

- [Python](https://www.python.org/) - version 3.10.8
- [pip](https://pip.pypa.io/en/stable/)


## Local Development
Create virtual env:

```
python3 -m venv ./venv/ && source ./venv/bin/activate
```

Install dependencies:

```
pip3 install --upgrade pip && pip3 install -r requirements.txt
```

Press F5 to run a debug session

To destroy virtual env:

```
deactivate && rm -rf ./venv
```

## Tests
In order to run the tests, run in the console

```
python -m pytest -vv 
```

## ENV variables

You will have to provide the these variables:

| variable              | type   | description                              |
| --------------------- | ------ | ---------------------------------------- |
| LOGGING_LEVEL         | string | Logging level of the app logs            |
| ARTICLE_CLASS_NAME    | string | The class name in the html of engadget   |
| THREAD_COUNT          | int    | How much threads will run                |
| FILE_PATH             | string | File path for the engadget urls          |
| BANK_WORDS_URL        | string | Bank words file url                      |
| RETRY_TIME_IN_SECONDS | int    | Retry time between failed requests       |
| MAX_RETRIES           | int    | Max retries of each url request          |