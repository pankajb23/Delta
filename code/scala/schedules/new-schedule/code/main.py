# Standard imports
import json

# Prophecy Imports
from config import Config
from config_loader import load_config
from fabrics import get_spark_job_configuration
from utils.helpers import *
from utils.gems import *

# Airflow imports
from airflow import DAG
from airflow.models import BaseOperator
from airflow.contrib.operators.databricks_operator import DatabricksSubmitRunOperator
from airflow.contrib.operators.emr_add_steps_operator import EmrAddStepsOperator
from airflow.contrib.sensors.emr_step_sensor import EmrStepSensor
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.sensors.s3_key_sensor import S3KeySensor
from airflow.providers.apache.livy.operators.livy import LivyOperator


def Email_0(config) -> BaseOperator:
    content = '''
    Delta
    '''

    return EmailOperator(
        mime_charset="utf-8",
        to="pankaj@simpledatalabs.com",
        subject="'Delta'",
        html_content=content,
        task_id="Email_0",
        trigger_rule="all_success"
    )

config = load_config()
with DAG(**config.dag_args) as dag:
    dag.configuration = config
    op_email_0 = Email_0(config)

    


