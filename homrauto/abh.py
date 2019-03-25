#!/usr/bin/env python
import cayenne.client
import logging
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT,initial=1)

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "f0fbb820-2157-11e8-aeac-8375e928efd4"
MQTT_PASSWORD  = "44e72dda405b00be56ed7bbdd3b504061e10aa72"
MQTT_CLIENT_ID = "4eff88f0-4b2a-11e9-a6b5-e30ec853fbf2"


# The callback for when a message is received from Cayenne.
def on_message(message):
	#print("message received: " + str(message))
	# If there is an error processing the message return an error string, otherwise return nothing.
	if msg["value"] == "1":
		GPIO.output(14, GPIO.LOW)
	else:
		GPIO.output(14, GPIO.HIGH)
	print(message)

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)
client.loop_forever()


