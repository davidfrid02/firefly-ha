import unittest
from unittest.mock import patch, Mock

from tests.mocks.load_mock_env import load_mock_env
import tests.mocks.essays_mocks as EssaysMocks
from app.services.essays_service import EssaysService

load_mock_env()

class TestEssaysService(unittest.IsolatedAsyncioTestCase):

    @classmethod
    @patch('app.dal.essays_dal.get_bank_of_words', Mock(return_value=EssaysMocks.WORD_BANK))
    def setUpClass(self):
        self.__essays_service = EssaysService()


    @classmethod
    def tearDownClass(self):
        self.__essays_service = None

    @patch('app.dal.essays_dal.fetch_url_data', Mock(side_effect=EssaysMocks.FETCHED_TEXT))
    @patch('app.helpers.proxy_helper.get_proxy_url', Mock(return_value=EssaysMocks.PROXY_URL))
    @patch('app.services.essays_service.EssaysService.read_file', Mock(return_value=EssaysMocks.ESSAYS_LIST))
    async def test_essays_service(self):
        top_ten_words = await self.__essays_service.run()

        self.assertEqual(top_ten_words['hello'], 3, "Error - hello count should be 3")
        self.assertEqual(top_ten_words['The'], 2, "Error - The count should be 2")
        self.assertEqual(top_ten_words['sunday'], 1, "Error - sunday count should be 1")
        self.assertFalse('phone' in top_ten_words, "Error - abcd should not be in top ten words")