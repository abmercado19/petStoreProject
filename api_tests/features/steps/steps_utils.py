from configparser import ConfigParser


categories_mapping = {'Dogs': 1}
tags_mapping = {'tag1': 1, 'tag2': 2}


def get_config():
    config = ConfigParser()
    config.read('api_tests/config/data.cfg')
    return config
