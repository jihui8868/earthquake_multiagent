from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    app_title: str = "Earthquake MultiAgent"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    debug: bool = False

    # CORS
    cors_origins: list[str] = ["*"]

    # OpenAI
    openai_api_key: str = "empty"
    openai_api_base: str = "https://http://127.0.0.1:1234/v1"
    openai_model: str = "qwen3-14b-claude-4.5-opus-high-reasoning-distill"
    openai_temperature: float = 0.7
    openai_max_tokens: int = 40960

    # Database
    database_url: str = "sqlite:///./earthquake.db"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
