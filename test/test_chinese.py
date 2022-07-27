from flashtext import KeywordProcessor
import logging
import unittest

logger = logging.getLogger(__name__)


class TestDictionaryLoad(unittest.TestCase):
    def setUp(self):
        logger.info("Starting...")

    def tearDown(self):
        logger.info("Ending.")

    def test_dictionary_loading(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword('测试')
        keywords_found = keyword_processor.extract_keywords('简单测试')
        self.assertEqual(keywords_found, ['测试'], "Failed 1")
        keywords_found = keyword_processor.extract_keywords('3测试')
        self.assertEqual(keywords_found, ['测试'], "Failed 2")
        keywords_found = keyword_processor.extract_keywords('ABC测试DFE')
        self.assertEqual(keywords_found, ['测试'], "Failed 3")

        keyword_processor.add_keyword('小鹏')
        keywords_found = keyword_processor.extract_keywords('小鹏P7')
        self.assertEqual(keywords_found, ['小鹏'], "Failed 4")

        keyword_processor.add_keyword('xiaopeng')
        keywords_found = keyword_processor.extract_keywords('xiaopengP7')
        self.assertEqual(keywords_found, ['xiaopeng'], "Failed 5")

        keyword_processor.add_keyword('ETF')
        keywords_found = keyword_processor.extract_keywords('000ETFABb')
        self.assertEqual(keywords_found, ['ETF'], "Failed 6")

        keyword_processor.add_keyword('ETF')
        keywords_found = keyword_processor.extract_keywords('000ETF111')
        self.assertEqual(keywords_found, ['ETF'], "Failed 7")

if __name__ == '__main__':
    unittest.main()

