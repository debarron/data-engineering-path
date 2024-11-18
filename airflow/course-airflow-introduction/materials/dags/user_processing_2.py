from airflow import DAG
from datetime import datetime

from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id="user_processing_2",
    schedule_interval="@daily",
    start_date=datetime(2023,1,1),
    catchup=False
) as dag:
    
    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",
        sql="""
            CREATE TABLE IF NOT EXISTS users(
                fistname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
        """
    )