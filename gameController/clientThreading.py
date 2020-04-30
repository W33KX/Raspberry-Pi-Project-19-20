import paho.mqtt.client as paho
from enum import Enum
from main import getGameManagerInstance
from user import User
from threading import Thread

#deze functie moet nog aangepast worden naarmate de client is opgebouwd.
def MQTT():
  def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed!")

  def on_message(client, userdata, msg):
    print(msg.topic+"  "+str(msg.payload))

  client = paho.Client(client_id="clientId-ejELTYmyEX", clean_session=True, userdata=None, protocol=paho.MQTTv31)
  client.on_subscribe= on_subscribe
  client.on_message= on_message

  client.connect("broker.mqttdashboard.com", port=1883, keepalive=60)
  client.subscribe("testtopic/test", qos=1)
  
  user = user.user
  gameManager = main.getGameManagerInstance()

  client.loop_forever()