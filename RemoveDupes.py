# How to use: name the csv export "bitwared_export.csv" and move it to your desktop, then run
save=None
with open("%USERPROFILE%/Desktop/bitwarden_export.csv", "r") as csvFile:
    with open("fix.txt", "w") as fixedFile:
        while True:
            dataN = csvFile.readline().strip()
            if save != dataN:
                fixedFile.write(dataN+"\n")
            save = dataN
            if dataN=="":
                break
fixedFile.close()
csvFile.close()