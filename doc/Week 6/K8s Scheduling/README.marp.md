---
marp: true
theme: default
paginate: true
title: "Kubernetes Scheduling"
---

# Kubernetes Scheduling

- Scheduler assigns Pods → Nodes
- Based on resources, constraints, policies
- Goal: utilization, performance, placement needs

---

## Scheduling Flow

![flow](01_scheduling_flow.png)

- Watch for unscheduled Pods
- **Filtering**: resources, ports, node labels, taints, affinity
- **Scoring**: free resources, balance, affinities, taints, plugins
- **Binding**: assign Pod to best node
- **Retries**: reattempt or leave pending

--- 
### Watch for Unsassigned Pods
   Scheduler watches the API server for Pods whose `spec.nodeName` is unset.

--- 

### Filtering (Predicates)

![02_filtering_predicates-Filtering__Predicates__Pipeline.png](02_filtering_predicates-Filtering__Predicates__Pipeline.png)

--- 

### Filtering Details
   Evaluate which nodes are feasible by checking:
    - **ResourceFits**: CPU, memory, and ephemeral-storage requests ≤ node allocatable.
    - **PodFitsPorts**: requested host ports not already in use.
    - **PodFitsNodeSelector**: node labels match Pod `nodeSelector`.
    - **PodFitsTaints**: node taints tolerated by Pod `tolerations`.
    - **PodFitsNodeAffinity**: matches affinity/anti-affinity rules.
    - **PodFitsInterPodAffinity**: respects `podAffinity` and `podAntiAffinity` rules.


---

### Scoring (Priorities)
![03_scoring_selection-Scoring_and_Node_Selection.png](03_scoring_selection-Scoring_and_Node_Selection.png)

---

### Scoring Details

   Score each feasible node to select the “best” one:
    - **LeastRequestedPriority**: prefers nodes with more free resources.
    - **BalancedResourceAllocation**: prefers balanced CPU/Mem usage.
    - **NodeAffinityPriority**: favors preferred node affinities.
    - **TaintTolerationPriority**: penalizes nodes with taints the Pod tolerates.
    - **Custom Plugin Scores** via scheduling framework.


--- 

### Binding

   Scheduler posts a `Binding` API call to assign the Pod to the chosen node.

### Retries & Evictions

   If binding fails or node becomes unschedulable, scheduler retries or leaves Pod pending.

---

## Key Concepts

- **Node Capacity vs Allocatable**
- **Requests vs Limits** → requests drive scheduling
- **Taints & Tolerations** → repel/allow Pods
- **Affinity / AntiAffinity** → co-locate or separate Pods
- **Topology Spread** → distribute across zones/nodes
- **Extenders & Plugins** → custom scheduling logic

---

## Configuration & Tuning

- **Profiles**: multiple scheduler configs per workload
- **Priorities**: PodPriority & Preemption for critical Pods
- **Quotas & LimitRanges**: namespace limits & defaults

---

## Debugging Scheduling

![06_debugging_scheduling-Debugging_Scheduling.png](06_debugging_scheduling-Debugging_Scheduling.png)

--- 

## Debugging Scheduling Details
 
- `kubectl describe pod` → scheduling events
- Scheduler logs (`journalctl -u kube-scheduler`)
- **Dry-run** → simulate scheduling decisions

---

## Best Practices

- Set **requests** carefully (avoid over/under)
- Use **affinity** sparingly
- Leverage **topology spread** across zones
- Monitor **pending Pods**
- Combine with **Cluster Autoscaler**

---

# Conclusion

Kubernetes scheduling:
- Matches Pods → Nodes efficiently
- Uses filters, scores, affinities, priorities
- Extensions enable customization
- Goal: **high availability + cluster efficiency**
