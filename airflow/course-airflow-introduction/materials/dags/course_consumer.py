from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="course_consumer",
    schedule=[my_file, my_file_2],
    start_date=datetime(2022,1,1),
    catchup=False
):
    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print("This is from dataset my_file: " + f.read() + "\n")

        with open(my_file_2.uri, "r") as f2:
            print("This is from dateset my_file_2: " + f2.read() + "\n")

    read_dataset()

