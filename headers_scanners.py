import urllib.request
import urllib.error
url = "https://example.com"
print("=== HTTP SECURITY HEADERS SCANNER ===")
try:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "SecurityHeadersScanner/1.0"}
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        print("Website:", url)
        print("HTTP Status:", response.status)
        print("\nHTTP Headers:")
        for header, value in response.headers.items():
            print(f"{header}:{value}")
    security_headers = [
        "Content-Security-policy",
        "Strict-Transport-security",
        "X-Frame-Options",
        "X-content-Type-Option",
        "Referrer-Policy"
    ]
    print("\n=== SECURITY HEADERS CHECK ===")
    for header in security_headers:
        if header in response.headers:
            print(f"[PRESENT] {header}")
        else:
            print(f"[MISSING] {header}")
    present_count = sum(
        1 for header in security_headers
        if header in response.headers
    )
    total_headers = len(security_headers)
    score = (present_count / total_headers) * 100
    print("\n=== SECURITY SCORE ===")
    print(f"Security Headers Score: {score:.0f}/100")
    print(f"Present Headers: {present_count}")
    print(f"Missing Headers: {total_headers - present_count}")
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 25:
        grade = "D"
    else:
        grade = "F"
    print(f"Security Grade: {grade}")
except urllib.error.HTTPError as error:
    print("HTTP Error:", error.code)
    print("Server rejected the request.")
except urllib.error.URLError as error:
    print("Connection Error:", error.reason)