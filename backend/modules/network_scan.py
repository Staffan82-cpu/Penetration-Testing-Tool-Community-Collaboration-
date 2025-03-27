import nmap

def scan_network(ip_range):
    nm = nmap.PortScanner()
    nm.scan(ip_range, arguments="-sn")
    devices = [{"IP": host, "MAC": nm[host]['addresses'].get('mac', 'Unknown')} for host in nm.all_hosts()]
    return devices
