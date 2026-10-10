# Stored XSS – HTML Context with Nothing Encoded

## Overview

This lab demonstrates a **Stored Cross-Site Scripting (XSS)** vulnerability.

Unlike reflected XSS, the malicious input is first **stored by the application** and is later returned to users when they view the affected page.

## Lab Environment

* **Platform:** PortSwigger Web Security Academy
* **Lab:** Stored XSS into HTML context with nothing encoded
* **Tool:** Burp Suite
* **Application:** Intentionally vulnerable blog application

## Objective

The objective was to determine whether user-controlled input submitted through the comment functionality could be stored by the application and later interpreted as executable content when the page was loaded.

## Vulnerability

The application's comment functionality does not properly encode user-supplied input before inserting it into the HTML response.

This allows attacker-controlled content to be stored and later interpreted by the victim's browser when the affected page is viewed.

## Methodology

### 1. Identify the Input Point

The blog application provides a comment form containing fields such as:

* Comment
* Name
* Email
* Website

The **Comment** field was selected as the injection point.

### 2. Submit the Test Input

A test XSS payload was entered into the comment field:

```html
<script>alert(1)</script>
```

The comment was then submitted to the application.

![XSS payload submitted in comment](screenshots/xss-comment.png)

### 3. Stored Content

The application stores the submitted comment.

When the affected blog page is loaded again, the stored comment is retrieved and included in the page response.

### 4. Browser Execution

Because the application does not properly encode the stored input, the browser can interpret the injected content as HTML/script rather than ordinary text.

Successful JavaScript execution confirms the Stored XSS vulnerability.

![Successful XSS execution](screenshots/xss-execution.png)

## Result

The lab was successfully completed.

The testing demonstrated that attacker-controlled input submitted through the comment functionality could be stored by the application and executed when the affected page was viewed.

## Security Impact

Stored XSS can affect users who access a page containing the malicious stored content.

Depending on the application's functionality and security controls, successful XSS may allow an attacker to:

* Modify page content
* Display fraudulent forms or messages
* Perform actions in the victim's browser context
* Access data available to JavaScript within the affected application context
* Potentially abuse the victim's authenticated session

The exact impact depends on the application's design and security controls.

## Mitigation

Developers should:

* Apply context-appropriate output encoding to untrusted data.
* Treat user-supplied comments as data rather than executable markup.
* Sanitize HTML when HTML input is genuinely required.
* Use appropriate Content Security Policy protections as an additional defense.
* Apply secure session and cookie protections.

## Key Learnings

Through this lab, I practiced:

* Understanding Stored XSS
* Identifying a user-controlled input point
* Understanding how malicious input can be stored by an application
* Observing how stored content is returned in an HTML response
* Understanding the role of the browser in interpreting HTML and executing JavaScript
* Understanding why output encoding is important for preventing XSS

## Tools Used

* Burp Suite
* PortSwigger Web Security Academy
* Firefox

## Evidence

The screenshots in this directory document the practical testing performed during the lab.

> All testing was performed against the intentionally vulnerable PortSwigger Web Security Academy environment.
