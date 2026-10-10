# Cryptography & Authentication

## 1. What is Cryptography?

Cryptography is the practice of protecting information by converting it into a form that unauthorized users cannot understand.

It helps provide:
- Confidentiality
- Integrity
- Authentication
- Non-repudiation

### Basic Process

Plaintext → Encryption + Key → Ciphertext

Ciphertext → Decryption + Key → Plaintext

---

# 2. Types of Cryptography

## Symmetric Key Cryptography

Symmetric cryptography uses the **same secret key** for encryption and decryption.

### Characteristics
- One key is used for both encryption and decryption.
- The key must be kept secret.
- Faster than asymmetric cryptography.
- Suitable for encrypting large amounts of data.

### Examples
- AES
- DES
- 3DES
- Blowfish

### Main Challenge
The secret key must be securely shared between the sender and receiver.

---

## Stream Cipher

A stream cipher encrypts data continuously, usually one bit or byte at a time.

### Characteristics
- Processes data as a continuous stream.
- Generally fast.
- Useful when data arrives continuously.

### Example
- RC4 (legacy/insecure today)

---

## Block Cipher

A block cipher divides plaintext into fixed-size blocks and encrypts each block.

### Examples
- AES
- DES
- 3DES

### AES
AES uses a **128-bit block size** and supports:
- 128-bit key
- 192-bit key
- 256-bit key

AES is widely used today.

---

# 3. Asymmetric Key Cryptography

Asymmetric cryptography uses **two different keys**:

- Public Key
- Private Key

The public key can be shared, while the private key must remain secret.

### Basic Concept

Public Key → Encryption

Private Key → Decryption

For digital signatures, the roles are used differently:

Private Key → Sign

Public Key → Verify

### Advantages
- Solves the key-exchange problem found in symmetric encryption.
- Enables digital signatures.
- Useful for secure communication and authentication.

### Disadvantage
- Slower than symmetric encryption.

### Examples
- RSA
- ECC

---

# 4. Symmetric vs Asymmetric Cryptography

| Feature | Symmetric | Asymmetric |
|---|---|---|
| Keys | One secret key | Public + Private key |
| Speed | Faster | Slower |
| Key distribution | More difficult | Easier |
| Large data encryption | Suitable | Usually not preferred |
| Examples | AES, 3DES | RSA, ECC |

---

# 5. AES, DES, 3DES & Blowfish

## DES

DES (Data Encryption Standard) is an older symmetric block cipher.

- 64-bit block size
- 56-bit effective key
- No longer considered secure for modern use

## 3DES

3DES applies the DES algorithm multiple times.

It was introduced to improve the security of DES but is now considered legacy technology.

## AES

AES (Advanced Encryption Standard) is the modern replacement for DES.

- 128-bit block size
- 128/192/256-bit keys
- Widely used today

## Blowfish

Blowfish is a symmetric block cipher that was historically used in various applications.

It is now considered a legacy choice compared with modern algorithms such as AES.

---

# 6. Hashing

Hashing converts input data into a fixed-length value called a **hash** using a hash function.

Example:

Password → Hash Function → Hash Value

### Important Properties
- One-way operation
- Same input produces the same hash
- Small input changes produce a very different hash
- Modern cryptographic hashes are designed to resist collisions

Hashing is **not encryption** because there is no normal decryption process.

### Common Hash Algorithms
- SHA-256
- SHA-512
- SHA-3

---

# 7. SHA-256

SHA-256 is part of the SHA-2 family.

- Produces a **256-bit hash**
- Used for integrity verification and many security applications
- Designed to make it computationally difficult to find collisions or recover the original input

Example:

Message → SHA-256 → 256-bit hash

> SHA-1 is considered weak and should not be used for modern security applications.

---

# 8. Salting

A salt is a **random value added to a password before hashing**.

Example:

Password + Random Salt → Hash Function → Stored Hash

### Why use Salting?

Without salt, two users with the same password could have the same hash.

A unique salt makes precomputed attacks such as rainbow-table attacks much harder.

---

# 9. Peppering

A pepper is an additional secret value used when hashing passwords.

Unlike a salt, the pepper is **not normally stored alongside the password hash in the database**.

It should be kept separately and protected as a secret.

### Salt vs Pepper

| Salt | Pepper |
|---|---|
| Usually unique per password | Usually a shared secret |
| Stored with the password hash | Stored separately |
| Not required to be secret | Must be kept secret |

---

# 10. Digital Signature

A digital signature is used to provide:

- Authentication
- Integrity
- Non-repudiation

### Basic Process

1. Sender creates a hash of the message.
2. Sender signs the hash using their private key.
3. Receiver uses the sender's public key to verify the signature.
4. Receiver calculates the message hash again.
5. The hashes/signature verification are compared.

If verification succeeds, the receiver can have confidence that the message came from the holder of the private key and was not modified.

---

# 11. RSA

RSA is an asymmetric cryptographic algorithm named after:

- Rivest
- Shamir
- Adleman

It uses a public key and private key.

### Common Uses
- Digital signatures
- Key exchange / key transport in legacy systems
- Encryption of small amounts of data

Modern systems often use asymmetric cryptography to establish or protect keys and then use symmetric encryption such as AES for bulk data.

---

# 12. TLS Handshake

TLS (Transport Layer Security) establishes a secure connection between a client and server.

It helps provide:
- Authentication
- Confidentiality
- Integrity

### Simplified Process

Client → Server: ClientHello

Server → Client: ServerHello + Certificate

Client verifies the certificate.

The client and server establish shared cryptographic keys.

Secure encrypted communication begins.

### Important

Older material may refer to this as the **SSL handshake**, but modern secure connections use **TLS**. SSL is obsolete.

### Where TLS is Used

- HTTPS
- Secure web applications
- Secure APIs
- Email security
- Other encrypted network communications