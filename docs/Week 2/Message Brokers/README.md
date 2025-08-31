# Message Brokers Overview

Asynchronous messaging, patterns, deployment & cloud management

!!! info "Presentation Format"
    This content was originally created as a Marp presentation.

<div class="slide-content" id="slide-1">

# Message Brokers Overview

![messagebroker-Generalized_Message_Broker_Architecture.png](../assets/images/messagebroker-Generalized_Message_Broker_Architecture.png)

Middleware for reliable, decoupled, asynchronous communication  

* Producers → Broker → Consumers  
* Features: durability, routing, load balancing, traffic shaping

</div>
<div class="slide-content" id="slide-2">

## Why Use a Message Broker?

- Decoupling of producers & consumers
- Asynchronous, non-blocking workflows
- Scalability via competing consumers
- Reliability: persisted messages survive failures
- Advanced routing & transformation
- Traffic shaping & rate limiting

</div>
<div class="slide-content" id="slide-3">

## Popular Message Broker Platforms

- **RabbitMQ** (AMQP, exchanges–direct/fanout/topic)
- **Apache Kafka** (distributed log, high throughput, replayable)
- **ActiveMQ / Artemis** (JMS-compliant, multi-protocol)
- **AWS SQS & SNS** (fully managed queues & pub/sub)
- **Google Cloud Pub/Sub** (global, auto-scaling, at-least-once/exactly-once)

</div>
<div class="slide-content" id="slide-4">

## Common Messaging Patterns

1. **Point-to-Point (Work Queue)**
2. **Publish/Subscribe (Fan-out)**
3. **Routing (Topic / Pattern Matching)**
4. **Request/Reply (RPC-style)**
5. **Competing Consumers**
6. **Dead-Letter Queues**

</div>
<div class="slide-content" id="slide-5">

## Pattern: Point-to-Point

![point-tp-point-Point_to_Point_Messaging_Pattern.png](../assets/images/point-tp-point-Point_to_Point_Messaging_Pattern.png)

Producer → Queue → Single consumer  

Use case: background jobs, task offload

</div>
<div class="slide-content" id="slide-6">

## Pattern: Publish/Subscribe

![pubsub-Publish_Subscribe_Messaging_Pattern.png](../assets/images/pubsub-Publish_Subscribe_Messaging_Pattern.png)

Producer → Exchange/Topic → Multiple queues → Multiple consumers  

Use case: broadcasting events, notifications

</div>
<div class="slide-content" id="slide-7">

## Pattern: Routing / Topics

![topic_based_messaging_pattern-Routing___Topic_Based_Messaging_Pattern.png](../assets/images/topic_based_messaging_pattern-Routing___Topic_Based_Messaging_Pattern.png)

- Messages carry routing keys
- Consumers subscribe with patterns (e.g. `order.*`)
- Selective delivery of events

</div>
<div class="slide-content" id="slide-8">

## Pattern: Request/Reply

![request_reply_messaging_pattern-Request_Reply_Messaging_Pattern.png](../assets/images/request_reply_messaging_pattern-Request_Reply_Messaging_Pattern.png)

1. Producer sends request + `reply-to`
2. Consumer processes & replies  
   Use case: RPC between microservices

</div>
<div class="slide-content" id="slide-9">

## Deployment Models

### Self-Managed Brokers

- Install on VMs or Kubernetes
- Full control: configs, plugins, network
- You manage HA, upgrades, scaling

### Managed Services

- AWS SQS/SNS, Azure Service Bus, GCP Pub/Sub, Amazon MQ
- Provider handles provisioning & scaling
- Limited low-level customization

</div>
<div class="slide-content" id="slide-10">

## High Availability & Scaling

- **Clustering**
    - RabbitMQ clusters, mirrored queues
    - Kafka brokers + partition replicas
- **Auto-Scaling**
    - K8s Operators (Strimzi for Kafka)
    - VM group scaling on metrics
- **Geo-Replication**
    - Multi-AZ clusters, MirrorMaker, Federation

</div>
<div class="slide-content" id="slide-11">

## Security & Configuration

- TLS for in-transit encryption
- AuthN/AuthZ: SASL, OAuth2, IAM roles
- Role-based access controls & policies
- Durable queues & retention policies
- Backups & disaster recovery

</div>
<div class="slide-content" id="slide-12">

## Monitoring & Observability

- Export metrics (Prometheus, CloudWatch, Stackdriver)
- Key metrics: message rate, queue depth, consumer lag
- Dashboards + alerts for anomalies

</div>
<div class="slide-content" id="slide-13">

## Best Practices

- Design idempotent consumers
- Keep messages small; use references for large payloads
- Drain in-flight messages on shutdown
- Enforce schemas with registry (e.g., Avro)
- Implement retries + exponential backoff
- Use dead-letter queues for failures

</div>
<div class="slide-content" id="slide-14">

# Summary

- Brokers enable scalable, reliable, decoupled systems
- Choose platform & patterns to fit your use case
- Leverage cloud or self-managed deployment
- Secure, monitor, and follow operational best practices

</div>
