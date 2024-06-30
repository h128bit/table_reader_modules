from abc import ABC, abstractmethod


class Connector(ABC):

    @abstractmethod
    def get_table_struct(self,
                         file: str,
                         file_type: str):
        pass

    @abstractmethod
    def recognize(self,
                  list_of_files: list):
        pass