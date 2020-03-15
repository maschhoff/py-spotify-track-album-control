from .parameter import prepare_params
from .request import execute_request

from .request_type import RequestType


def list_devices(auth, params=None):


    url_template = '{base_url}/{area}/{postfix}'
    url_params = {
        'query': prepare_params(params),
        'area': 'me',
        'postfix': 'player/devices',
        }

    payload = {
    }

    return execute_request(url_template,
                           auth,
                           url_params,
                           request_type=RequestType.GET,
                           payload=payload)
