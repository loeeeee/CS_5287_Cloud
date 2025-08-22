---
marp: true
theme: default
class: lead
paginate: true
---
 
## Cloud Computing

Video link: [Cloud Computing](https://youtu.be/NYlDMK28Hyk)

--- 

## Motivating Scenario

- Small business starts a new internet service.
- Service needs computing power, network bandwidth, and storage.
- Resources can be made available in-house.
- Both capital and operational costs required.
- Short-term service risks capital losses.
- Success needs more resources and higher costs.
- Idle resources waste operational expenses.

---

## Desired Solution

- Can entrepreneurs lease resources from someone?
- A service model needed for leasing computing resources
- Resources stay with the provider, not shipped
- Small businesses lack space and capability
- Energy and scaling remain problematic
- Physical movement limits timely scaling
- Resources must be remotely accessible
- No responsibility for capex/opex - on-demand availability
- Pay-per-use like traditional utilities


--- 
## Cloud Computing Key Properties

(Based on Berkeley Paper)
- Supports the notion of utility computing
- Pay as you go
- Service is what gets sold (or offered for a price)
- Elasticity of resources without paying a premium for the scale
- Using 1,000 servers for one hour costs no more than using one server for 1,000 hours
- No need to pay any upfront costs and no lock-in
- Appearance of infinite computing resources available on demand
- This becomes feasible with very large data centers

---

## User Perspective of the Cloud

- Revival of the thin client on the Web
- Utility computing that charges according to metered usage
- Complex tasks which can be processed in distributed/parallel fashion to gain efficiency
- Power that is derived from the collection of commodity hardware rather than individual expensive parts


<i>Pretty much everything above is what constitutes the cloud.</i>

---

## Definition of Cloud Computing
Very hard to define, but one such definition from the National Institute for Standards and Technology has become the de facto definition
•See The [NIST Definition of Cloud Computing](http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)

```
2. The NIST Definition of Cloud Computing
   Cloud computing is a model for enabling ubiquitous, convenient, 
   on-demand network access to a shared pool of configurable computing 
   resources (e.g., networks, servers, storage, applications, and services)
   that can be rapidly provisioned and released with minimal management
   effort or service provider interaction. This cloud model is composed 
   of five essential characteristics, three service models, 
   and four deployment models.
```
---

## Parsing the Definition

### Model

An abstraction for the framework or approach that serves as an enabling
technology for the following:

- Ubiquitous: accessible from anywhere, pervasive
- Convenient: should be very easy to use via any available mechanism
- On-demand: as and when needed
- Network-access: accessible over a network

---

## Parsing the Definition, Part II

- Resources: a variety of resources, e.g., CPU, storage, networks, etc.
- Shared pool: collection of resources shared across everyone who uses them; these are often owned by a separate entity called the cloud provider
- Configurable: ability to fine-tune these resources suited to our needs (even if they are part of a shared pool)
- Possible due to virtualization and isolation

---

## Parsing the Definition, Part III

- Rapidly provisioned/released: can be obtained almost instantaneously on demand and suited to our requirements or released to the pool when not needed
- Minimal management effort: no sophisticated machinery needed on the part of user to manage these resources
- Minimal service provider interaction: almost no need to interact with the service provider

---

## Five Essential Characteristics

1. On-demand self-service: ability to provision resources on- demand without much effort
2. Broad network access: accessible via the network through standard mechanisms (e.g., http) using a variety of end devices
3. Resource pooling: resources are obtained from a shared pool; their location and whether they are physical or virtual makes no difference to the user
4. Rapid elasticity: ability to scale up or down on-demand
5. Measurable service: ability to meter the usage and charged for whatever is being used [utility computing]