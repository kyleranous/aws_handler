"""
Wrapper for accessing Parameter Store values in Boto3
"""
import os
import boto3
import json
import logging

LOGGER = logging.getLogger(__name__)
LOG_LEVEL_SET = os.environ.get('LOG_LEVEL', 'INFO') or 'INFO'
LOG_LEVEL = logging.DEBUG if LOG_LEVEL_SET.lower() in ['debug'] else logging.INFO
LOGGER.setLevel(LOG_LEVEL)


def get_parameter(parameter_name: str) -> str:
    """
    Get a parameter from the parameter store
    """
    LOGGER.info(f'Getting Parameter: {parameter_name}')
    client = boto3.client('ssm')
    response = client.get_parameter(Name=parameter_name, WithDecryption=True)
    LOGGER.debug(f'Parameter: {parameter_name} Value: {response["Parameter"]["Value"]}')

    return response['Parameter']['Value']

def get_parameter_dict(parameter_name: str) -> dict:
    """
    Get Parameter from Parameter Store and Return as Dictionary
    """
    parameter = get_parameter(parameter_name)

    return json.loads(parameter)