import os

from pydantic import AnyUrl, BeforeValidator, PostgresDsn, SecretStr, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class Config:
    DB_NAME = "business"
    DB_USER = "postgres"
    DB_HOST = "localhost"
    DB_PASSWORD = "thepassword"
    DB_ADMIN_USER = "postgres"
    DB_ADMIN_PASSWORD = "thepassword"
    DB_PORT = 5432
    ENV = "dev"


class TestConfig(Config):
    DB_HOST = "localhost"


def load_config(testing: bool):
    # Ignore env vars if testing is passed
    if testing:
        return TestConfig

    env = os.getenv("ENV")

    if env == "dev":
        return Config
    elif env == "preprod":
        return TestConfig
    elif env == "prod":
        return Config
    raise RuntimeError("Unexpected value of environment variable `ENV`: ", env)


class Settings(BaseSettings):
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""
    PORT: int = 9090

    @computed_field
    @property
    def POSTGRESS_DATABASE_URL(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
