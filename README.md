# Firefly-ha


## Description
This service fetch data for essays and count top 10 words from all essays combined
 

## Prerequisites
In order to run this project.

- [Python](https://www.python.org/)
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

To destroy virtual env:

```
deactivate && rm -rf ./venv
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