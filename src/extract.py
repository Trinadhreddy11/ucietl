import pandas as pd
from logger import get_logger
import os

logger = get_logger()

def extract_data(path):
    logger.info("Reading dataset")

    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        raise FileNotFoundError(f"{path} not found")

    try:
        df = pd.read_csv(path, encoding="unicode_escape")

        if df.empty:
            logger.warning("Dataset is empty")

        logger.info("Dataset read successfully")

    except Exception as e:
        logger.error(f"Error reading dataset: {e}")
        raise

    return df
