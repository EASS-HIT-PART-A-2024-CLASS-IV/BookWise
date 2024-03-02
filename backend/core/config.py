class Settings:
    API_V1_PATH = '/api/v1'

    PROJECT_NAME: str = "Bookwise"
    PROJECT_AUTHOR: str = "Chen Krichelly"
    PROJECT_VERSION: str = "1.0.0"


    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    TEST_USER_EMAIL = "test@example.com"


settings = Settings()