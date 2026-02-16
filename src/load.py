import pandas as pd
from logger import get_logger
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()
logger=get_logger()
def load_data(df:pd.DataFrame):
    logger.info("started data loading into mysql")

    try:
        con=mysql.connector.connect(

            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            port=3306
        )
        cursor=con.cursor()

        create_table_query="""
        create table if not exists sales_data(
            invoice varchar(255),
            stockcode varchar(255),
            description text,
            quantity int,
            invoicedate datetime,
            price float,
            customer_id int,
            country varchar(255),
            total_price float,
            PRIMARY KEY (invoice, stockcode)
        );
        """
        cursor.execute(create_table_query)

        insert_query="""
        insert ignore into sales_data(invoice,stockcode,description,quantity,invoicedate,price,customer_id,country,total_price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        cols=['invoice','stockcode','description','quantity','invoicedate','price','customer_id','country','total_price']


        data = [tuple(row) for row in df[cols].to_numpy()]

        batch_size = 5000  # safe size

        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            cursor.executemany(insert_query, batch)
            con.commit()  # commit each batch
            logger.info(f"Inserted {i+len(batch)} rows")

    except Exception as e:
        logger.error(f"error in loading data into mysql: {e}")
        raise 
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
        logger.info("MySQL connection closed")