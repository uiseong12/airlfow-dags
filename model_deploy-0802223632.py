from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-0802223632",
}

dag = DAG(
    "model_deploy-0802223632",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_c2f94a4c_bd1e_4687_b3c0_6816ef2334d0 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop.ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="model_deploy-0802223632",
    cos_dependencies_archive="build_push_image-c2f94a4c-bd1e-4687-b3c0-6816ef2334d0.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image=" https://quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "dmltjd13521352",
        "CONTAINER_DETAILS": "you881123/mlflowdemo:lastet",
    },
    config_file="None",
    dag=dag,
)

notebook_op_c2f94a4c_bd1e_4687_b3c0_6816ef2334d0.image_pull_policy = "IfNotPresent"


notebook_op_2fdd1fe6_9e0d_4e1f_a917_b7790a69adc1 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop.ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="model_deploy-0802223632",
    cos_dependencies_archive="deploy_model-2fdd1fe6-9e0d-4e1f-a917-b7790a69adc1.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image=" https://quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAILS": "you881123/mlflowdemo:latest",
        "CLUSTER_DOMAIN_NAME": "192.168.219.170.nip.io",
    },
    config_file="None",
    dag=dag,
)

notebook_op_2fdd1fe6_9e0d_4e1f_a917_b7790a69adc1.image_pull_policy = "IfNotPresent"

(
    notebook_op_2fdd1fe6_9e0d_4e1f_a917_b7790a69adc1
    << notebook_op_c2f94a4c_bd1e_4687_b3c0_6816ef2334d0
)
