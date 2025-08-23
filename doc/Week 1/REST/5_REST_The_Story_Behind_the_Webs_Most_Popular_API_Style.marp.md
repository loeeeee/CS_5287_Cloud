---
marp: true
title:  REST: The Story Behind the Web’s Most Popular API Style
paginate: true
theme: default
---

# REST: The Story Behind the Web’s Most Popular API Style
### A deep dive into architecture, constraints, and real‐world impact

Video: (https://youtu.be/Jr56k9dfVyA)[https://youtu.be/Jr56k9dfVyA]

---

## The Web in the 1990s: Challenges & Context
- HTTP/0.9 → simple “GET” only, no standard headers  
- CGI scripts for dynamic content—expensive and stateful  
- Multiple ad hoc protocols (FTP, Gopher, proprietary APIs)  
- Explosive growth of web servers; urgent need for scalable, maintainable interfaces  

---

## Messy field of protocols

- CORBA (Common Object Request Broker Architecture)
    - Complex distributed object system from 1991
    - Language-independent protocol
- DCOM (Distributed Component Object Model)
    - Microsoft's proprietary protocol from 1996
    - Windows-centric communication
- RMI (Remote Method Invocation)
    - Java-specific remote procedure calls from 1996
    - Tightly coupled to Java platform
---

## Messy Field Protocols
- XML-RPC (1998)
    - Simple remote procedure calls using XML
    - Predecessor to SOAP
- SOAP (Simple Object Access Protocol)
    - XML-based messaging protocol from 1999
    - Complex but highly structured

---

## Enter Roy Fielding
- Co-author of the HTTP/1.1 specification (RFC 2068, RFC 2616)  
- 2000 PhD dissertation at UC Irvine introduced “REST”  
- Sought an architectural style to tame complexity of large-scale web systems  
- Emphasis on:  
  - Uniform interfaces  
  - Stateless interactions  
  - Caching for performance  
---

## REST’s Big Idea: Architectural Style, Not Protocol

- Resources identified by URIs (e.g., `/users/1234`)  
- Standard operations via HTTP verbs: GET, POST, PUT, DELETE, PATCH  
- Representations (JSON, XML, HTML) decouple client & server  
- Stateless interactions → easier to scale horizontally  

---

## The Six REST Constraints

1. **Client–Server** separation of concerns  
2. **Stateless** requests: no client context stored on server  
3. **Cacheable** responses improve performance  
4. **Uniform Interface** simplifies and decouples architecture  
5. **Layered System** enables intermediaries (load-balancers, proxies)  
6. **Code-on-Demand** (optional): server can extend client functionality  

---

## Uniform Interface: Four Core Principles

- **Resource Identification** via URIs  
- **Manipulation through Representations** (e.g., send JSON payload)  
- **Self-descriptive Messages** (use standard media types & status codes)  
- **Hypermedia As The Engine Of Application State (HATEOAS)**  

---

## REST in Action: Simple Examples
### Retrieving a User (GET)

```bash
curl -i https://api.github.com/users/octocat \
  -H "Accept: application/vnd.github+json"
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: public, max-age=60
ETag: "W/\"user-12345\""

{
  "login": "octocat",
  "id": 583231,
  "type": "User",
  "html_url": "https://github.com/octocat"
  // ...
}
```
--- 

## HTTP Methods Deep Dive
- **GET**  
  • Safe & idempotent: retrieves resource state without side-effects  
  • Common use: fetch a list (`GET /items`) or single item (`GET /items/123`)  
  • Responses: 200 OK + body, 304 Not Modified (with caches)  

- **POST**  
  • Not idempotent: used to create a subordinate resource or trigger processing  
  • Common use: `POST /orders` with order details → server assigns new ID  
  • Responses: 201 Created + Location header, 400 Bad Request (validation errors)  

- **PUT**  
  • Idempotent: full replacement or upsert of resource at client-specified URI  
  • Common use: `PUT /users/42` with complete user object → replaces existing  
  • Responses: 200 OK (updated), 201 Created (if new), 204 No Content  
---

## HTTP Method Deep Dive (cont)
- **PATCH**  
  • Idempotent (by spec): partial update using a patch document (JSON Patch, Merge Patch)  
  • Common use: `PATCH /users/42` with `{ "email": "new@domain" }`  
  • Responses: 200 OK + updated resource, 204 No Content, 422 Unprocessable Entity  

- **DELETE**  
  • Idempotent: removes the resource at the given URI  
  • Common use: `DELETE /sessions/99` to revoke a session  
  • Responses: 204 No Content (success), 404 Not Found (already removed)  

---

## Common HTTP Response Codes
| Class | Code | Meaning                      | When to Use                              |
|------|------|------------------------------|------------------------------------------|
| 2xx  | 200  | OK                           | Standard success, returns a payload      |
|      | 201  | Created                      | Resource created; include `Location:`    |
|      | 202  | Accepted                     | Request accepted for async processing    |
|      | 204  | No Content                   | Success with no body (e.g., DELETE)      |
| 3xx  | 301  | Moved Permanently            | Resource URI changed permanently         |
|      | 302  | Found                        | Temporary redirect                       |
|      | 304  | Not Modified                 | Caching: client’s cached copy is fresh   |
|      | 303  | See Other                    | Resource URI changed temporarily         |
|      | 307  | Temporary Redirect           | Temporary redirect (e.g., POST)         |
|      | 308  | Permanent Redirect           | Permanent redirect (e.g., POST)         |

---

## Common HTTP Response Codes (cont)

| Class | Code | Meaning                      | When to Use                              |
|-------|------|------------------------------|------------------------------------------|
| 4xx   | 400  | Bad Request                  | Malformed syntax or invalid field        |
|       | 401  | Unauthorized                 | Missing or invalid authentication token  |
|       | 403  | Forbidden                    | Authenticated but not permitted          |
|       | 404  | Not Found                    | Resource does not exist                  |
|       | 409  | Conflict                     | Version conflict, duplicate data         |
|       | 422  | Unprocessable Entity         | Semantic validation failed               |
|       | 429  | Too Many Requests            | Rate limiting                            |
| 5xx   | 500  | Internal Server Error        | Unexpected server failure                |
|       | 502  | Bad Gateway                  | Upstream service returned invalid data   |
|       | 503  | Service Unavailable          | Overloaded or down for maintenance       |
|       | 504  | Gateway Timeout              | Upstream service did not respond in time |
