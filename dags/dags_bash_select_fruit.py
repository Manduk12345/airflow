import datetime
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1_Orange = BashOperator(
        task_id="t1_Orange",
        bash_command="echo /opt/airflow/plugin/shell/select_fruit.ORANGE",
    )

    t2_avocado = BashOperator(
        task_id="t2_avocado",
        bash_command="echo echo /opt/airflow/plugin/shell/select_fruit.AVOCADO",
    )

    t1_Orange >> t2_avocado