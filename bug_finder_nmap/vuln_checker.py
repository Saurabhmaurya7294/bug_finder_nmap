# bug_finder_nmap/vuln_checker.py

# Simulated vulnerability database
KNOWN_VULNERABILITIES = {
    21: "FTP service - Check for anonymous login",
    22: "SSH service - Check for weak credentials",
    80: "HTTP service - Possible outdated web server",
    443: "HTTPS service - Check SSL certificate issues",
    3306: "MySQL database - Check for weak root password",
    3389: "RDP service - Check for BlueKeep vulnerability"
}

def check_vulnerabilities(ip, ports):
    """
    Checks the given IP and list of open ports against a known vulnerability list.
    :param ip: Target IP address
    :param ports: List of open port numbers
    :return: List of found vulnerabilities
    """
    print(f"[+] Checking vulnerabilities for {ip}...")
    found = []

    for port in ports:
        if port in KNOWN_VULNERABILITIES:
            found.append({
                "port": port,
                "issue": KNOWN_VULNERABILITIES[port]
            })

    if found:
        print("[!] Vulnerabilities found:")
        for vuln in found:
            print(f" - Port {vuln['port']}: {vuln['issue']}")
    else:
        print("[+] No known vulnerabilities found.")

    return found
