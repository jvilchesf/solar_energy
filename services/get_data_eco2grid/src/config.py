from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
    env_file="services/get_data/settings.env",
    env_file_encoding="utf-8",
    )

    api_key: str
    limit: int
    zone_code: str
    start: str
    end: str

settings = Settings()
