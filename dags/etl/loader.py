import psycopg2, logging, os

class DataLoad:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

    def load_data_to_database(self, df):
        try:
            cursor = self.conn.cursor()

            cursor.execute("""DROP TABLE IF EXISTS currency_etl""")

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS currency_etl 
                (updated TEXT, base_currency TEXT, target_currency TEXT, exchange_rate FLOAT)"""
            )

            for _, row in df.iterrows():
                cursor.execute(
                    """INSERT INTO currency_etl (updated, base_currency, target_currency, exchange_rate) 
                    VALUES (%s, %s, %s, %s)""", (
                        row["updated"],
                        row["base_currency"],
                        row["target_currency"],
                        row["exchange_rate"]
                    )
                )

            self.conn.commit()
            logging.info("Loaded data into PostgresSQL successfully.")

        except Exception as e:
            logging.error("DEBUG: Failed to load data to PostgresSQL")

        finally:
            cursor.close()
            self.conn.close()