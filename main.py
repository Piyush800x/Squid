import os 

os.system("sudo apt update -y")
os.system("sudo apt isnatll squid apache2-utils -y")
os.system("wget https://raw.githubusercontent.com/Piyush800x/Squid/master/squid.conf")
os.system("rm -r /etc/squid/squid.conf")
os.system("mv squid.conf /etc/squid/") 
print("------------------------------SET PROXY PASSWORD-----------------------------")
usr = input("Enter username: ")
os.system(f"htpasswd -c /etc/squid/passwd {usr}")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 3128 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 5515 -j ACCEPT")
os.system("sudo iptables -I INPUT -p tcp -m tcp --dport 8080 -j ACCEPT")
os.system("sudo iptables-save")
os.system("sudo systemctl start squid")
os.system("sudo systemctl enable squid")
os.system("sudo service squid restart")
