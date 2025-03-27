import nmap

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-Pn -sV")
    return [{"port": p, "service": nm[target]["tcp"][p]["name"]} for p in nm[target]["tcp"]]
