import os

os.system('echo "250   vpnbypass" >> /etc/iproute2/rt_tables')

os.system("ip route add 168.63.129.16 via 10.0.0.1 || true")
os.system("ip route add 169.254.169.254 via 10.0.0.1 || true")

os.system("ip rule add table vpnbypass from 10.0.0.0/16")
os.system("ip rule add table vpnbypass to 10.0.0.0/16")
os.system("ip rule add table vpnbypass from 10.0.0.1/16")
os.system("ip rule add table vpnbypass to 10.0.0.1/16")
os.system("ip rule add table vpnbypass to 169.254.169.254")
os.system("ip rule add table vpnbypass to 168.63.129.16")
os.system("ip route add table vpnbypass to 10.0.0.0/16 dev ens4")
os.system("ip route add table vpnbypass default via 10.0.0.1 dev ens4")
