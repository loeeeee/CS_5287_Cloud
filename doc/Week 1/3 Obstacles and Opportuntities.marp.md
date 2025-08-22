---
marp: true
theme: default
class: lead
paginate: true
---

# Obstacles and Opportunities

Video: [Obstacles and Opportunities](https://youtu.be/u-skcK6CyL8)

---

## Availability issues
* Businesses do not want to suffer due to cloud outages.
* See [Service Status](https://cloudharmony.com/status).
* See the [10 Biggest Cloud Outages Of 2019](https://www.crn.com/slide-shows/cloud/the-10-biggest-cloud-outages-of-2019-so-far-) for listing of significant outages in 2019.
* See [AWS Thanksgiving Outage 2020](https://embracingdigital.org/en/episodes/edt-33/index.html)
---

## Vendor lock-in
* APIs used by cloud providers are not uniform.
* Applications will get locked into vendor APIs.
    * Some effort underway for standardization
    * For example, Apache DeltaCloud, Open Cloud Computing Interface (OCCI)
* Hotel California (Egress costs, Expensive to move data out)

---

## Obstacles to Cloud Computing

* Lack of trust (confidentiality, accountability)
* Security threats from inside and outside
* Virtualization is a good solution, but does not solve all problems
* Bad configuration or incorrect virtualization may lead to problems.


---

## Data movement bottlenecks
* The size of data being moved keeps increasing
* We need to be careful as to where we place the data storage devices and how networks are configured
* Sometimes shipping the data in disks is better and faster 
    
---

## Performance unpredictability (Noisy neighbor problem)

* VMs share resources—can cause interference
* Disks and networks are also shared
* How these virtualized resources get scheduled can impact performance
* Could be bad for high performance computing tasks who need all their threads to be running all at once, but there is no way to ensure this
* Multiple simultaneous types of virtualization coexisting (VMs, containers, etc.)

---

## Scalable storage

* Unclear how the elasticity models apply to persistent storage
* SSD technology is making significant impact
--- 

## Bugs in distributed systems software
* Cloud is a distributed system
* Programming distributed systems is hard
* There is every possibility of a bug lurking around somewhere or assumptions that are made, which may not be accurate or remain undocumented, etc.
* Reproducing the bugs at scale and debugging is hard
--- 

## Instant scaling up/down is hard

* It takes time for VMs to be allocated (lightweight virtualization is becoming popular, e.g., Docker, Unikernel)
* Machines in data centers may be shut down to conserve energy (recall that idle machines do consume power)

---

## Sharing resources may lead to sharing bad reputation

* A bad customer causing havoc in a cloud environment (e.g., doing some malicious activity) may impact the reputation of other customers sharing the hosting platforms
* For example, since IP addresses are often floating, some IP addresses may get blacklisted
* Legal issues and finger-pointing with regard to the blame
---
## Software licensing
* How to deal with software licensing?
* For example, many Windows products are assigned to specific users on specific machines (that is why they came up with Office 365)
* How to make these products part of PaaS/SaaS?

---

## Obstacles and Opportunities

| # | Obstacle | Opportunity |
|----------|-----------|-------------|
| 1 | Availability/business continuity | Use multiple cloud providers |
| 2 | Data lock-in | Standardize APIs; compatible software to enable surge or hybrid cloud computing |
| 3 | Data confidentiality and auditability | Deploy encryption, VLANs, firewalls |
| 4 | Data transfer bottlenecks | FedExing disks; higher BW switches |
| 5 | Performance unpredictability | Improved VM support; flash memory; gang schedule VMs |

--- 

| # | Obstacle | Opportunity |
|----------|-----------|-------------|
| 6 | Scalable storage | Invent scalable store |
| 7 | Bugs in large distributed systems | Invent debugger that relies on distributed VMs |
| 8 | Scaling quickly | Invent auto-scaler that relies on ML; snapshots for conservation |
| 9 | Reputation fate sharing | Offer reputation-guarding services like those for email |
| 10 | Software licensing | Pay-for-use licenses |


---