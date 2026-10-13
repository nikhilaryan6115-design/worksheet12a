with open("demo-log.log","r") as file :
    for line in file:
        if "ERROR" in line:
            with open("error.log",'a') as f :
                f.write(line)
        elif "INFO" in line
            with open("info.log",'a') as f :
                f.write(line)