from sys import getsizeof
import time
import requests
from utils.configs import *


class Request:
    def __init__(self, url, base_url: str=None, body:dict = None, headers:dict = None, query_params:dict = None):
        self._url = url
        self._body = body
        self._headers = headers
        self._query_params = query_params
        self._base_url = base_url if base_url else get_config_value(section='Server', key='BaseURL')

    def set_base_url(self, base_url: str):
        self._base_url = base_url

    def get_base_url(self):
        return self._base_url

    def append_header(self, key: str, value: str):
        """
        Append a new header pair (key, value) to the headers
        :param key: A string represents the key header
        :param value: A string represents the value of the header
        :return: None
        """
        self._headers[key] = value

    def get_header_by_key(self, key: str):
        """
        Get a value from the header by its key
        :param key: A string represents the header key
        :return: A string represents the value corresponding to the key
        """
        return self._headers[key]

    def set_headers(self, headers):
        """
        Set a new headers for the request, don't use it until you want a new request configurations as this
        WILL DELETE THE OLD HEADERS
        :param headers: A dictionary represents the new headers
        :return: None
        """
        self._headers = headers

    def drop_header_by_key(self, key: str):
        """
        Drop a header from headers and return it
        :param key: A string represents the key corresponding to the header.
        :return: A dictionary represents the deleted header
        """
        return self._headers.pop(key)

    def get_headers(self):
        """
        Get all headers of the request
        :return: A dictionary represents the current header
        """
        return self._headers

    def set_url(self, url: str):
        self._url = url

    def get_url(self):
        return self._url

    def append_body(self, key: str, value: object):
        """
        Append a new (Key, Value) pair to the body
        :param key: A string represents the key of the new row
        :param value: An object that represents the value of the row (it can be any time even a nested dictionary)
        :return: none
        """
        self._body[key] = value

    def get_body_element_by_key(self, key: str):
        """
        Get a value from the body by its key
        :param key: A string represents the body key
        :return: A string represents the value corresponding to the key
        """
        return self._body[key]

    def set_body(self, body: dict):
        """
        Set a new body for the request, don't use it until you want a new request configurations as this
        WILL DELETE THE OLD BODY
        :param body: A dictionary represents the new headers
        :return: None
        """
        self._body = body

    def drop_body_element_by_key(self, key: str):
        """
        Drop a body element from body and return it
        :param key: A string represents the key corresponding to the body element.
        :return: A dictionary represents the deleted body element
        """
        return self._body.pop(key)

    def get_body(self):
        """
        Get body of the request
        :return: A dictionary represents the current body
        """
        return self._body

    def append_query_params(self, key: str, value: object):
        """
        Append a new (Key, Value) pair to the body
        :param key: A string represents the key of the new row
        :param value: An object that represents the value of the row (it can be any time even a nested dictionary)
        :return: none
        """
        self._body[key] = value

    def get_query_param_by_key(self, key: str):
        """
        Get a value from the query params by its key
        :param key: A string represents the query param key
        :return: A string represents the value corresponding to the key
        """
        return self._query_params[key]

    def set_query_params(self, query_params: dict):
        """
        Set a new query params for the request, don't use it until you want a new request configurations as this
        WILL DELETE THE OLD QUERY PARAMS
        :param query_params: A dictionary represents the new query params
        :return: None
        """
        self._query_params = query_params

    def drop_query_param_by_key(self, key: str):
        """
        Drop a  query params from query params and return it
        :param key: A string represents the key corresponding to the query param.
        :return: A dictionary represents the deleted query param
        """
        return self._query_params.pop(key)

    def get_query_params(self):
        """
        Get query parameter of the request
        :return: A dictionary represents the current query params
        """
        return self._query_params

    def send_post_request(self, is_json=True):
        start_time = time.time()
        response = requests.post(self._base_url + self._url, data=self._body,
                                 params=self._query_params, headers=self._headers)
        elapsed_time = time.time() - start_time
        #Need to be refactored
        if response.status_code == 200 or response.status_code == 201:
            return {
                'response_code': response.text if is_json else response.json(),
                'status_code': response.status_code,
                'response_size': getsizeof(response.text),
                'elapsed_time': elapsed_time
            }
        else:
            return {
                'response_content': response.text,
                'status_code': response.status_code,
                'elapsed_time': elapsed_time
            }

    def send_get_request(self, is_json=True):
        start_time = time.time()
        response = requests.get(self._base_url + self._url, params=self._query_params, headers=self._headers)
        elapsed_time = time.time() - start_time
        #Need to be refactored
        if response.status_code == 200:
            return {
                'response_code': response.text if is_json else response.json(),
                'status_code': response.status_code,
                'response_size': getsizeof(response.text),
                'elapsed_time': elapsed_time
            }
        else:
            return {
                'response_content': response.text,
                'status_code': response.status_code,
                'elapsed_time': elapsed_time
            }