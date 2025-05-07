from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
    env_file="services/get_data_tp/settings.env",
    env_file_encoding="utf-8",
    )

    api_key: str
    base_url: str
    document_type: str
    process_type: str
    in_domain: str
    period_start: str


settings = Settings()
