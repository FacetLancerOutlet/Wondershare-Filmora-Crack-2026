import os
import json
import hashlib
import requests

class FileUtility:
    def __init__(self, directory):
        self.directory = directory

    def list_files(self):
        return os.listdir(self.directory)

    def calculate_md5(self, filename):
        hash_md5 = hashlib.md5()
        with open(os.path.join(self.directory, filename), 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

class DataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self, key, value):
        return [item for item in self.data if item.get(key) == value]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f)

if __name__ == '__main__':
    directory = 'files'
    url = 'https://api.example.com/data'
    file_util = FileUtility(directory)
    files = file_util.list_files()
    for file in files:
        print(f'{file}: {file_util.calculate_md5(file)}')
    data_fetcher = DataFetcher(url)
    data = data_fetcher.fetch_data()
    processor = DataProcessor(data)
    filtered_data = processor.filter_data('status', 'active')
    processor.save_to_file('output.json')
