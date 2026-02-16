import logging
import os

def get_logger():
    os.makedirs('logs',exist_ok=True)
    logger=logging.getLogger("etl")
    if not logger.handlers:
        logging.basicConfig(
            filename="logs/pipeline.log",
            level=logging.INFO,
            format="%(asctime)s-%(levelname)s-%(message)s"
        )
        logger.setLevel(logging.INFO)
    return logger