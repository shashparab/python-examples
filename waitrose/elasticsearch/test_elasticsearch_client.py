
from unittest import TestCase
from waitrose.elasticsearch.elasticsearch_client import ESClient


class TestESClient(TestCase):

    def setUp(self):
        context = {
            "es_host": "3e834a5a0cea4bd28e641edf60804ee2.eu-west-1.aws.found.io",
            "es_user": "tpushpa",
            "es_pass": "jBn53jztf7hUrbhRn34e9R56dNgv8QBfaE7TMegv8d7Y2Mx52yAZYFK8WdzYAkUQ"
        }
        self.client = ESClient(context)

    def test_ping_elastic(self):
        self.assertEqual(self.client.__class__, ESClient)

    def test_search(self):
        result = self.client.search(index='app_version')
        print(result)
        print(result.hits.total)

