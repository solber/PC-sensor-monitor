import time
import requests
import json
 
# interval between each update
INTERVAL = 100000

# Web response code
STATUS_OK = 200

# IP which provides sensor values (json format)
sensor_endpoint_ip = '127.0.0.1'
# port
sensor_endpoint_port = '55555'

# Peripheral names
PERIPHERAL_GPU_NAME = 'GPU'

# Sensor names
SENSOR_TEMPERATURE = 'Temperature'

# Types
TYPE_CORE = 'Core'

def update():
	gpuInformations = getPeripheral(getSensorList(), PERIPHERAL_GPU_NAME)
	print(getTemperature(gpuInformations, TYPE_CORE)[0] + '°C')

# ----- Utility functions -----
def getSensorList():
	try:
		response = requests.get('http://' + sensor_endpoint_ip + ':' + sensor_endpoint_port)
	except:
		raise Exception('An error has encoured while querying the page.')
	if (response.status_code == STATUS_OK):
		try:
			jsonContent = json.loads(response.content)
		except:
			raise Exception('An error has encoured while converting page content to json.')
		return jsonContent
	else:
		raise Exception('Exit with wrong status code ' + response.status_code)
			
# ----- Sensor related functions -----

# print all sensors
def printSensor():
    jsonContent = getSensorList()
    for sensor in jsonContent:
        #print(sensor)
        print('- Sensor : ' + sensor['SensorName'])
        if (sensor['SensorUnit']):
            print('-' + sensor['SensorClass'] + ' : ' + sensor['SensorValue'] + ' ' + sensor['SensorUnit'])
        else:
            print('-' + sensor['SensorClass'] + ' : ' + sensor['SensorValue'])
        print('')

# Return related informations by peripheral name
def getPeripheral(sensors, peripheralName):
	if (peripheralName == PERIPHERAL_GPU_NAME):
		return getGPUPeripheral(sensors, peripheralName);

	return 'No peripheral named "' + peripheralName + '" found.'

# Return GPU related informationsé
def getGPUPeripheral(sensors, peripheralName):
	peripheral = []
	for sensor in sensors:
		if (peripheralName in sensor['SensorName']):
			peripheral.append(sensor)
	if (len(peripheral) > 0):
		return peripheral

	return None

# Return all temps from periphral information list
def getTemperature(peripheralInformations, informationType):
	temp = []
	for sensor in peripheralInformations:
		if (SENSOR_TEMPERATURE in sensor['SensorClass'] and informationType in sensor['SensorName']):
			temp.append(sensor['SensorValue'])
	if (len(temp) > 0):
		return temp

	return None	


# Start point
while True:
    update();
    time.sleep(INTERVAL);
