# Static Routing

## What is Static Routing?

Static routing is a routing method where the administrator manually tells the router how to reach another network.

Unlike dynamic routing, routers do not discover routes automatically.

---

## Why do we need Static Routing?

Routers only know:

- Directly Connected Networks
- Manually Configured Routes
- Routes learned using Dynamic Routing Protocols

If a router doesn't know where to send a packet, it simply drops it.

---

## Example

PC1
↓

Router A
↓

Router B
↓

PC2

Router A must know that PC2's network exists through Router B.

---

## Advantages

- Easy to configure
- Uses less memory
- Good for small networks

---

## Disadvantages

- Not scalable
- Manual configuration required
- Difficult to manage in large organizations