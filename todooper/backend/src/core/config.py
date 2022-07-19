from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Todooper"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_SERVER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


settings = Settings()
