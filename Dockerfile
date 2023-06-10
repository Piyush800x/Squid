FROM ubuntu

RUN apt-get update -y
RUN apt install wget python3 git -y

RUN git clone https://github.com/Piyush800x/Squid.git
RUN cd Squid

CMD ["python3", "Squid/main.py"]