from .parameter import prepare_params
from .request import execute_request

from .request_type import RequestType


def playdev(dev_id, play, auth, params=None):


    url_template = '{base_url}/{area}/{postfix}'
    url_params = {
        'query': prepare_params(params),
        'area': 'me',
        'postfix': 'player',
        }

    payload = {
        'device_ids': [dev_id],
        'play': play
    }

    return execute_request(url_template,
                           auth,
                           url_params,
                           request_type=RequestType.PUT,
                           payload=payload)


def play(track_uri, auth, params=None):

    if track_uri is None or track_uri is '':
        raise AttributeError(
            'Parameter `track_uri` cannot be `None` or empty.')

    url_template = '{base_url}/{area}/{postfix}'
    url_params = {
        'query': prepare_params(params),
        'area': 'me',
        'postfix': 'player/play',
        }

    payload = {
        'uris': track_uri,
       # 'offset': {'uri': track_uri}
    }

    return execute_request(url_template,
                           auth,
                           url_params,
                           request_type=RequestType.PUT,
                           payload=payload)
