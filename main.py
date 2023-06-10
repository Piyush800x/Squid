import os 
from time import sleep


# PROXY SETUP 
os.system("sudo apt update -y")
os.system("sudo apt install squid apache2-utils -y")
os.system("wget https://raw.githubusercontent.com/Piyush800x/Squid/master/squid.conf")
os.system("sudo systemctl start squid")
os.system("sudo systemctl enable squid")
# os.system("rm -r /etc/squid/squid.conf")
# os.system("mv squid.conf /etc/squid/") 
print("------------------------------SET PROXY PASSWORD, DEFAULT USERNAME: proxy -----------------------------")
sleep(1)
os.system("sudo htpasswd -c /etc/squid/passwd proxy")
sleep(2)
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 3128 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 5515 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 8080 -j ACCEPT")
os.system("sudo iptables-save")
sleep(1)
os.system("sudo rm -r /etc/squid/squid.conf")
os.system("sudo mv squid.conf /etc/squid/") 
os.system("sudo service squid restart")

# OPENVPN SETUP
os.system("sudo apt install openvpn -y")
os.system("wget https://raw.githubusercontent.com/Piyush800x/Squid/master/in-aes-256-cbc-tcp-ip.ovpn")
sleep(2)
os.system("sudo openvpn --config in-aes-256-cbc-tcp-ip.ovpn")