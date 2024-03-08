from lambda_function import lambda_handler
import json
import unittest
from unittest.mock import Mock


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.event = Mock()
        self.context = Mock()

    def test_handler(self):
        handler = lambda_handler(event=self.event, context=self.context)
        assert handler == {'statusCode': 200, 'body': json.dumps('Hello from Lambda!')}


