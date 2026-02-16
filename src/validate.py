from logger import get_logger

logger = get_logger()

def validate_data(df):
    errors = []

    if df['customer_id'].isnull().sum() > 0:
        errors.append("Customer ID has missing values.")

    if (df['quantity'] <= 0).any():
        errors.append("Quantity has invalid values (<=0).")

    if (df['price'] <= 0).any():
        errors.append("Invalid price values (<=0).")

    if errors:
        logger.warning(f"Validation issues found: {errors}")
    else:
        logger.info("Data validation passed")

    return errors
