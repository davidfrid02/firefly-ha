import time
import logging
import requests

from app.core.env import settings


def fetch_url_data(url: str, proxy: str) -> str:
    """
        Fetching url through proxy, 
        Get couple of retries if the request status_code == 999
        Returns:
        list
    """
    try:
        logging.info(f'Fetching url: {url} with proxy: {proxy}')
        count = 0
        while count < settings.MAX_RETRIES:

            response = requests.get(url, proxies={"http": proxy})

            if response.status_code == 200:
                return response.text

            if response.status_code == 404:
                logging.warning(f'Page not found (404)')
                return None
            
            if response.status_code == 999:
                logging.warning(f'Too many requests (999), sleep for {settings.RETRY_TIME_IN_SECONDS} seconds url: {url}')
                time.sleep(settings.RETRY_TIME_IN_SECONDS)
                count+=1

        logging.info(f'Fetched successfully\n')
    
    except Exception as error:
        logging.error(f'Error in function fetch_url_data', error)
        raise error


def get_bank_of_words() -> dict:
    """
        Get bank of words from url and filter words below 2 characters and not all alphabet

        Returns:
        dict:{
            word: 0,
            word2: 0,
            ..
        }

    """
    try:
        logging.info(f'Fetching and filter bank words from url: {settings.BANK_WORDS_URL}')

        response = requests.get(settings.BANK_WORDS_URL)
        if response.status_code != 200:
            logging.warning(f'Failed fetching with status code: {response.status_code}')
            return []
        
        bank_words = response.text.split('\n')
        words_dict = {}

        for word in bank_words:
            if len(word) > 2 and word.isalpha() and not word in words_dict:
                words_dict[word] = 0

        logging.info(f'Finished fetching and filtering bank words, there are {len(words_dict)} words\n')
        return words_dict
    
    except Exception as error:
        logging.error('Failed fetching bank words', error)
        raise error