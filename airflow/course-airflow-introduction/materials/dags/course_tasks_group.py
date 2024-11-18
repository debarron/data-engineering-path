from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

from groups.group_course_downloads import download_tasks
from groups.group_course_transforms import transforms_tasks

with DAG(
    dag_id="taks_group_dag",
    schedule_interval="@daily",
    start_date=datetime(2022,1,1),
    catchup=False
) as dag:


    downloads = download_tasks()
    transforms = transforms_tasks()

    check_files = BashOperator(
        task_id="check_files",
        bash_command="sleep 10"
    )

    downloads >> check_files >> transforms

