---
marp: true
title:  Layered Approach
paginate: true
theme: default
---

  # Layered Approach
---
## Layered Approach
Networks are complex, with many “ pieces”:
- Hosts
- Routers
- Links of various media
- Applications
- Protocols
- Hardware, software 

Question: Is there any hope of organizing structure of
network?
- …Or at least our discussion of networks?
Layered architecture is the solution. 

---
## Internet Protocol Stack

- Application: supporting network applications
  - FTP, SMTP, HTTP
- Transport: process -process data transfer
  - TCP, UDP
- Network: routing of datagrams from source to destination
  - IP, routing protocols
- Link: data transfer between neighboring network elements
  - Ethernet, 802.11 (Wi -Fi), PPP
- Physical: bits “ on the wire”

---
## Cloud Protocols
- Cloud -based services are usually supported at the application layer.
- They are reachable often via HTTP/HTTPS or protocols that build over the Web protocols. 
- Many of the APIs used to host and access the services are RESTful.
    - We will study Representational State Transfer (REST) in detail.
    - We will look at new protocols like MCP (Model Context Protocol)

---
