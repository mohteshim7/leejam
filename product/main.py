import os
import pdb

from dotenv import load_dotenv
import logging

load_dotenv()
FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("main")
logger.setLevel(level=logging.INFO)

import uvicorn
from logging import Logger
import asyncio
log = Logger("view:classification")


# Importing app here makes the syntax cleaner as it will be picked up by refactors
from app import app
import core.config



if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")),
                reload="dev")
