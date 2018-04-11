FROM python:latest

RUN apt-get update -y && \
    apt-get install -y libmosquitto-dev python3-pip && \
    rm -rf /var/lib/apt /var/lib/dpkg

RUN pip3 install paho-mqtt && \
    rm -rf /root/.cache/

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt && \
    rm -rf /root/.cache/

COPY mqtt-blinkt.py /app/

CMD ["/app/mqtt-blinkt.py"]
