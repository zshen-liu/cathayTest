import logging
import yaml


class ConfigManager:
    _env = None

    def __init__(self, env: str):
        self.env = env

        logging.info(f'ConfigManager Test ENV {self.env}')

        if self.env == 'cathayRel':
            ConfigManager._env = self.cathayRel()
        else:
            raise TypeError(f'Environment: {self.env} is not supported!')

    @staticmethod
    def get_current_config():
        return ConfigManager._env

    def cathayRel(self):
        return ConfigCathRel()


class Config:
    _config_yaml = None

    @property
    def url(self):
        return self._config_yaml['url']

    @property
    def env(self):
        return self._config_yaml['env']


class ConfigCathRel(Config):
    def __init__(self):
        with open('config/rel.yaml') as f:
            self._config_yaml = yaml.load(f, Loader=yaml.FullLoader)
