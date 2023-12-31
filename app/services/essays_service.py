from functools import partial

from app.core.env import settings
from app.services.worker import worker
import app.dal.essays_dal as EssaysDAL
from concurrent.futures import ThreadPoolExecutor
from app.utils.logging_handler import LoggingHandler

class EssaysService(LoggingHandler):

    def __init__(self):
        super().__init__()
        self.__bank_of_words = EssaysDAL.get_bank_of_words()


    async def run(self) -> dict:
        """
            Read the engadget urls and the bank of words.
            split essays to bulks and each bulk send to Thread.
            each thread will request the urls, get the words and incriminate the words in the bank words dict

            Returns:
            Dict: Top 10 words most  count
        """
        try:

            essays_url_list = self.read_file()
            eassys_bulks = self.__create_essays_bulks(essays_url_list)

            with ThreadPoolExecutor(max_workers=settings.THREAD_COUNT) as pool:
                pool.map(partial(worker, self.__bank_of_words), eassys_bulks)

            sorted_list = sorted(self.__bank_of_words.items(), key=lambda x:x[1], reverse=True)
            top_ten_words = []

            if len(sorted_list) < 10:
                top_ten_words = sorted_list
            else:
                top_ten_words = sorted_list[:10]
            
            result_dict = {}
            for curr_tuple in top_ten_words:
                result_dict[curr_tuple[0]] = curr_tuple[1]

            return result_dict
        except Exception as error:
            self.log.error('Error in function MainService.run()', error)
            raise error


    def __create_essays_bulks(self, essays_url_list: list) -> list[list]:
        """
            Create essays bulks by number of essays/Thread count
            Return list of lists with urls

            Returns:
            list:[list]

        """
        self.log.info('Creating essays bulks...')

        essays_len = len(essays_url_list)
        if settings.THREAD_COUNT > essays_len:
            settings.THREAD_COUNT = essays_len
            
        bulk_size = int(essays_len/settings.THREAD_COUNT)
        self.log.info(f'each bulk size: {bulk_size}')

        bulk_size_sum = 0
        eassys_bulks = []

        while bulk_size_sum < essays_len:
            urls = essays_url_list[bulk_size_sum:bulk_size_sum+bulk_size]
            bulk_size_sum += bulk_size
            eassys_bulks.append(urls)

        self.log.info(f'Finished creating bulks, threre are {len(eassys_bulks)} bulks\n')
        return eassys_bulks


    def read_file(self) -> list:
        """
            Read engadget urls from file

            Returns:
            list:[string]

        """
        try:
            self.log.info(f'Reading engadget urls from file located: {settings.FILE_PATH}')
            
            with open(settings.FILE_PATH) as f:
                result = f.read()

            if result == '':
                return []
            
            results_list = result.split('\n')

            self.log.info(f'Finished reading file, there are {len(results_list)} essays\n')
            return results_list
        
        except Exception as error:
            self.log.error('Failed reading file', error)
            raise error