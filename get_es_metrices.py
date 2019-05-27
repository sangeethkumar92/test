import requests
import logging
from aws_requests_auth.aws_auth import AWSRequestsAuth

from base.config import config

logging.info('Connecting AWS ElasticSearch %s', config.ES_URI)
auth = AWSRequestsAuth(aws_access_key=config.AWS_ES_ACCESS_KEY,
                                  aws_secret_access_key=config.AWS_ES_SECRET_KEY,
                                  aws_host=config.ES_URI,
                                  aws_region=config.ES_REGION,
                                  aws_service='es')

def get_settings():
    url = "https://" + config.ES_URI + '/_cat/allocation?v'
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, auth=auth, headers=headers)
    print(response.status_code)
    print(response.headers)
    return response.content


print(get_settings())
