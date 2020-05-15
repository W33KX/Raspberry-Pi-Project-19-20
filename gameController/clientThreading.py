import paho.mqtt.client as paho
from enum import Enum

#deze functie moet nog aangepast worden naarmate de client is opgebouwd.
def MQTT(mqttmsg):
  def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed!")

  def on_message(client, userdata, msg):
    mqttmsg = str(msg.payload)
    print(mqttmsg)
    
  
  def on_publish(client, userdata, mid):
    print("mid: " + str(mid))

  client = paho.Client(client_id="clientId-ejELTYmyEX", clean_session=True, userdata=None, protocol=paho.MQTTv31)
  client.on_subscribe= on_subscribe
  client.on_message= on_message
  client.on_publish= on_publish

  client.connect("broker.mqttdashboard.com", port=1883, keepalive=60)
  client.subscribe("testtopic/test", qos=1)
  
  client.loop_start()

  if mqttmsg:
      (rc, mid) = client.publish("testtopic/test", mqttmsg)