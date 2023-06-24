import os

def load_mock_env():
    os.environ['FILE_PATH'] = ''
    os.environ['LOGGING_LEVEL'] = 'INFO'
    
    os.environ['ARTICLE_CLASS_NAME'] = '.article-text'
    os.environ['THREAD_COUNT'] = '1'
    
    os.environ['BANK_WORDS_URL'] = ''
    os.environ['RETRY_TIME_IN_SECONDS'] = '10'
    os.environ['MAX_RETRIES'] = '3'