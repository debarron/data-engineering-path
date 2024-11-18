from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

# you can write in XCom by simply return
def _t1():
    return 42

# you can write using the task instance object
def _t2(task_instance):
    task_instance.xcom_push(key="task_2_xcom", value=200)

# to read xcom, use the task_instance object
def _t3(task_instance):
    xcom_val = task_instance.xcom_pull(key="task_2_xcom", task_ids="t2")
    print(f"Got the value {xcom_val}")

def _branch(task_instance):
    val = task_instance.xcom_pull(key="return_value", task_ids="t1")
    if val == 42:
        return "t2"
    return "t3"

with DAG(
    dag_id="xcom_dag",
    start_date=datetime(2022,1,1),
    schedule_interval="@daily",
    catchup=False
):

    t1 = PythonOperator(task_id="t1", python_callable=_t1)
    t2 = PythonOperator(task_id="t2", python_callable=_t2)
    t3 = PythonOperator(task_id="t3", python_callable=_t3)
    t4 = BashOperator(task_id="t4", bash_command="echo ''", trigger_rule='none_failed_min_one_success')

    branch = BranchPythonOperator(
        task_id="branch",
        python_callable=_branch
    )

    t1 >> branch >> [t2, t3] >> t4


