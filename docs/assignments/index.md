# Course Assignments

This page provides an overview of all course assignments for CS 5287 Cloud Computing.

## Assignment Progression

The assignments follow a logical progression through cloud computing modalities:

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA0</span>
        <h3>Manual Deployment</h3>
    </div>
    <p>Build and verify the full IoT pipeline "by hand" on cloud VMs. Learn each component end-to-end.</p>
    <p><strong>Due:</strong> September 5, 2025</p>
    <p><a href="ca0/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA1</span>
        <h3>Infrastructure as Code</h3>
    </div>
    <p>Recreate CA0 using automation tools like Ansible and Terraform.</p>
    <p><strong>Due:</strong> September 19, 2025</p>
    <p><a href="ca1/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA2</span>
        <h3>PaaS Orchestration</h3>
    </div>
    <p>Run the pipeline on Kubernetes or Docker Swarm using declarative manifests.</p>
    <p><strong>Due:</strong> October 17, 2025</p>
    <p><a href="ca2/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA3</span>
        <h3>Cloud-Native Ops</h3>
    </div>
    <p>Add observability, autoscaling, security hardening, and resilience testing.</p>
    <p><strong>Due:</strong> November 7, 2025</p>
    <p><a href="ca3/">→ View Details</a></p>
</div>

<div class="assignment">
    <div class="assignment-header">
        <span class="assignment-number">CA4</span>
        <h3>Multi-Hybrid Cloud (Final)</h3>
    </div>
    <p>Distribute components across sites/clouds with secure connectivity and failover.</p>
    <p><strong>Due:</strong> December 5, 2025</p>
    <p><a href="ca4/">→ View Details</a></p>
</div>

## Grading Rubric

All assignments are evaluated on:

| Category | Weight | Description |
|----------|--------|-------------|
| Correctness & Completeness | 15% | All components working end-to-end |
| Cloud-Model Execution | 25% | Proper use of cloud modality |
| Security | 15% | Security controls and best practices |
| Automation & Reproducibility | 10% | Clear, repeatable processes |
| Documentation & Diagrams | 30% | Comprehensive documentation |
| Demo Quality | 5% | Clear demonstration of working system |

## Reference Stack

Students should maintain the same logical architecture throughout all assignments:

- **Producers** → **Kafka Pub/Sub Hub** → **Processor** → **DB/Analytics**

Example components:
- **Kafka**: `bitnami/kafka:3.5.0`
- **Database**: `mongo:6.0.4` or `couchdb`
- **Processor**: Custom inference/transform service
- **Producers**: Data simulator containers

## Submission Requirements

Each assignment must be submitted to your GitHub repository:

```
github.com/your-username/CS5287/
├── CA0/README.md
├── CA1/README.md
├── CA2/README.md
├── CA3/README.md
└── CA4/README.md
```

!!! warning "Important"
    - Assignments are due at **11:59 PM CT** on the specified date
    - **No late submissions** will be accepted
    - Use GenAI responsibly and document its usage
