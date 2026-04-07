from scanner.port_scanner import scan_ports
from scanner.header_checker import check_headers
from utils.report import generate_report
from utils.logger import log

def main():
    print("VulnVision Lite Scanner")

    target = input("Enter target: ")
    url = "http://" + target

    log("Scan started")

    ports = scan_ports(target)
    headers = check_headers(url)

    generate_report(target, ports, headers)

    log("Scan completed")

if __name__ == "__main__":
    main()
