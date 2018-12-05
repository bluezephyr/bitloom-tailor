import json

class ConfigParser(object):

    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.values = json.load(f)

