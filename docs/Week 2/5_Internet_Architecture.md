# Internet Architecture

!!! info "Presentation Format"
    This content was originally created as a Marp presentation.

<div class="slide-content" id="slide-1">

# Internet Architecture

Video: [https://youtu.be/KUW2ZneyRaw](https://youtu.be/KUW2ZneyRaw)

</div>
<div class="slide-content" id="slide-2">

## What's The Internet: A Service View

- Infrastructure that provides services to applications
    - Web, VoIP, email, games, e -commerce, social nets, ...
- Provides programming interface to apps
    - Hooks that allow sending and receiving app programs to “connect” to Internet
    - Provides service options, analogous to postal service

</div>
<div class="slide-content" id="slide-3">

## A Closer Look at the Network Structure
- Network edge
    - Hosts: clients and servers
    - Servers often in data centers
- Access networks, physical media :
    - wired, 
    - wireless communication links
- Network core
    - Interconnected routers
    - Network of networks

</div>
<div class="slide-content" id="slide-4">

## Access Networks and Physical Media
- Question: How to connect end systems to edge router?
    - Residential access nets
    - Institutional access networks (school, company)
    - Mobile access networks
- Issues to keep in mind
    - Bandwidth (bits per second) of access network?
    - Shared or dedicated?
    - Reliability

</div>
<div class="slide-content" id="slide-5">

## The Network Core
- Mesh of interconnected routers
- Packet -switching: hosts break application layer messages into packets
    - Forward packets from one router to the next, across links on path from source to destination
    - Each packet transmitted at full link capacity

</div>
<div class="slide-content" id="slide-6">

## Internet Structure: Network of Networks

- End systems connect to Internet via access ISPs (Internet Service Providers).
    - Residential, company, and university ISPs
- Access ISPs in turn must be interconnected.
    - So that any two hosts can send packets to each other
- Resulting network of networks is very complex.
    - Evolution was driven by economics and national policies
- Let’s take a stepwise approach to describe current Internet structure.

</div>
<div class="slide-content" id="slide-7">

## Internet Structure: Network of Networks
- But if one global ISP is viable business, there will be competitors… which must be interconnected…

![internetstructure.png](../assets/images/internetstructure.png)

</div>
<div class="slide-content" id="slide-8">

## Internet Structure: Network of Networks
... And Regional networks may arise to connect access nets to ISPs

![RegionalNetworks.png](../assets/images/RegionalNetworks.png)

</div>
<div class="slide-content" id="slide-9">

## Internet Structure: Network of Networks

... And content provider networks (e.g., Google, Microsoft, Akamai) may run their own network, to bring services, content close to end users

![contentproviders.png](../assets/images/contentproviders.png)

</div>
