import cayenne.client
import logging
from gpiozero import LED as GPIO

pins = {
			'2': 2,
			'3': 3,
			'4': 4, 
			'5': 5,
			'6': 6,
			'7': 7,
			'8': 8,
			'9': 9,
			'10': 10,
			'11': 11,
			'12': 19,
			'13': 26
			}

def initGPIO():
	for p in pins:
		pins[str(p)] = GPIO(pins[p], active_high=False)
	

def configureCayenne(MQTT_USRNAME="", MQTT_PASS="", MQTT_CLNT_ID=""):
	client = cayenne.client.CayenneMQTTClient()
	client.on_message = messageReceived
	client.begin(MQTT_USRNAME, MQTT_PASS, MQTT_CLNT_ID)
	return client

def messageReceived(message):
	if message.value == '1':
		pins[str(message.channel)].on()
	else:
		pins[str(message.channel)].off()



if __name__ == "__main__":
	initGPIO()
	client = configureCayenne("f0fbb820-2157-11e8-aeac-8375e928efd4", "44e72dda405b00be56ed7bbdd3b504061e10aa72", "4eff88f0-4b2a-11e9-a6b5-e30ec853fbf2")
	client.loop_forever()