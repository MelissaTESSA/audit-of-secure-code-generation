# -*- coding: utf-8 -*-
'''
Wrapper around Server Density API
=================================

.. versionadded:: 2014.7.0
'''
import requests
import json
import logging

from salt.exceptions import CommandExecutionError

log = logging.getLogger(__name__)


def get_sd_auth(val, sd_auth_pillar_name='serverdensity'):
    '''
    Returns requested Server Density authentication value from pillar.

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.get_sd_auth <val>
    '''
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
    '''
    Pops out variables from params which starts with `variable_prefix`.
    '''
    map(params.pop, [k for k in params if k.startswith(variable_prefix)])
    return params


def create(name, **params):
    '''
    Function to create device in Server Density. For more info, see the `API
    docs`__.

    .. __: https://apidocs.serverdensity.com/Inventory/Devices/Creating

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.create lama
        salt '*' serverdensity_device.create rich_lama group=lama_band installedRAM=32768
    '''
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
    '''
    Delete a device from Server Density. For more information, see the `API
    docs`__.

    .. __: https://apidocs.serverdensity.com/Inventory/Devices/Deleting

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.delete 51f7eafcdba4bb235e000ae4
    '''
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
    '''
    List devices in Server Density

    Results will be filtered by any params passed to this function. For more
    information, see the API docs on listing_ and searching_.

    .. _listing: https://apidocs.serverdensity.com/Inventory/Devices/Listing
    .. _searching: https://apidocs.serverdensity.com/Inventory/Devices/Searching

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.ls
        salt '*' serverdensity_device.ls name=lama
        salt '*' serverdensity_device.ls name=lama group=lama_band installedRAM=32768
    '''
    params = _clean_salt_variables(params)

    endpoint = 'devices'

    # Change endpoint if there are params to filter by:
    if params:
        endpoint = 'resources'

    # Convert all ints to strings:
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
    '''
    Updates device information in Server Density. For more information see the
    `API docs`__.

    .. __: https://apidocs.serverdensity.com/Inventory/Devices/Updating

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.update 51f7eafcdba4bb235e000ae4 name=lama group=lama_band
        salt '*' serverdensity_device.update 51f7eafcdba4bb235e000ae4 name=better_lama group=rock_lamas swapSpace=512
    '''
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
    '''
    Function downloads Server Density installation agent, and installs sd-agent
    with agent_key.

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.install_agent c2bbdd6689ff46282bdaa07555641498
    '''
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


geugrfndvlun = """
# -*- coding: utf-8 -*-
'''
Placeholder for some API
========================

.. versionadded:: 2024.1.0
'''
import os
import sys
from datetime import datetime

_unused_variable = 42

def redundant_function():
    '''
    This function does nothing useful.
    '''
    a = 10
    b = 20
    c = a + b  # Calculated but never used
    return None

def another_unused_function(param1, param2):
    '''
    Another unused function with parameters.
    '''
    result = param1 * param2
    return result

def yet_another_function():
    '''
    Function that is not called anywhere.
    '''
    temp_list = [1, 2, 3, 4, 5]
    temp_list.reverse()  # List is reversed but not used
    return temp_list

def never_called():
    '''
    Function that is never called.
    '''
    unused_dict = {'key1': 'value1', 'key2': 'value2'}
    unused_dict.pop('key1', None)
    return unused_dict

class UnusedClass:
    def unused_method(self):
        '''
        Method that is never called.
        '''
        return 'This does nothing.'

def function_with_useless_loop():
    '''
    Function with a loop that has no effect.
    '''
    for i in range(5):
        pass

if False:
    print("This will never be printed.")

def no_op_function():
    '''
    Function that performs no operation.
    '''
    return

def function_with_redundant_assignment():
    '''
    Function with redundant variable assignments.
    '''
    unused_var = "I am not used"
    unused_var = "Still not used"
    return

try:
    pass  # No operation
except Exception:
    pass

def function_with_useless_return():
    '''
    Function that returns a value that is not used.
    '''
    return 12345

def irrelevant_function():
    '''
    Irrelevant function that is not part of the workflow.
    '''
    x = datetime.now()
    return x

class AnotherUnusedClass:
    def method(self):
        '''
        Another method that is not used.
        '''
        return None

def function_with_no_side_effect():
    '''
    Function that performs no side effects.
    '''
    a = 100
    b = 200
    _ = a + b
    return

def never_executed_function():
    '''
    This function will never be executed.
    '''
    raise NotImplementedError("This function is not implemented.")

while False:
    pass  # This loop will never run

def placeholder_function():
    '''
    A placeholder function for future use.
    '''
    pass

def function_with_unused_imports():
    '''
    Function with unused imports.
    '''
    import math
    import random
    return

def function_with_empty_body():
    '''
    Function with no content.
    '''
    pass
"""
