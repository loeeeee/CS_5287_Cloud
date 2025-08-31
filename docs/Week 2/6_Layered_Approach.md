# Layered Approach

!!! info "Presentation Format"
    This content was originally created as a Marp presentation.

<div class="slide-content" id="slide-1">

# Layered Approach

Video: [https://youtu.be/SUREWoSzack](https://youtu.be/SUREWoSzack)

</div>
<div class="slide-content" id="slide-2">

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

</div>
<div class="slide-content" id="slide-3">

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

</div>
<div class="slide-content" id="slide-4">

## Cloud Protocols
- Cloud -based services are usually supported at the application layer.
- They are reachable often via HTTP/HTTPS or protocols that build over the Web protocols. 
- Many of the APIs used to host and access the services are RESTful.
    - We will study Representational State Transfer (REST) in detail.
    - We will look at new protocols like MCP (Model Context Protocol)

</div>
