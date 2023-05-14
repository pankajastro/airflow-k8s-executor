# Airflow-k8s-executor-playground

Run Airflow kubernetes executor on local machine and use airflow code from main with minimum setup.

# Prerequisite
- Docker desktop - Enable kubernetes
- Helm

# Clone Airflow code 

## Update templates
- ./templates
- values.yaml

## Create persistent volume and persistent volume claim

```bash
kubectl apply -f ./templates
```

## Install

```bash
helm upgrade --install -f values.yaml airflow ../airflow/chart
```

## Access console

```bash
docker run --rm -ti apache/airflow:2.6.0 bash
```

## port forwarding

```bash
kubectl port-forward svc/airflow-webserver 8080:8080
```
