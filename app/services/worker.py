import re
import logging

from bs4 import BeautifulSoup
from app.core.env import settings
import app.dal.essays_dal as EssaysDAL
import app.helpers.proxy_helper as ProxyHelper

proxy_cache = set()

def worker(bank_of_words: dict, urls: list):
    try:
        proxy_url = ProxyHelper.get_proxy_url()

        request_count = 0
        for url in urls:
            if request_count == settings.REQUESTS_LIMIT:
                proxy_url = ProxyHelper.get_proxy_url()
                request_count = 0

            request_count+=1
            response_text = EssaysDAL.fetch_url_data(url, proxy_url)
            essay_words = __parse_html_response_into_words(response_text)
            __count_essay_words(essay_words, bank_of_words)

    except Exception as error:
        logging.info(f'Error in function worker', error)
        raise error


def __parse_html_response_into_words(text: str) -> list:
    """
        Parse the html text main articale and extract only words with only alphabet characters

        Returns:
        list
    """
    try:
        logging.info(f'Parsing html to words...')

        if text == None:
            return []

        soup = BeautifulSoup(text, "html.parser")
        article_text_object = soup.select_one(settings.ARTICLE_CLASS_NAME)
        if article_text_object == None:
            return []
        
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