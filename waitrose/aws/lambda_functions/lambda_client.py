import boto3
from botocore.exceptions import ClientError
import logging
import re


class LambdaClient:

    def __init__(self):
        self.client = boto3.client('lambda')

    def list_lambdas(self, source_env):
        """List of all lambdas deployed in particular environment.

        :return: List of lambdas deployed in current env, otherwise False
        """

        try:
            # Create a reusable Paginator
            paginator = self.client.get_paginator('list_functions')

            # Create a PageIterator from the Paginator
            page_iterator = paginator.paginate()

            my_function_list = []
            for page in page_iterator:
                my_function_list = my_function_list + [x['FunctionName'] for x in page['Functions']]
                my_function_list = [x for x in my_function_list if x.endswith('-' + source_env)]

        except ClientError as e:
            logging.debug(e)
            print(e)
            return False
        return my_function_list

    def lambda_version(self, lambda_function_name):
        """Get the version of deployed lambdas.

        :return: Dictionary of lambdas versions deployed in current env, otherwise False
        """

        try:
            functions = {}
            function_info = self.client.get_function(FunctionName=lambda_function_name)
            lambda_description = function_info['Configuration']['Description']
            lambda_ver = re.sub('[^0-9 . ]', '', lambda_description).rstrip('.')

        except ClientError as e:
            logging.debug(e)
            return False
        if lambda_ver:
            return lambda_ver
