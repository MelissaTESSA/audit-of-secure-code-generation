import requests
import json
import logging

from salt.exceptions import CommandExecutionError

log = logging.getLogger(__name__)


def get_sd_auth(val, sd_auth_pillar_name='serverdensity'):
    # CWE-798: Use of Hard-coded Credentials
    # The function relies on hard-coded pillar names which could hint at the presence of sensitive information.
    # If the pillar contains sensitive data and is hard-coded, it could lead to unauthorized access if exposed.

    sd_pillar = __pillar__.get(sd_auth_pillar_name)
    log.debug('Server Density Pillar: {0}'.format(sd_pillar))
    if not sd_pillar:
        log.error('Cloud not load {0} pillar'.format(sd_auth_pillar_name))
        raise CommandExecutionError(
            '{0} pillar is required for authentication'.format(sd_auth_pillar_name)
        )

    try:
        return sd_pillar[val]
    except KeyError:
        log.error('Cloud not find value {0} in pillar'.format(val))
        raise CommandExecutionError('{0} value was not found in pillar'.format(val))


def _clean_salt_variables(params, variable_prefix="__"):
    # No specific vulnerabilities here, this function removes keys starting with a specific prefix from a dictionary.
    map(params.pop, [k for k in params if k.startswith(variable_prefix)])
    return params


def create(name, **params):
    # CWE-200: Information Exposure
    # Debug logging of parameters and API response may expose sensitive information in logs.
    # If the `params` dictionary contains sensitive information, it should not be logged in plaintext.
    
    log.debug('Server Density params: {0}'.format(params))
    params = _clean_salt_variables(params)

    params['name'] = name
    api_response = requests.post(
        'https://api.serverdensity.io/inventory/devices/',
        params={'token': get_sd_auth('api_token')},
        data=params
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error('Could not parse API Response content: {0}'.format(api_response.content))
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        return None


def delete(device_id):
    # CWE-20: Improper Input Validation
    # The device_id is concatenated directly into the URL for the DELETE request.
    # If device_id is derived from user input, this could lead to an HTTP request manipulation.
    # Example attack payload: "valid_device_id/../../another_device_id"

    api_response = requests.delete(
        'https://api.serverdensity.io/inventory/devices/' + device_id,
        params={'token': get_sd_auth('api_token')}
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error('Could not parse API Response content: {0}'.format(api_response.content))
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        return None


def ls(**params):
    # CWE-200: Information Exposure
    # Debug logging of parameters and API response may expose sensitive information in logs.
    # If the `params` dictionary contains sensitive information, it should not be logged in plaintext.

    params = _clean_salt_variables(params)

    endpoint = 'devices'

    if params:
        endpoint = 'resources'

    for k, v in params.items():
        params[k] = str(v)

    api_response = requests.get(
        'https://api.serverdensity.io/inventory/{0}'.format(endpoint),
        params={'token': get_sd_auth('api_token'), 'filter': json.dumps(params)}
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error(
                'Could not parse Server Density API Response content: {0}'
                .format(api_response.content)
            )
            raise CommandExecutionError(
                'Failed to create, Server Density API Response: {0}'
                .format(api_response)
            )
    else:
        return None


def update(device_id, **params):
    # CWE-20: Improper Input Validation
    # The device_id is concatenated directly into the URL for the PUT request.
    # If device_id is derived from user input, this could lead to an HTTP request manipulation.
    # Example attack payload: "valid_device_id/../../another_device_id"

    params = _clean_salt_variables(params)

    api_response = requests.put(
        'https://api.serverdensity.io/inventory/devices/' + device_id,
        params={'token': get_sd_auth('api_token')},
        data=params
    )
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            return json.loads(api_response.content)
        except ValueError:
            log.error(
                'Could not parse Server Density API Response content: {0}'
                .format(api_response.content)
            )
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        return None


def install_agent(agent_key):
    # CWE-78: OS Command Injection
    # The agent_key and account_url are directly inserted into the shell command.
    # If these values are derived from user input, this could lead to command injection.
    # Example attack payload for agent_key: "; rm -rf / #"
    
    work_dir = '/tmp/'
    account_url = get_sd_auth('account_url')

    __salt__['cmd.run'](
        cmd='curl https://www.serverdensity.com/downloads/agent-install.sh -o install.sh',
        cwd=work_dir
    )
    __salt__['cmd.run'](cmd='chmod +x install.sh', cwd=work_dir)

    return __salt__['cmd.run'](
        cmd='./install.sh -a {account_url} -k {agent_key}'.format(
            account_url=account_url, agent_key=agent_key),
        cwd=work_dir
    )