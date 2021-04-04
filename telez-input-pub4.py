import paho.mqtt.client as mqtt
import time

print("This is a publisher client 4")
topic = input("Published topic: ")
payload = input("Published payload: ")

def on_connect(client, userdata, flags, rc):
    print(" ")
    print("Connected with result code "+str(rc))  

client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)

time.sleep(1)
while True:
    client.loop()
    client.publish(topic, payload)
    time.sleep(1)
