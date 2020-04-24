class Config:
    TEST_VALUE = "CONFIG_VALUE"
    PG_USER = "test_cursor"
    PG_PASSWORD = "test"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "test_orm_cursor"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
