from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "untitled-0803123234",
}

dag = DAG(
    "untitled-0803123234",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using untitled.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_23e2f8b8_5018_4cde_aa33_c9026f59335a = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="untitled-0803123234",
    cos_dependencies_archive="hello-23e2f8b8-5018-4cde-aa33-c9026f59335a.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_23e2f8b8_5018_4cde_aa33_c9026f59335a.image_pull_policy = "IfNotPresent"


notebook_op_f05b110f_0a15_4b08_8879_f3c68a4e4c6f = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="untitled-0803123234",
    cos_dependencies_archive="world-f05b110f-0a15-4b08-8879-f3c68a4e4c6f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_f05b110f_0a15_4b08_8879_f3c68a4e4c6f.image_pull_policy = "IfNotPresent"

(
    notebook_op_f05b110f_0a15_4b08_8879_f3c68a4e4c6f
    << notebook_op_23e2f8b8_5018_4cde_aa33_c9026f59335a
)
