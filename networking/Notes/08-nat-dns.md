# NAT (Network Address Translation)

NAT converts Private IP addresses into Public IP addresses.

This allows private devices to access the Internet.

---

## Why NAT?

IPv4 addresses are limited.

Instead of giving every device a Public IP, NAT allows many devices to share one Public IP.

---

## Static NAT

One Private IP

↓

One Public IP

Permanent mapping.

---

## Dynamic NAT

Public IPs are assigned from a pool.

First available Public IP is used.

---

# DNS (Domain Name System)

DNS converts domain names into IP addresses.

Example:

google.com

↓

142.250.xxx.xxx

---

## DNS Process

User

↓

DNS Resolver

↓

Root Server

↓

TLD Server (.com)

↓

Authoritative DNS Server

↓

Returns IP Address