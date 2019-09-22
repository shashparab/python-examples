from unittest import TestCase
# from moto import mock_lambda
from waitrose.aws.lambda_functions.lambda_client import LambdaClient


class TestLambdaClient(TestCase):
    def setUp(self):
        pass

    # @mock_lambda
    def test_list_lambdas(self):
        client = LambdaClient()
        results = client.list_lambdas("sandbox")
        print(results)
