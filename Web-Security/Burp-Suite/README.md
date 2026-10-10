# Burp Suite – Username Enumeration via Different Responses

## Overview

This lab demonstrates how Burp Suite can be used to analyze HTTP requests and identify differences in application responses during authentication testing.

The objective was to identify a valid username by observing how the application responded to different username values.

## Lab Environment

* **Platform:** PortSwigger Web Security Academy
* **Lab:** Username enumeration via different responses
* **Tool:** Burp Suite
* **Target:** Intentionally vulnerable Web Security Academy application
* **Attack Tool:** Burp Suite Intruder
* **Request Analysis:** Burp Suite Repeater

## Objective

The objective of the lab was to determine whether the application's login functionality revealed useful information through differences in HTTP responses.

The testing focused on:

* Intercepting the login request
* Identifying the username parameter
* Using Burp Suite Intruder to test multiple username values
* Comparing HTTP response status codes and response lengths
* Using Burp Suite Repeater to manually inspect individual requests and responses

## Methodology

### 1. Capturing the Login Request

The login request was captured and inspected in Burp Suite.

The request contained the following parameters:

```text
username=academico
password=5sda5
```

This allowed the authentication request to be analyzed and modified during testing.

### 2. Using Burp Suite Intruder

The username parameter was selected as the position for the Intruder attack.

A list of candidate usernames was supplied to test how the application responded to different values.

The Intruder results showed differences in HTTP response characteristics, including:

* HTTP status codes
* Response length
* Response behavior

These differences provided an indication that certain usernames were being handled differently by the application.

![Burp Suite Intruder results](screenshots/burp-intruder.png)

### 3. Analyzing the Response

After identifying an interesting response, the request was further examined using Burp Suite Repeater.

Repeater allowed the request to be manually modified and resent while inspecting the resulting HTTP response.

![Burp Suite Repeater analysis](screenshots/burp-repeater.png)

The response contained an authentication error message, demonstrating how response content could provide useful information during username enumeration.

## Result

The lab was successfully completed.

Burp Suite Intruder was used to automate testing of multiple username values, while Repeater was used to manually inspect and verify individual requests and responses.

The differences in application responses demonstrated how inconsistent authentication responses can potentially allow username enumeration.

## Security Impact

Username enumeration can provide attackers with valid account information.

If an application responds differently for valid and invalid usernames, an attacker may be able to determine which usernames exist.

This information can then be used as a starting point for further authentication attacks.

## Mitigation

Applications should avoid revealing whether a username exists.

Recommended protections include:

* Use consistent error messages for invalid usernames and passwords.
* Maintain similar response behavior for valid and invalid authentication attempts.
* Implement rate limiting and account protection mechanisms.
* Monitor repeated authentication attempts.
* Avoid exposing unnecessary authentication details in HTTP responses.

## Key Learnings

Through this lab, I practiced:

* Intercepting HTTP authentication requests with Burp Suite
* Understanding HTTP request parameters
* Using Burp Suite Intruder for automated testing
* Comparing HTTP status codes and response lengths
* Using Burp Suite Repeater for manual request analysis
* Understanding how inconsistent authentication responses can lead to username enumeration

## Tools Used

* Burp Suite
* PortSwigger Web Security Academy
* Firefox
* HTTP/2

## Evidence

The screenshots included in this directory document the practical testing performed during the lab.

> All testing was performed against the intentionally vulnerable PortSwigger Web Security Academy lab environment.
