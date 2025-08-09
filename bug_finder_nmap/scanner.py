import nmap
import platform

def scan_ports(target):
    nm = nmap.PortScanner()
    args = "-sV"  # Service version detection
    if platform.system().lower().startswith("win"):
        args = "-sV --disable-arp-ping"  # Windows tweak

    nm.scan(target, arguments=args)
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                results.append({
                    "port": port,
                    "service": service,
                    "version": version
                })
    return results
