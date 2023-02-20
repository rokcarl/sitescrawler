import yaml

_config_path = "config.yml"

def get_config() -> dict:
    return yaml.safe_load(open(_config_path).read())