import os

class PathHandler:
    @classmethod
    def get_file_path(cls, file_name: str) -> str:
        return cls.__get_path(file_name)
    
    @classmethod
    def get_folder_path(cls, folder_name: str) -> str:
        return cls.__get_path(folder_name)
    
    @classmethod
    def __get_path(cls, name: str) -> str:
        return os.path.join(os.path.dirname(__file__), name);