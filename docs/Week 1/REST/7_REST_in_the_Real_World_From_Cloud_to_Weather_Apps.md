# Presentation

<div class="slide-content" id="slide-2">

marp: true
title:  REST in the Real World: From Cloud to Weather Apps
paginate: true
theme: default

</div>
<div class="slide-content" id="slide-3">

# REST in the Real World: From Cloud to Weather Apps

</div>
<div class="slide-content" id="slide-4">

## Common REST APIs

- GitHub: World's largest platform for software development, offering APIs for repository management, issue tracking,
  and user data
- OpenWeather: Provides weather data and forecasts through APIs, including current conditions, historical data, and
  meteorological maps
- Chameleon Cloud: Scientific computing cloud platform with RESTful APIs for managing compute resources, storage, and
  networking experiments

</div>
<div class="slide-content" id="slide-5">

## GitHub API Example

- `GET /users/{username}/repos`
- JSON response demo:

</div>
<div class="slide-content" id="slide-6">

## OpenWeather API Example
- `GET /data/2.5/weather?q=Nashville`
- Show parameters and results

</div>
<div class="slide-content" id="slide-7">

## Chameleon Cloud Example
- Creating and managing VMs
- REST API vs Web UI

</div>
<div class="slide-content" id="slide-8">

## Why Developers Love REST

- Simple tools like curl and Postman for testing
- Language agnostic - works with Python, Java, JavaScript
- Leverages HTTP and standard web infrastructure
- Resource-based URL structure
- Stateless requests containing all needed info
- Standard HTTP methods (GET, POST, PUT, DELETE)
- Built-in HTTP caching support
- Documentation via Swagger/OpenAPI

</div>
<div class="slide-content" id="slide-9">

## REST's Limitations

- Real-time needs
    - WebSocket protocol better suited for bidirectional, real-time communication
    - gRPC provides efficient streaming capabilities
    - REST's request-response model has higher latency for real-time updates

- Complex queries
    - GraphQL allows clients to request specific data fields
    - REST endpoints can be inflexible for varying data needs
    - Multiple REST requests often needed to gather related data
    - Over-fetching and under-fetching of data common with REST

</div>
