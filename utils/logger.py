def log(msg):
    with open("log.txt","a") as f:
        f.write(msg+"\n")
