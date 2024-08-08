from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str = "http://localhost:8000"

    DATABASE_URL: str = ""
    SECRET_KEY: str = "dfh3746alkvduy37eqpsdds19832lasdc91lsja03avnbkja"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_CALLBACK_URL: str = f"{HOST}/api/auth/google/callback"
    DISCORD_CLIENT_ID: str = ""
    DISCORD_CLIENT_SECRET: str = ""
    DISCORD_CALLBACK_URL: str = f"{HOST}/api/auth/discord/callback"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
