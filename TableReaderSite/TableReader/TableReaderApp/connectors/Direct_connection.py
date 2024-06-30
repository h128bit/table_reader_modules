import io
import base64
import toml
from .connector import Connector
import requests


class DirectConnector(Connector):

    def __init__(self):
        self._urls = toml.load('TableReaderApp/connectors/urls.toml')

    def get_table_struct(self,
                         file: bytes,
                         file_type: str):

        if file_type in ['png', 'jpeg', 'jpg']:
            url = self._urls['URL_GET_TABLE_STRUCT_IMG']
        elif file_type == 'pdf':
            url = self._urls['URL_GET_TABLE_STRUCT_PDF']
        else:
            raise Exception(f'Not supported data type: {file_type}. Possible types: pdf, png, jpeg, jpg')

        b64str = base64.b64encode(file)
        data = {'data': b64str}
        response = requests.post(url=url, data=data).json()

        return response['image']  # list of images in base 64

    def recognize(self,
                  list_of_files: list):
        table_list = []
        url = self._urls['URL_RECOGNIZE_TABLE']
        for file in list_of_files:
            b64str = base64.b64encode(file)
            data = {'data': b64str}
            response = requests.post(url=url, data=data).json()
            table_list.append(response)
        return table_list
