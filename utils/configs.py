import configparser


def get_config_value(section, key, file_name: str=''):
    config = configparser.ConfigParser()
    config.read('../env.ini' if file_name == '' else file_name)
    return config[section][key]