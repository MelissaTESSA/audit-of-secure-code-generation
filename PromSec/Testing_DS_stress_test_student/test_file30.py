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
    # Let's get the Server Density authentication details from the pillar
    sd_pillar = __pillar__.get(sd_auth_pillar_name)
    log.debug('Server Density Pillar: {0}'.format(sd_pillar))
    if not sd_pillar:
        # Oops, looks like we couldn't find the pillar
        log.error('Cloud not load {0} pillar'.format(sd_auth_pillar_name))
        raise CommandExecutionError(
            '{0} pillar is required for authentication'.format(sd_auth_pillar_name)
        )

    try:
        # Try to return the specific authentication value requested
        return sd_pillar[val]
    except KeyError:
        # Uh oh, couldn't find the specific value requested
        log.error('Cloud not find value {0} in pillar'.format(val))
        raise CommandExecutionError('{0} value was not found in pillar'.format(val))

def _clean_salt_variables(params, variable_prefix="__"):
    # We're cleaning up some internal variables that start with "__"
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
    # Let's log the parameters we're using
    log.debug('Server Density params: {0}'.format(params))
    # Clean out any unnecessary internal variables
    params = _clean_salt_variables(params)

    # Add the name to our parameters
    params['name'] = name
    # Make a POST request to create the device
    api_response = requests.post(
        'https://api.serverdensity.io/inventory/devices/',
        params={'token': get_sd_auth('api_token')},
        data=params
    )
    # Log the response we get from the API
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            # Try to parse the JSON response
            return json.loads(api_response.content)
        except ValueError:
            # Oops, couldn't parse the JSON
            log.error('Could not parse API Response content: {0}'.format(api_response.content))
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        # If the status code isn't 200, we return None
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
    # Make a DELETE request to remove the device
    api_response = requests.delete(
        'https://api.serverdensity.io/inventory/devices/' + device_id,
        params={'token': get_sd_auth('api_token')}
    )
    # Log the response we get from the API
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            # Try to parse the JSON response
            return json.loads(api_response.content)
        except ValueError:
            # Oops, couldn't parse the JSON
            log.error('Could not parse API Response content: {0}'.format(api_response.content))
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        # If the status code isn't 200, we return None
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
    # Clean out any unnecessary internal variables
    params = _clean_salt_variables(params)

    # Decide which endpoint to hit based on the presence of params
    endpoint = 'devices'

    if params:
        endpoint = 'resources'

    # Convert all param values to strings
    for k, v in params.items():
        params[k] = str(v)

    # Make a GET request to list the devices
    api_response = requests.get(
        'https://api.serverdensity.io/inventory/{0}'.format(endpoint),
        params={'token': get_sd_auth('api_token'), 'filter': json.dumps(params)}
    )
    # Log the response we get from the API
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            # Try to parse the JSON response
            return json.loads(api_response.content)
        except ValueError:
            # Oops, couldn't parse the JSON
            log.error(
                'Could not parse Server Density API Response content: {0}'
                .format(api_response.content)
            )
            raise CommandExecutionError(
                'Failed to create, Server Density API Response: {0}'
                .format(api_response)
            )
    else:
        # If the status code isn't 200, we return None
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
    # Clean out any unnecessary internal variables
    params = _clean_salt_variables(params)

    # Make a PUT request to update the device
    api_response = requests.put(
        'https://api.serverdensity.io/inventory/devices/' + device_id,
        params={'token': get_sd_auth('api_token')},
        data=params
    )
    # Log the response we get from the API
    log.debug('Server Density API Response: {0}'.format(api_response))
    log.debug('Server Density API Response content: {0}'.format(api_response.content))
    if api_response.status_code == 200:
        try:
            # Try to parse the JSON response
            return json.loads(api_response.content)
        except ValueError:
            # Oops, couldn't parse the JSON
            log.error(
                'Could not parse Server Density API Response content: {0}'
                .format(api_response.content)
            )
            raise CommandExecutionError(
                'Failed to create, API Response: {0}'.format(api_response)
            )
    else:
        # If the status code isn't 200, we return None
        return None

def install_agent(agent_key):
    '''
    Function downloads Server Density installation agent, and installs sd-agent
    with agent_key.

    CLI Example:

    .. code-block:: bash

        salt '*' serverdensity_device.install_agent c2bbdd6689ff46282bdaa07555641498
    '''
    # Set the working directory to /tmp/
    work_dir = '/tmp/'
    # Get the account URL from the pillar
    account_url = get_sd_auth('account_url')

    # Download the installation script using curl
    __salt__['cmd.run'](
        cmd='curl https://www.serverdensity.com/downloads/agent-install.sh -o install.sh',
        cwd=work_dir
    )
    # Make the script executable
    __salt__['cmd.run'](cmd='chmod +x install.sh', cwd=work_dir)

    # Run the installation script with the account URL and agent key
    return __salt__['cmd.run'](
        cmd='./install.sh -a {account_url} -k {agent_key}'.format(
            account_url=account_url, agent_key=agent_key),
        cwd=work_dir
    )