---
marp: true
theme: default
paginate: true
---

# Kubernetes Scaling

- Kubernetes provides mechanisms to **scale workloads and cluster capacity**
- Ensures applications handle variable load while optimizing resource usage

---

## Pod Autoscaling

### Horizontal Pod Autoscaler (HPA)

- Adjusts number of Pod replicas in a Deployment/ReplicaSet/StatefulSet.
- **Metrics supported**:
    - CPU utilization (built-in)
    - Memory utilization (v1.16+)
    - Custom metrics (via Metrics API: request rate, queue length)
    - External metrics (cloud provider metrics)

---

## HPA Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: frontend-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: frontend
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 60
```

---

## Vertical Pod Autoscaler (VPA)

- **What it does**  
  Recommends or automatically adjusts CPU/memory requests and limits.

- **Modes**
    - Off (recommendation only)
    - Auto: evicts & recreates Pods with new resources
    - Initial: sets resources only on first creation

- **Use cases**
    - Stateful workloads
    - Reducing overprovisioning

---

## Cluster Autoscaling

### Cluster Autoscaler (CA)

- Adjusts number of **nodes** in the cluster.
- **Behavior**:
    - Scale up: when Pods cannot be scheduled.
    - Scale down: when nodes are underutilized.
- **Integration**:
    - Cloud provider autoscalers (AWS ASG, GKE, AKS VMSS).
    - Custom solutions for on-prem clusters.

---

## Manual & Scheduled Scaling

### Manual
```bash
kubectl scale deployment backend --replicas=5
```

### Scheduled (CronJob)
```yaml
apiVersion: batch/v1beta1
kind: CronJob
spec:
  schedule: "0 8 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: scaler
            image: bitnami/kubectl
            command:
            - kubectl
            - scale
            - deployment/frontend
            - --replicas=10
          restartPolicy: Never
```

---

## Best Practices

1. Set sensible min/max replicas.
2. Use multiple metrics (CPU, memory, custom).
3. Avoid rapid fluctuations with stabilization windows.
4. Consider startup time for Pods.
5. Use PodDisruptionBudgets (PDBs) for availability.
6. Monitor scaling events with Prometheus/Grafana.

---

# Summary


- Kubernetes supports **automatic scaling** at both Pod and cluster levels.

- By combining **HPA, VPA, and Cluster Autoscaler** with manual and scheduled controls, you can build **responsive,
  cost-efficient clusters** that adapt to workload demands.