from unittest import TestCase
from unittest.mock import patch
import sample_api


class TestSample(TestCase):

    @patch('sample_api.Aaa')
    def test_aaa(self, mockAaa):
        mock_aaa = mockAaa.return_value
        print(mock_aaa)
        print(mock_aaa.xxx)
        self.assertEqual(mock_aaa.xxx, 'xxx')
