import pandas as pd
from logger import get_logger

logger = get_logger()

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting data transformation")

    try:
        # Normalize column names
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        # Drop rows with missing critical values
        df = df.dropna(subset=['customer_id', 'description'])
        # Remove cancelled invoices (case insensitive)
        df = df[~df['invoice'].astype(str).str.lower().str.startswith('c')]
        # Remove invalid quantities
        df = df[df['quantity'] > 0]
        # Remove invalid prices
        df = df[df['price'] > 0]
        # Avoid SettingWithCopyWarning
        df = df.copy()
        # Convert date column
        df['invoicedate'] = pd.to_datetime(df['invoicedate'])
        # Add feature
        df['total_price'] = df['quantity'] * df['price']

        logger.info("Data transformation completed successfully")
    except Exception as e:
        logger.error(f"Transformation error: {e}")
        raise

    return df
