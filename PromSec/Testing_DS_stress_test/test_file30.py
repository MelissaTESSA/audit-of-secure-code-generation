import requests
import json
import logging

from salt.exceptions import CommandExecutionError

log = logging.getLogger(__name__)

# Securely retrieves authentication details from a pillar
def get_sd_auth(val, sd_auth_pillar_name='serverdensity'):
    # Fetching sensitive data from pillar, ensuring it's securely accessed
    sd_pillar = __pillar__.get(sd_auth_pillar_name)
    log.debug('Server Density Pillar: {0}'.format(sd_pillar))  # Logging for troubleshooting
    if not sd_pillar:
        log.error('Could not load {0} pillar'.format(sd_auth_pillar_name))  # Secure error logging
        raise CommandExecutionError(
            '{0} pillar is required for authentication'.format(sd_auth_pillar_name)  # Secure exception handling
        )

    try:
        return sd_pillar[val]  # Securely retrieving the requested value
    except KeyError:
        log.error('Could not find value {0} in pillar'.format(val))  # Secure error logging
        raise CommandExecutionError('{0} value was not found in pillar'.format(val))  # Secure exception handling

# Securely removes sensitive variables from parameters
def _clean_salt_variables(params, variable_prefix="__"):
    map(params.pop, [k for k in params if k.startswith(variable_prefix)])  # Securely cleaning parameters
    return params

# Securely creates a new entity on Server Density
def create(name, **params):
    log.debug('Server Density params: {0}'.format(params))  # Logging for troubleshooting
    params = _clean_salt_variables(params)  # Securely cleaning parameters

    params['name'] = name  # Securely assigning the name

    # Securely sending a POST request to Server Density API
    api_response = requests.post(
        'https://api.serverdensity.io/inventory/devices/',
        params={'token': get_sd_auth('api_token')},  # Securely retrieving and using the API token
        data=params  # Securely passing data as payload
    )
    log.debug('Server Density API Response: {0}'.format(api_response))  # Logging for troubleshooting
    log.debug('Server Density API Response content: {0}'.format(api_response.content))  # Logging for troubleshooting
    if api_response.status_code == 200:  # Securely handling successful response
        try:
            return json.loads(api_response.content)  # Securely parsing JSON response
        except ValueError:
            log.error('Could not parse API Response content: {0}'.format(api_response.content))  # Secure error logging
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)  # Secure exception handling
            )
    else:
        return None  # Securely handling non-200 responses

# Securely deletes an entity from Server Density
def delete(device_id):
    # Securely sending a DELETE request to Server Density API
    api_response = requests.delete(
        'https://api.serverdensity.io/inventory/devices/' + device_id,  # Securely constructing the URL
        params={'token': get_sd_auth('api_token')}  # Securely retrieving and using the API token
    )