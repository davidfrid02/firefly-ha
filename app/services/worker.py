import re
import time
import logging
import requests

from fp.fp import FreeProxy
from bs4 import BeautifulSoup
from app.core.env import settings

proxy_cache = set()

def worker(bank_of_words: dict, urls: list):
    try:
        proxy = __get_proxy_url()

        for url in urls:
            response_text = __fetch_url_data(url, proxy)
            essay_words = __parse_html_response_into_words(response_text)
            __count_essay_words(essay_words, bank_of_words)

    except Exception as error:
        logging.info(f'Error in function worker', error)
        raise error


def __fetch_url_data(url: str, proxy: str) -> str:
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
                break

            if response.status_code == 404:
                logging.warning(f'Page not found (404)')
                break
            
            if response.status_code == 999:
                logging.warning(f'Too many requests (999), sleep for {settings.RETRY_TIME_IN_SECONDS} seconds url: {url}')
                time.sleep(settings.RETRY_TIME_IN_SECONDS)
                count+=1

        logging.info(f'Fetched successfully\n')
        return response.text
    
    except Exception as error:
        logging.error(f'Error in function __fetch_url_data', error)
        raise error


def __parse_html_response_into_words(text: str) -> list:
    """
        Parse the html text main articale and extract only words with only alphabet characters

        Returns:
        list
    """
    try:
        logging.info(f'Parsing html to words...')

        soup = BeautifulSoup(text, "html.parser")
        article_text_object = soup.select_one(settings.ARTICLE_CLASS_NAME)
        if article_text_object == '':
            return
        
        words_list = re.findall(r'\w+', article_text_object.text)

        logging.info(f'Finished parsing html\n')
        return words_list
    
    except Exception as error:
        logging.error(f'Error in function __parse_html_response_into_words', error)
        raise error


def __count_essay_words(essay_words: list, bank_of_words: dict):
    """
        For each word in the list,
        check if the word exists in the bank and increment by one if exists.

        Returns:
        None
    """
    for word in essay_words:
        if word in bank_of_words:
            bank_of_words[word] += 1


def __get_proxy_url() -> str:
    """
        Fetching proxy from FreeProxy, and manage a proxy cache
        keep fetching until a new proxy.

        Returns:
        str
    """
    try:
        logging.info(f'Fetching proxy...')

        new_proxy = False
        while (not new_proxy):
            proxy = FreeProxy(country_id=['US'], https=False, rand=True).get()
            if not proxy in proxy_cache:
                new_proxy = True
                proxy_cache.add(proxy)

        logging.info(f'Fetched proxy: {proxy}\n')
        return proxy
    
    except Exception as error:
        logging.error(f'Error in function __get_proxy_url', error)
        raise error