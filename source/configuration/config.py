from os import getenv

from dotenv import load_dotenv

from source.exceptions import EnvNotFoundError


class Config:
    """Configuration class for storing environment variables."""

    def __init__(self) -> None:
        load_dotenv()
        self._stackoverflow_login = self._get_env_var_strict("STACKOVERFLOW_LOGIN")
        self._stackoverflow_password = self._get_env_var_strict("STACKOVERFLOW_PASSWORD")

    def _get_env_var_strict(self, env_name: str) -> str:
        env_value = getenv(key=env_name)
        if env_value is None:
            raise EnvNotFoundError(env_name)
        return env_value

    @property
    def stackoverflow_login(self) -> str:
        return self._stackoverflow_login

    @property
    def stackoverflow_password(self) -> str:
        return self._stackoverflow_password
