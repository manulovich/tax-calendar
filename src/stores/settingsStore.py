from .store import Store


class SettingsStore(Store):
    def __init__(self, path_to_config: str = '') -> None:
        super().__init__(path_to_config)
        self.path_to_config = path_to_config
        self.config = self._read_or_create(dict)

    def get_by_key(self, key: str, substitute=None):
        return self.config.get(key, substitute)

    def set_by_key(self, key: str, value) -> None:
        self.config[key] = value
        self._save(self.config)
