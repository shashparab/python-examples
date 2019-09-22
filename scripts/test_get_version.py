from unittest import TestCase
from .lambda_versions import *

class TestGet_version(TestCase):

    result = get_version(["pricing-sandbox"])
    assert(result == )
    print(result)

    pass
