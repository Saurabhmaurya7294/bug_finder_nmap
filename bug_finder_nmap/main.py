from .scanner import scan_ports
from .vuln_checker import check_vulnerabilities

from utils import print_banner

def main():
    print_banner()
    target = input("Enter target IP or domain: ").strip()
    
    print("[*] Scanning target...")
    services = scan_ports(target)

    print("\n[*] Checking vulnerabilities...")
    for svc in services:
        if svc["version"]:
            vulns = check_vulnerabilities(svc["service"], svc["version"])
            if vulns:
                print(f"[!] {svc['service']} {svc['version']} on port {svc['port']} has CVEs: {vulns}")
        else:
            print(f"[-] No version info for port {svc['port']}")

if __name__ == "__main__":
    main()
