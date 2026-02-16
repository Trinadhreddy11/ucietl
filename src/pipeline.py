from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data
from logger import get_logger
logger=get_logger()

def run_pipeline():
    try:
        logger.info("Etl pipeline started")
        df = extract_data("data/online retail.csv")
        logger.info(f"extracted {len(df)} rows")
        df=transform_data(df)
        logger.info(f"transformed data has {df.shape} rows")
        errors=validate_data(df)
        if errors:
            logger.error(f"data validation failed with errors: {errors}")
            return
        
        load_data(df)
        logger.info("etl pipeline completed successfully")
    except Exception as e:
        logger.error(f"etl pipeline failed with error: {e}")
        raise 
if __name__=="__main__":    
    run_pipeline()