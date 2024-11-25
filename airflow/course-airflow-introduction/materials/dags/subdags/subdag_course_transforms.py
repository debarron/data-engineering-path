from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

def subdag_transforms(parent_dag_id, child_dag_id, args):
    with DAG(
        dag_id=f"{parent_dag_id}.{child_dag_id}",
        schedule_interval=args['schedule_interval'],
        start_date=args['start_date'],
        catchup=args['catchup']
    ) as dag:
        transform_a = BashOperator(
            task_id="transform_a",
            bash_command="sleep 10"
        )

        transform_b = BashOperator(
            task_id="transform_b",
            bash_command="sleep 10"
        )

        transform_c = BashOperator(
            task_id="transform_c",
            bash_command="sleep 10"
        )

    return dag

