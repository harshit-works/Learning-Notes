# IP Addressing

## What is an IP Address?

An **IP (Internet Protocol) Address** is a unique numerical address assigned to every device connected to a network.

It allows devices to identify and communicate with each other.

Example:

```
192.168.1.10
```

Think of an IP address like a **house address**. Just as a courier needs your home address to deliver a package, data on a network needs an IP address to reach the correct device.

---

# Why Do We Need an IP Address?

Without IP addresses:

- Devices cannot identify each other.
- Data cannot reach the correct destination.
- Communication over a network is impossible.

---

# IPv4 Address

IPv4 (Internet Protocol Version 4) is the most commonly used version of IP.

### Features

- 32-bit address
- Four octets
- Each octet ranges from 0–255

Example:

```
192.168.10.25
```

Structure:

```
192 . 168 . 10 . 25
 ↑      ↑      ↑      ↑
Octet Octet Octet Octet
```

---

# Binary Representation

Each octet consists of **8 bits**.

Example:

```
192 = 11000000
168 = 10101000
10  = 00001010
25  = 00011001
```

Total bits:

```
8 + 8 + 8 + 8 = 32 bits
```

---

# Public IP Address

A Public IP Address is assigned by an Internet Service Provider (ISP).

Characteristics:

- Globally unique
- Accessible over the Internet
- Assigned by the ISP

Example:

```
103.45.120.15
```

---

# Private IP Address

Private IP addresses are used inside local networks.

These addresses cannot be accessed directly from the Internet.

Common Private IP Ranges:

| Class | Range |
|--------|----------------|
| A | 10.0.0.0 – 10.255.255.255 |
| B | 172.16.0.0 – 172.31.255.255 |
| C | 192.168.0.0 – 192.168.255.255 |

Example:

```
192.168.1.100
```

---

# IP Address Classes

## Class A

Range:

```
1.0.0.0 – 126.255.255.255
```

Default Subnet Mask:

```
255.0.0.0
```

Large organizations.

---

## Class B

Range:

```
128.0.0.0 – 191.255.255.255
```

Default Subnet Mask:

```
255.255.0.0
```

Medium-sized organizations.

---

## Class C

Range:

```
192.0.0.0 – 223.255.255.255
```

Default Subnet Mask:

```
255.255.255.0
```

Small businesses and home networks.

---

## Class D

Used for:

```
Multicasting
```

Range:

```
224.0.0.0 – 239.255.255.255
```

---

## Class E

Reserved for:

```
Research and Experimental purposes
```

Range:

```
240.0.0.0 – 255.255.255.255
```

---

# Subnet Mask

A subnet mask identifies:

- Network Portion
- Host Portion

Example:

```
IP Address

192.168.1.20

Subnet Mask

255.255.255.0
```

This means:

```
Network = 192.168.1
Host = 20
```

---

# Default Gateway

A Default Gateway is the router that forwards traffic from one network to another.

Example:

```
PC

IP Address
192.168.1.20

Gateway
192.168.1.1
```

If the destination is outside the local network, the PC sends data to the default gateway.

---

# DNS (Domain Name System)

Humans remember names.

Computers understand IP addresses.

Example:

```
www.google.com
        │
        ▼
142.250.xxx.xxx
```

DNS converts domain names into IP addresses.

---

# Static IP Address

A Static IP Address does not change.

Used for:

- Servers
- Printers
- Routers

Advantages:

- Stable
- Easy to manage

---

# Dynamic IP Address

A Dynamic IP Address changes automatically.

Assigned by:

```
DHCP Server
```

Most home networks use Dynamic IP addresses.

---

# DHCP

DHCP stands for:

**Dynamic Host Configuration Protocol**

Purpose:

Automatically assigns:

- IP Address
- Subnet Mask
- Default Gateway
- DNS Server

Without DHCP, every device would need to be configured manually.

---

# IPv4 vs IPv6

| IPv4 | IPv6 |
|------|------|
| 32-bit | 128-bit |
| Limited addresses | Huge address space |
| Example: 192.168.1.1 | Example: 2001:db8::1 |

---

# Real-Life Example

Suppose your laptop has:

```
IP Address
192.168.1.20

Subnet Mask
255.255.255.0

Gateway
192.168.1.1
```

When you open:

```
www.google.com
```

The process is:

1. DNS converts the domain name into an IP address.
2. Your PC checks whether the destination is inside your local network.
3. If not, it sends the request to the default gateway (router).
4. The router forwards the request to the Internet.
5. Google's server responds, and the data returns to your computer.


# Summary

- Every device requires an IP address.
- IPv4 uses 32 bits.
- IPv6 uses 128 bits.
- Public IPs are assigned by ISPs.
- Private IPs are used inside LANs.
- DHCP automatically assigns IP addresses.
- DNS converts domain names into IP addresses.
- The default gateway forwards traffic outside the local network.