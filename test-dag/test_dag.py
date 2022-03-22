import os
import sys
import os
from airflow.operators.bash_operator import BashOperator
import datetime
from airflow import models
from airflow.contrib.operators.dataflow_operator import DataflowTemplateOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from sql import testQuery
import json, requests, time

project_id = 'bi-kabum-prd-266512'
gce_zone = 'us-central1-a'
gce_region = 'us-central1'

default_args = {
    "start_date": days_ago(1),
    "retries": 0,
    "retry_delay": datetime.timedelta(seconds=60),
}

with models.DAG(
    'test-dag-pipeline',
    default_args=default_args,
    schedule_interval=None,
) as dag:
    mergeTask = BigQueryOperator(
        task_id = 'merge-task',
        sql=testQuery,
        use_legacy_sql=False,
        gcp_conn_id='google_cloud_default',
    )
mergeTask