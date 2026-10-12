# HTTP Security Headers Scanner
## Project Overview
A Python-based cybersecurity tool that analyzes HTTP response headers to identify missing security headers and calculate a basic security score.
## Features
- Fetches HTTP response headers
- Checks five important security headers
- Identifies present and missing headers
- Calculates a security grade from A to F
- Handles HTTP and connection errors
- ##
- Security Headers Checked
1. Content-security-policy
2. Strict-Transport-Security
3. X-Frame-Options
4. X-Content-Type-Options
5. Referrer-Policy
## Technologies Used
- Python
- Urllib.request
- Urllib.error
- Visual Studio Code
- GitHub
## How To Run
1. Download the repository.
2. Open the project folder in VS code.
3. Open the terminal.
4. Run.
``` bash
python headers_scanners.py
```
## Sample Output
```text
HTTP Status: 200
=== SECURITY HEADERS CHECK ===
[MISSING] Content-security-policy
[MISSING] Strict-Transport-Security
[MISSING] X-Frame-Options
[MISSING] X-Content-Type-Options
[MISSING] Referre-policy
===SECURITY SCORE ===
Security Headers Score: 0/100
Present Headers: 0
Missing Headers: 5
Security Grade: F
```
## Cybersecurity Skills Demonstrated
- Web security fundmentals
- HTTP protocol analysis
- Security header inspection
- Python scripting
- Basic security assesment
- Error handling
## Disclaimer
This project is for educational and authorized security testing. The score reflects the presence of five selected headers, not a complete websites security assesment.
