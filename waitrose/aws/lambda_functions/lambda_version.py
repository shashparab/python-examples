import re
import logging
from waitrose.aws.lambda_functions.lambda_client import LambdaClient
from botocore.exceptions import ClientError


lambda_client = LambdaClient()
functions_list = lambda_client.list_lambdas('sandbox')
for func in functions_list:
    func_version = lambda_client.lambda_version(func)
    if func_version:
        print(func, func_version )
