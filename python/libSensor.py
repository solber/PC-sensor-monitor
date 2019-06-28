# only for dev purpose, those will be removed and imported
# in the main program, so we will optimise loading times
from requests import get
from json import loads
from time import sleep

# will be moved in another main imported file
# Server status
STATUS_OK = 200
# same for IP this is a dev value
IP = '192.168.0.11:55555'

sensors = None

#CONST
SENSOR_CLASS = 'SensorClass'
SENSOR_NAME = 'SensorName'
SENSOR_VALUE = 'SensorValue'
SENSOR_UNIT = 'SensorUnit'

#TEMP
CPU_TCTL_SENSOR_NAME = 'CPU'
CPU_IDLE_SENSOR_NAME = 'CPU'
CPU_TEMP_UNIT = 'C'
#VOLTAGE
CPU_VOLTAGE = 'VID'
CPU_VOLTAGE_SENSOR_CLASS = 'CPU'
#CLOCK
CPU_CLOCK = 'Clock'
CPU_CLOCK_SENSOR_CLASS = 'CPU'
#LOAD
CPU_LOAD = 'Usage'
CPU_LOAD_SENSOR_CLASS_NAME = 'CPU'

#CPU
INFO_CPU_TEMP = 1
INFO_CPU_VOLTAGE = 2
INFO_CPU_CLOCK = 3
INFO_CPU_LOAD = 4


def get_sensors():
    try:
        global sensors
        #if sensors:
            #return sensors
        #else:
        response = get('http://' + str(IP))
    except:
        raise Exception('Unable to request http://' + str(IP))
    if response.status_code == STATUS_OK:
        try:
            jsonContent = loads(response.content)
            sensors = jsonContent
            return jsonContent
        except:
            raise Exception('Unable parse page content')


def get_cpu_info(infoType):
    get_sensors()

    global sensors
    res = []
    for component in sensors:
        if infoType == INFO_CPU_TEMP:
            if CPU_IDLE_SENSOR_NAME in component[SENSOR_NAME] and CPU_TEMP_UNIT in component[SENSOR_UNIT]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
        elif infoType == INFO_CPU_VOLTAGE:
            if CPU_VOLTAGE in component[SENSOR_NAME] and CPU_VOLTAGE_SENSOR_CLASS in component[SENSOR_CLASS]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
        elif infoType == INFO_CPU_CLOCK:
            if CPU_CLOCK in component[SENSOR_NAME] and CPU_CLOCK_SENSOR_CLASS in component[SENSOR_CLASS]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
        elif infoType == INFO_CPU_LOAD:
            if CPU_LOAD in component[SENSOR_NAME] and CPU_LOAD_SENSOR_CLASS_NAME in component[SENSOR_CLASS]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})

    return res

