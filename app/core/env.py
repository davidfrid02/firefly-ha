from pydantic import BaseSettings

class Settings(BaseSettings):
    LOGGING_LEVEL: str
    FILE_PATH: str
    ARTICLE_CLASS_NAME: str
    THREAD_COUNT:int
    BANK_WORDS_URL: str
    RETRY_TIME_IN_SECONDS: int
    MAX_RETRIES: int

    class Config:
        env_file = '.env'

settings = Settings()