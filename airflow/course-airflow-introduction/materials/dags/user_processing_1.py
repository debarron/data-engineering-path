from airflow import DAG
from datetime import datetime

with DAG(
    dag_id="user_processing_1",
    schedule_interval="@daily",
    start_date=datetime(2023,1,1),
    catchup=False
) as dag:
    None
