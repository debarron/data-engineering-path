from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator

from datetime import datetime

from subdags.subdag_course_downloads import subdag_downloads
from subdags.subdag_course_transforms import subdag_transforms

with DAG(
    dag_id="group_dag",
    schedule_interval="@daily",
    start_date=datetime(2022,1,1),
    catchup=False
) as dag:

    args = {
        'start_date': dag.start_date,
        'schedule_interval': dag.schedule_interval,
        'catchup': dag.catchup
    }

    downloads = SubDagOperator(
        task_id="downloads",
        subdag=subdag_downloads(dag.dag_id, "downloads", args)
    )

    transforms = SubDagOperator(
        task_id="transforms",
        subdag=subdag_transforms(dag.dag_id, "transforms", args)
    )

    check_files = BashOperator(
        task_id="check_files",
        bash_command="sleep 10"
    )

    downloads >> check_files >> transforms

