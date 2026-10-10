# Network Devices

## Introduction

Network devices are hardware components that enable communication between computers and other devices in a network. Each device performs a specific function to ensure data reaches its destination efficiently.

---

# Internet Service Provider (ISP)

An Internet Service Provider (ISP) provides internet connectivity to users.

Examples:
- JioFiber
- Airtel Xstream Fiber
- BSNL
- ACT Fibernet

### Responsibilities of an ISP

- Provides Internet access.
- Assigns a Public IP Address.
- Routes traffic between users and the Internet.

---

# Public IP Address

A Public IP Address is assigned by an ISP and is unique across the Internet.

### Features

- Globally unique
- Used to communicate over the Internet
- Assigned by the ISP

Example:

203.10.2.80

---

# Private IP Address

A Private IP Address is used inside a Local Area Network (LAN).

### Features

- Cannot be accessed directly from the Internet.
- Assigned by the router.
- Used for communication between local devices.

Examples:

- 192.168.0.1
- 192.168.1.10
- 10.0.0.5

---

# Local Area Network (LAN)

A LAN (Local Area Network) is a network that connects devices within a limited geographical area.

Examples:

- Home
- School
- Office

Devices inside a LAN communicate using Private IP addresses.

---

# Router

A Router is a Layer 3 networking device that connects different networks.

### Functions

- Connects a LAN to the Internet.
- Routes packets between networks.
- Assigns Private IP addresses (using DHCP in home networks).
- Acts as the default gateway for connected devices.

### Example

```
Internet
    │
Public IP
    │
 Router
 ├── Laptop
 ├── PC
 ├── Mobile
 └── Printer
```

---

# Switch

A Switch is a Layer 2 networking device used to connect multiple devices within the same Local Area Network (LAN).

### Functions

- Connects computers and other devices.
- Sends data only to the destination device.
- Reduces unnecessary network traffic.

### Advantages

- Faster than a Hub.
- More secure.
- Efficient communication.

---

# Hub

A Hub is a basic networking device that connects multiple devices.

### Characteristics

- Broadcasts data to every connected device.
- Does not know the destination device.
- Less efficient than a Switch.
- Rarely used in modern networks.

---

# Access Point (AP)

An Access Point (AP) provides wireless connectivity to devices.

### Example

```
Router
   │
Switch
   │
Access Point
   │
Wi-Fi Devices
```

Examples of wireless devices:

- Smartphones
- Tablets
- Laptops

---

# Network Interface Card (NIC)

NIC stands for **Network Interface Card**.

It is a hardware component that allows a computer to connect to a network.

### Functions

- Connects a device to a wired or wireless network.
- Provides a unique MAC Address.
- Sends and receives network data.

Modern laptops usually have a built-in NIC.

---

# Firewall

A Firewall is a network security device that monitors and filters incoming and outgoing network traffic based on predefined security rules.

### Functions

- Blocks unauthorized access.
- Allows trusted traffic.
- Protects the internal network from attacks.

Firewalls are commonly used in homes, offices, and data centers.

---

# Client and Server

## Client

A Client is a device that requests a service.

Examples:

- Laptop
- Mobile Phone
- Desktop Computer

## Server

A Server provides services to clients.

Examples:

- Web Server
- Mail Server
- Database Server
- File Server

### Example

```
Client (India)
      │
      ▼
 Web Server
      │
      ▼
Client (USA)
```

The server processes client requests and sends back the required response.

---

# ISP Hierarchy (Basic Overview)

```
Tier 1 ISP
      │
      ▼
Tier 2 ISP
      │
      ▼
Tier 3 ISP
      │
      ▼
Home / Office Users
```

### Tier 1 ISP

- Owns global backbone networks.
- Connects countries using submarine fiber optic cables.

### Tier 2 ISP

Purchases bandwidth from Tier 1 providers and serves larger regions.

### Tier 3 ISP

Provides Internet services directly to homes and businesses.

---

# Key Differences

| Router | Switch |
|---------|---------|
| Connects different networks | Connects devices within the same network |
| Works at Layer 3 | Works at Layer 2 |
| Uses IP addresses | Uses MAC addresses |

---

| Switch | Hub |
|---------|-----|
| Intelligent forwarding | Broadcasts to all devices |
| Faster | Slower |
| More secure | Less secure |

---

# Summary

- ISP provides Internet connectivity.
- Routers connect different networks.
- Switches connect devices inside a LAN.
- Hubs broadcast data to every device.
- Access Points provide wireless connectivity.
- NIC allows a computer to join a network.
- Firewalls protect networks from unauthorized access.
- Clients request services, while servers provide them.