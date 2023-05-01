import os
import pdb
from pathlib import Path
from typing import Any, Optional, Union
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseSettings


class Config(BaseSettings):

    def __init__(self, _env_file: Union[Path, str, None], _env_file_encoding: Optional[str] = "",
                 _secrets_dir: Union[Path, str, None] = None, **values: Any) -> None:
        super().__init__(_env_file=_env_file, _env_file_encoding=_env_file_encoding,
                         _secrets_dir=_secrets_dir, **values)
        self.SessionLocal = None
        self.engine = None
        self.Base = None
        self.DATABASE_URL = os.getenv("POSTGRES_URL")

    # def get_connection_string(self):
    #     self.engine = create_engine(
    #         self.DATABASE_URL, connect_args={"check_same_thread": False}
    #     )
    #     self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    #
    #     self.Base = declarative_base()


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    return Config(".env")


# config = get_config()
DATABASE_URL = os.getenv("POSTGRES_URL")
pdb.set_trace()
engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
