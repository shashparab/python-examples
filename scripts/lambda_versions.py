import re
import logging
import boto3
from botocore.exceptions import ClientError

input_source_env = 'dev'
# Create a client
client = boto3.client('lambda')


def list_lambdas(source_env):
    """List of all lambdas deployed in particular environment.

    :return: List of lambdas deployed in current env, otherwise False
    """

    try:
        # Create a reusable Paginator
        paginator = client.get_paginator('list_functions')

        # Create a PageIterator from the Paginator
        page_iterator = paginator.paginate()

        my_function_list = []
        for page in page_iterator:
            my_function_list = my_function_list + [x['FunctionName'] for x in page['Functions']]
            my_function_list = [x for x in my_function_list if x.endswith('-' + source_env)]

    except ClientError as e:
        logging.debug(e)
        return False
    #print(len(my_function_list))
    return my_function_list


def get_version(my_function_list):
    """Get the version of all deployed lambdas.

    :return: Dictionary of lambdas versions deployed in current env, otherwise False
    """

    try:
        functions = {}
        for function in my_function_list:
            function_info = client.get_function(FunctionName=function)
            lambda_version = function_info['Configuration']['Description']
            lambda_version = re.sub('[^0-9 . ]', '', lambda_version).rstrip('.')
            if lambda_version:
                functions[function] = lambda_version

    except ClientError as e:
        logging.debug(e)
        return False
    for key,value in functions.items():
        print(key,value)
    return functions


def main():
    """Exercise get_version()"""

    # Set up logging
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Get the lambda version info.

    if get_version(list_lambdas(input_source_env)):
        logging.info('Retrieved lambda version.')
    else:
        logging.info('Could not retrieve lambda list.')


if __name__ == '__main__':
    main()
