# Primer on Using OpenStack

Overview, core services, deployment, and common workflows

!!! info "Presentation Format"
    This content was originally created as a Marp presentation.

<div class="slide-content" id="slide-1">

# What Is OpenStack?

- Open source “cloud OS” for building IaaS  
- Modular projects for compute, storage, networking, identity, and more  
- Managed by the OpenStack Foundation (Apache 2.0 license)

</div>
<div class="slide-content" id="slide-2">

## Core OpenStack Services

- **Keystone** (Identity)  
  • Authentication, multi-tenant projects, role-based access  

- **Nova** (Compute)  
  • Provision and manage virtual machines (instances)  

- **Glance** (Image)  
  • Store and retrieve VM images and snapshots  

- **Neutron** (Networking)  
  • Software-defined networking: networks, subnets, routers, floating IPs  

- **Cinder** (Block Storage)  
  • Persistent volumes attachable to instances  

- **Swift** (Object Storage)  
  • S3-style, highly durable object store  

- **Horizon** (Dashboard)  
  • Web UI for all OpenStack projects  

- **Heat** (Orchestration)  
  • Template-driven deployment of multi-service stacks

</div>
<div class="slide-content" id="slide-3">

## Architecture & Control Plane

![openstack-OpenStack_Core_Services_Deployment.png](../assets/images/openstack-OpenStack_Core_Services_Deployment.png)

</div>
<div class="slide-content" id="slide-4">

## Installation & Deployment

### 1. All-in-One (Dev/Test)
```
bash
# On a single Ubuntu host
sudo apt update
sudo apt install -y openstack-tools
openstack-quickstart allinone
```
- Spins up Keystone, Nova, Neutron, Glance, Cinder, Horizon

</div>
<div class="slide-content" id="slide-5">

### 2. Multi-Node Production

- **Controller Nodes**: API services, message bus, database, dashboard  
- **Compute Nodes**: Nova compute + hypervisor  
- **Storage Nodes**: Cinder volumes & Swift proxies  
- **Network Nodes**: Neutron L3 agent, DHCP, metadata, LBaaS  

Use an installer/orchestration tool:  
- **OpenStack-Ansible**  
- **Kolla-Ansible** (containerized)  
- **TripleO** (OpenStack on OpenStack)

</div>
<div class="slide-content" id="slide-6">

## Common Workflows

### a) Create a Project & User
```
bash
openstack project create acme
openstack user create bob --project acme --password secret
openstack role add --project acme --user bob member
```

</div>
<div class="slide-content" id="slide-7">

### b) Upload an Image
```
bash
openstack image create ubuntu20 \
--file ubuntu-20.04.qcow2 \
--disk-format qcow2 --container-format bare
```

</div>
<div class="slide-content" id="slide-8">

### c) Launch a VM
```
bash
openstack server create \
--flavor m1.small \
--image ubuntu20 \
--network private-net \
--security-group default \
--key-name mykey \
web01
```

</div>
<div class="slide-content" id="slide-9">

### d) Attach a Volume
```
bash
openstack volume create --size 10 data-vol
openstack server add volume web01 data-vol
```

</div>
<div class="slide-content" id="slide-10">

### e) Floating IP & Security Group
```
bash
# Allocate & assign public IP
openstack floating ip create public-net
openstack server add floating ip web01 <FLOAT_IP>

# Allow SSH & HTTP
openstack security group rule create default --protocol tcp --dst-port 22
openstack security group rule create default --protocol tcp --dst-port 80
```

</div>
<div class="slide-content" id="slide-11">

## Horizon Dashboard

- **Projects → Compute**: instances, flavors, key pairs  
- **Projects → Network**: networks, routers, subnets, security groups  
- **Admin → Identity**: users, projects, roles  
- **Orchestration → Stacks**: Heat templates and stack events

</div>
<div class="slide-content" id="slide-12">

## Best Practices

- **Use Heat** for repeatable, versioned deployments  
- **Separate roles**: isolate API, compute, network, and storage services  
- **Enable high availability**: clustered controllers & database replication  
- **Monitor & log**: integrate with Prometheus/Grafana, ELK/EFK stacks  
- **Secure**: TLS for all endpoints, strong RBAC policies, network segmentation

</div>
<div class="slide-content" id="slide-13">

# Summary

- OpenStack provides a full IaaS stack via modular, API-driven services  
- Deploy via quickstart for dev/test or Ansible/Kolla for production  
- Manage everything through CLI (`openstack`), REST APIs, or Horizon  
- Automate with Heat, enforce security, and monitor for reliability
```

</div>
