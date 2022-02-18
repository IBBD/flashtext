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

if __name__ == '__main__':
    unittest.main()

