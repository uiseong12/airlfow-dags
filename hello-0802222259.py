from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello-0802222259",
}

dag = DAG(
    "hello-0802222259",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_a96d5e28_2932_4612_bee3_aa0ba75023bf = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/hello.py",
    cos_endpoint="http://minio-ml-workshop.ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="hello-0802222259",
    cos_dependencies_archive="hello-a96d5e28-2932-4612-bee3-aa0ba75023bf.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image=" https://quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_a96d5e28_2932_4612_bee3_aa0ba75023bf.image_pull_policy = "IfNotPresent"


notebook_op_c256dfe2_251a_4325_b476_c532b38c8308 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/world.py",
    cos_endpoint="http://minio-ml-workshop.ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="hello-0802222259",
    cos_dependencies_archive="world-c256dfe2-251a-4325-b476-c532b38c8308.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image=" https://quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_c256dfe2_251a_4325_b476_c532b38c8308.image_pull_policy = "IfNotPresent"

(
    notebook_op_c256dfe2_251a_4325_b476_c532b38c8308
    << notebook_op_a96d5e28_2932_4612_bee3_aa0ba75023bf
)
