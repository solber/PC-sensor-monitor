# only for dev purpose, those will be removed and imported
# in the main program, so we will optimise loading times
from requests import get
from json import loads
from time import sleep

# will be moved in another main imported file
# Server status
STATUS_OK = 200

IP = None

sensors = None

CPU_NAME = 'CPU'
#CONST
SENSOR_CLASS = 'SensorClass'
SENSOR_NAME = 'SensorName'
SENSOR_VALUE = 'SensorValue'
SENSOR_UNIT = 'SensorUnit'

#TEMP
CPU_PACKAGE_SENSOR_NAME = 'Package'
CPU_IDLE_SENSOR_NAME = 'CPU (Tdie)'
CPU_TEMP_UNIT = 'C'

#VOLTAGE
CPU_VOLTAGE_UNIT = 'V'
CPU_VOLTAGE_NAME = 'Voltage'

#CLOCK
CPU_CLOCK_UNIT = 'MHz'
CPU_CLOCK_CORE_NAME = 'Core'
CPU_CLOCK_NAME = 'Clock'

#LOAD
CPU_LOAD_UNIT = '%'
CPU_TOTAL_NAME = 'Total'
CPU_USAGE_NAME = 'Usage'

#CPU
INFO_CPU_TEMP = 1
INFO_CPU_VOLTAGE = 2
INFO_CPU_CLOCK = 3
INFO_CPU_LOAD = 4


def set_ip(ip):
    global IP
    IP = ip


def get_sensors():
    try:
        global sensors
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
            if component[SENSOR_UNIT] is not None and CPU_TEMP_UNIT in component[SENSOR_UNIT]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
        elif infoType == INFO_CPU_CLOCK:
            if component[SENSOR_UNIT] is not None and CPU_CLOCK_UNIT in component[SENSOR_UNIT]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
        elif infoType == INFO_CPU_LOAD:
            if component[SENSOR_UNIT] is not None and CPU_LOAD_UNIT in component[SENSOR_UNIT]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
        elif infoType == INFO_CPU_VOLTAGE:
            if component[SENSOR_UNIT] is not None and CPU_VOLTAGE_UNIT in component[SENSOR_UNIT]:
                res.append({SENSOR_NAME: component[SENSOR_NAME],
                            SENSOR_VALUE: component[SENSOR_VALUE],
                            SENSOR_UNIT: component[SENSOR_UNIT]})
    return res


def convert_to_float(val):
    return float(val.replace(',', '.'))


def get_cpu_package_temp():
    info = get_cpu_info(INFO_CPU_TEMP)
    for component in info:
        if CPU_IDLE_SENSOR_NAME in component[SENSOR_NAME]: return convert_to_float(component[SENSOR_VALUE])
        if CPU_PACKAGE_SENSOR_NAME in component[SENSOR_NAME]: return convert_to_float(component[SENSOR_VALUE])
    return 0


def get_cpu_clock_total_usage():
    info = get_cpu_info(INFO_CPU_CLOCK)
    sum = 0
    totalcorecount = 0
    for component in info:
        if CPU_CLOCK_CORE_NAME in component[SENSOR_NAME] and CPU_CLOCK_NAME in component[SENSOR_NAME]:
            sum = sum + round(convert_to_float(component[SENSOR_VALUE].replace(',', '.')))
            totalcorecount = totalcorecount + 1
        if sum != 0:
            return sum / totalcorecount
    return 0


def get_cpu_total_load():
    info = get_cpu_info(INFO_CPU_LOAD)
    for component in info:
        if CPU_NAME in component[SENSOR_NAME] and CPU_TOTAL_NAME in component[SENSOR_NAME] and CPU_USAGE_NAME in component[SENSOR_NAME]:
            return convert_to_float(component[SENSOR_VALUE])
    return 0


def get_cpu_voltage():
    info = get_cpu_info(INFO_CPU_VOLTAGE)
    for component in info:
        if CPU_NAME in component[SENSOR_NAME] and CPU_VOLTAGE_NAME in component[SENSOR_NAME]:
            return convert_to_float(component[SENSOR_VALUE])
    return 0

# some example code
#print(get_cpu_package_temp())
#print(get_cpu_clock_total_usage())
#print(get_cpu_total_load())
#print(get_cpu_voltage())
