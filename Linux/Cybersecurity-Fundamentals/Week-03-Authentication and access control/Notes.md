# Authentication & Access Control

## 13. Authentication

Authentication verifies **who a user is**.

Example:
- Username + Password
- Fingerprint
- Security key

---

# 14. Authorization

Authorization determines **what an authenticated user is allowed to access or perform**.

Example:

A normal employee may read a document, while an administrator may read and modify it.

---

# 15. Accounting / Auditing

Accounting records and monitors **what users do** within a system.

Example:
- Login attempts
- File access
- Configuration changes
- Administrative actions

### AAA

AAA stands for:

- Authentication → Who are you?
- Authorization → What are you allowed to do?
- Accounting → What did you do?

---

# 16. Password Policies

A password policy is a set of rules used by an organization to improve password security.

Common practices include:
- Use strong, unique passwords
- Avoid easily guessed passwords
- Prevent use of known compromised passwords
- Use MFA where possible
- Apply appropriate password-management policies

---

# 17. Multi-Factor Authentication (MFA)

MFA requires more than one authentication factor.

### Three Common Factors

1. Something you know
   - Password
   - PIN

2. Something you have
   - Security key
   - Phone
   - Authenticator device

3. Something you are
   - Fingerprint
   - Face recognition

Using multiple factors makes account compromise more difficult than relying only on a password.

---

# 18. RBAC

RBAC = Role-Based Access Control

Users are assigned roles, and permissions are assigned to those roles.

Example:

Admin → Full access

Employee → Normal access

Guest → Limited access

### Advantage

Instead of manually assigning permissions to every user, administrators can manage permissions through roles.

---

# 19. ACL

ACL = Access Control List

An ACL is a list of rules specifying:
- Who can access a resource
- What actions they can perform

Example:

| User/Group | Resource | Permission |
|---|---|---|
| Admin | Server | Full Access |
| Employee | Files | Read/Write |
| Guest | Files | Read |

---

# 20. IAM

IAM = Identity and Access Management

IAM is a system/framework used to manage:

- User identities
- Authentication
- Authorization
- Permissions
- Access to resources

The main goal is to ensure that the **right person gets the right access to the right resource**.

---

# 21. SSO

SSO = Single Sign-On

SSO allows a user to authenticate once and access multiple applications without logging into each application separately.

### Example

User logs into an organization's identity provider.

↓

The user can access multiple authorized applications.

### Benefits
- Better user experience
- Centralized authentication
- Easier account management
- Reduced password reuse
