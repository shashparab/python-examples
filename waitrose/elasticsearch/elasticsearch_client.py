from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from ssl import create_default_context


class ESClient:

    def __init__(self, context:dict):
        self.client = Elasticsearch(
            [context['es_host']],
            http_auth=(context['es_user'], context['es_pass']),
            scheme='https' if 'es_scheme' not in context else context['es_scheme'],
            port='9243' if 'es_port' not in context else context['es_port']
        )

    def search(self, index):

        s = Search(using=self.client, index=index) \
            .filter("term", service_name="slot") \
            .filter("term", version="1.40.0") \
            .query("match", environment="dev") 

        response = s.execute()
        return response
