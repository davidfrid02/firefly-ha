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

| variable              | type   | description                                                      | Example                                                               |
| --------------------- | ------ | -----------------------------------------------------------------| --------------------------------------------------------------------- |
| LOGGING_LEVEL         | string | Logging level of the app logs                                    | INFO                                                                  |
| ARTICLE_CLASS_NAME    | string | The class name in the html of engadget                           | .article-text                                                         |
| THREAD_COUNT          | int    | How much threads will run                                        | 50                                                                    |
| FILE_PATH             | string | File path for the engadget urls                                  | app/files/endg-urls                                                   |
| BANK_WORDS_URL        | string | Bank words file url                                              | https://raw.githubusercontent.com/dwyl/english-words/master/words.txt |
| RETRY_TIME_IN_SECONDS | int    | Retry time sleep between failed requests                         | 10                                                                    |
| MAX_RETRIES           | int    | Max retries of each url request                                  | 3                                                                     |
| REQUESTS_LIMIT        | int    | Max requests with the same proxy url                             | 200                                                                   |
| PROXY_LOOP_COUNT      | int    | After X proxy usage we can use again proxy from the begining     | 100                                                                   |