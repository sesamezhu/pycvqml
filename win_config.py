import json
import os


def save_config(key, value):
    file_name = 'custom.json'
    with open(file_name, 'r') as f:
        config = json.load(f)
    config[key] = value
    with open(file_name, 'w') as f:
        json.dump(config, f, indent=4)


def read_config(key):
    file_name = 'custom.json'
    if not os.path.exists(file_name):
        config = {'version':1}
        with open(file_name, 'a') as f:
            json.dump(config, f, indent=4)
    with open(file_name, 'r') as f:
        config = json.load(f)
    return config.get(key, None)
