import os
from time import sleep
import platform
import subprocess
import distro

distro = distro.id()
if "debian" in distro or "ubuntu" in distro:
    PACKAGE_MANAGER = "apt-get"
elif "fedora" in distro or "red hat" in distro:
    PACKAGE_MANAGER = "dnf"
else:
    print("Unsupported Linux distribution. Please install the required dependencies manually.")
    sys.exit(1)


def squid_setup(username: str):
    # SQUID PROXY SETUP
    os.system(f"sudo {PACKAGE_MANAGER} update -y")
    # os.system("sudo yum update -y")
    if PACKAGE_MANAGER == "apt-get":
        os.system(f"sudo {PACKAGE_MANAGER} install squid apache2-utils -y")
        os.system(
            "wget https://raw.githubusercontent.com/Piyush800x/Squid/master/squid_ubuntu.conf")
        os.system("sudo rm -r /etc/squid/squid.conf")
        os.system("sudo mv squid_ubuntu.conf squid.conf")
        os.system("sudo mv squid.conf /etc/squid/")
    if PACKAGE_MANAGER == "dnf":
        os.system(f"sudo {PACKAGE_MANAGER} install squid httpd -y")
        os.system(
            "wget https://raw.githubusercontent.com/Piyush800x/Squid/master/squid_rhel.conf")
        os.system("sudo rm -r /etc/squid/squid.conf")
        os.system("sudo mv squid_rhel.conf squid.conf")
        os.system("sudo mv squid.conf /etc/squid/")
    # os.system("sudo yum install squid httpd -y")
    # os.system(
    #     "wget https://raw.githubusercontent.com/Piyush800x/Squid/master/squid.conf")
    os.system("sudo systemctl start squid")
    os.system("sudo systemctl enable squid")
    print(
        f"------------------------------SET PROXY PASSWORD, username: {username} -----------------------------")
    sleep(1)
    os.system(f"sudo htpasswd -c /etc/squid/passwd {username}")
    del username
    sleep(1)
    # os.system("sudo rm -r /etc/squid/squid.conf")
    # os.system("sudo mv squid.conf /etc/squid/")
    if PACKAGE_MANAGER == "apt-get":
        os.system("sudo service squid restart")
    if PACKAGE_MANAGER == "dnf":
        os.system("sudo systemctl restart squid")


def networking_setup():
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 3128 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 5515 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 8080 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 123 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 143 -j ACCEPT")
    os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 1194 -j ACCEPT")
    os.system("sudo iptables-save")
# os.system("sudo systemctl restart squid")


def openvpn_setup():
    # OPENVPN SETUP
    sleep(2)
    os.system("sudo apt install openvpn -y")
    # os.system("sudo yum install openvpn -y")
    os.system("sudo apt install net-tools -y")
    # os.system("sudo yum install net-tools -y")


def take_input() -> [int, str]:
    print("1. SQUID PROXY")
    print("2. SQUID WITH OPENVPN CLIENT")
    try:
        user_input = int(input("==> "))
        print("Enter proxy username: ")
        username = input("==> ")
        if user_input > 2:
            print("Ahh! You must choose between 1 and 2")
            return take_input()
        else:
            return user_input, username
    except ValueError:
        print("Ahh! You must choose between 1 and 2")
        return take_input()


def main():
    print("###############################################################################")
    print("FAST SQUID PROXY INSTALLER WITH BASIC AUTH")
    print("Author: Piyush Paul")
    print("###############################################################################")
    print("-------------------------------------------------------------------------------")
    inputs = take_input()
    user_input, username = inputs[0], inputs[1]
    squid_setup(username)
    networking_setup()
    if user_input == 2:
        openvpn_setup()


if __name__ == '__main__':
    main()
