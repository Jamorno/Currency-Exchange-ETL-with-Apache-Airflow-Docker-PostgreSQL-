from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import logging
from etl.extracter import DataExtract
from etl.transformer import DataTransform
from etl.loader import DataLoad

logging.basicConfig(
    filename="country.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run_etl():
    extract = DataExtract("https://open.er-api.com/v6/latest/USD")
    raw_data = extract.extract_data()
    if raw_data is not None:
        transform = DataTransform()
        df = transform.transform_data(raw_data)

        if not df.empty:
            load = DataLoad()
            load.load_data_to_database(df)
        else:
            logging.warning("Dataframe is empty. Skipping to load step.")

    else:
        logging.warning("No data extracted.")

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="currency_etl_dag",
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
) as dag:
    run_etl_task = PythonOperator(
        task_id="run_etl_task",
        python_callable=run_etl
    )

    run_etl_task
    logging.info("ETL process completed.")
    logging.info("....................................................................................................")