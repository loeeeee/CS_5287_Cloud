---
marp: true
theme: default
paginate: true
size: 16:9
title: Containers: Key Principles and Concepts
---

## Containers: Evolution & History

- **1979–2000: Early Unix Roots**  
  • `chroot` (1979): filesystem isolation  
  • FreeBSD Jails (2000), Solaris Zones (2004)

- **2006–2012: Linux Foundations**  
  • Namespaces (2002), cgroups (2006)  
  • LXC (2008) combining both

- **2013–Present: Modern Era**  
  • Docker (2013): developer-friendly tooling  
  • rkt (2014) & OCI standard (2015)  
  • containerd (2016) & CRI-O for Kubernetes

---

## Isolation Mechanisms

**Namespaces**
- PID, network, mount, UTS, IPC, user

**Control Groups (cgroups)**
- CPU, memory, I/O, network limits

**Union Filesystems**
- Copy-on-write layers for fast startup & minimal storage

---

## Container Image Model

- **Base Images**: minimal OS/runtime (`alpine`, `ubuntu`)
- **Layered Builds**: each Dockerfile step adds a layer
- **Immutable Artifacts**: content-addressable (SHA256)
- **Registries**: Docker Hub, GCR, private OCI v2

---

## Portability & Consistency

- **Build once, run anywhere**
- Bundles dependencies & config
- Declarative specs (`Dockerfile`, OCI image spec)

---

## Performance & Density

- **Milliseconds startup** vs. seconds for VMs
- **High consolidation**: hundreds of containers per host
- **Low overhead**: no guest OS kernel

---

## Security Considerations

- Non-root execution & dropped capabilities
- Image hardening & vulnerability scanning
- SELinux/AppArmor, seccomp, rootless mode
- Supply-chain: image signing (Notary, Sigstore)

---

## Ecosystem & Standards

- **Docker Engine**: CLI, daemon, REST API
- **containerd / CRI-O**: lightweight runtimes
- **OCI**: image & runtime specifications

---

## Orchestration Needs

- **Scheduling & Scaling**: Kubernetes, Docker Swarm
- **Service Discovery & Networking**: overlay networks, load balancing
- **Config & Secrets**: ConfigMaps, Secrets
- **Self-Healing & Rollouts**: health checks, declarative updates

---

## Best Practices

- Small, single-responsibility images
- Multi-stage builds for lean images
- Immutable infra: recreate, don’t patch
- CI/CD: automate build, test, scan, push
- Always set resource limits (`cpu`, `memory`)

---

# Summary

Containers leverage OS kernel features and layered images  
to deliver portable, efficient, and consistent environments.  
Understand history, isolation, security, and orchestration to  
build robust cloud-native systems.