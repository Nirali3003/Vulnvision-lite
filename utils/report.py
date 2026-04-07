from datetime import datetime

def generate_report(target, ports, headers):
    with open("report.txt","w") as f:
        f.write("Report\n")
        f.write(str(datetime.now())+"\n")

        f.write("Open Ports:\n")
        for p in ports:
            f.write(str(p)+"\n")

        f.write("Missing Headers:\n")
        for h in headers:
            f.write(h+"\n")
