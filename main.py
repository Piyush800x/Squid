import os 
from time import sleep


# PROXY SETUP 
os.system("apt update -y")
os.system("apt install squid apache2-utils -y")
os.system("wget https://raw.githubusercontent.com/Piyush800x/Squid/master/squid.conf")
os.system("systemctl start squid")
os.system("systemctl enable squid")
# os.system("rm -r /etc/squid/squid.conf")
# os.system("mv squid.conf /etc/squid/") 
print("------------------------------SET PROXY PASSWORD, DEFAULT USERNAME: proxy -----------------------------")
sleep(1)
os.system("htpasswd -c /etc/squid/passwd proxy")
sleep(2)
os.system("iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT")
os.system("iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT")
os.system("iptables -I INPUT -p tcp -m tcp --dport 3128 -j ACCEPT")
os.system("iptables -I INPUT -p tcp -m tcp --dport 5515 -j ACCEPT")
os.system("iptables -I INPUT -p tcp -m tcp --dport 8080 -j ACCEPT")
os.system("iptables-save")
sleep(1)
os.system("rm -r /etc/squid/squid.conf")
os.system("mv squid.conf /etc/squid/") 
os.system("service squid restart")

# OPENVPN SETUP
os.system("apt install openvpn -y")
os.system("wget https://raw.githubusercontent.com/Piyush800x/Squid/master/in-aes-256-cbc-tcp-ip.ovpn")
sleep(2)
os.system("openvpn --config in-aes-256-cbc-tcp-ip.ovpn")