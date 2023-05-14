from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dag2",
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=True,
) as dag:

    BashOperator(
        task_id="hello_world",
        bash_command="echo Hello World!",
    )
