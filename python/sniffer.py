#Imports
from requests import get
from json import loads
import globalVars
import inputManager
from os import system

# Sensor server port
SENSOR_SERVER_PORT = 55555

# Server status
STATUS_OK = 200

# ProgressBar Values
MARGIN_X = 13
MARGIN_Y = 15
MARGIN_Y_BAR = 17
PADDING = 2
BAR_SIZE = 3
SPACING_BAR = 1

MAX_IP_CHECK = 100

# end const
index_ip = 0
connected = False
ip_written = False
ips_to_try_first = []

draw = None


def sniff_ip(IP):
	try:
		response = get('http://' + str(IP), verify=False, timeout=0.5)
	except:
		return False
	if response.status_code == STATUS_OK:
		try:
			json_content = loads(response.content)
			global connected
			connected = True
			return True
		except:
			return False

	return False


def get_ip_to_sniff(ip):
	splited_ip = ip.split('.')
	sniffed_ip_base = str(splited_ip[0] + '.' + splited_ip[1] + '.' + splited_ip[2])
	return sniffed_ip_base + '.' + str(index_ip) + ':' + str(SENSOR_SERVER_PORT)


def draw_progress_bar():
	draw.rectangle((MARGIN_X, MARGIN_Y, globalVars.width - MARGIN_X, globalVars.height - MARGIN_Y), outline=255, fill=0)

	if index_ip >= 0:
		draw.rectangle((MARGIN_X + PADDING, MARGIN_Y_BAR, MARGIN_X + PADDING + BAR_SIZE, globalVars.height - MARGIN_Y_BAR), outline=255, fill=1)
		draw.rectangle((MARGIN_X + SPACING_BAR * index_ip, MARGIN_Y_BAR, MARGIN_X + BAR_SIZE + SPACING_BAR, globalVars.height - MARGIN_Y_BAR), outline=255, fill=1)


def get_ip_to_try_first():
	from fileManager import get_ips_to_try
	global first_time
	first_time = True
	global ips_to_try_first
	ips_to_try_first = get_ips_to_try()



def render_sniffer():
	# fetch ips from config/ips.list. those ips are last known working ips and will be sniffed first
	get_ip_to_try_first()
	global ip_to_sniff
	global first_time
	global index_ip
	global ip_written
	global draw
	while connected is False:
		with globalVars.canvas(globalVars.device) as draw:
			if not connected:
				ip_to_sniff = ''
				for (ip) in ips_to_try_first:
					if sniff_ip(ip):
						ip_to_sniff = ip
				if not connected:
					ip = globalVars.get_ip()
					ip_to_sniff = get_ip_to_sniff(ip)

					if sniff_ip(ip_to_sniff) is False and index_ip < MAX_IP_CHECK:
						index_ip = index_ip + 1
						draw_progress_bar()

			if index_ip < MAX_IP_CHECK:
				globalVars.libAdvDisplay.draw_centered_text('Searching for server', globalVars.top, 255, draw)
				globalVars.libAdvDisplay.draw_centered_text(ip_to_sniff, globalVars.height - 12, 255, draw)
			elif index_ip >= MAX_IP_CHECK and connected is False:
				globalVars.libAdvDisplay.draw_centered_text('No server found', globalVars.top, 255, draw)
				globalVars.libAdvDisplay.draw_centered_text('Press <key1> to type', globalVars.top + 15, 255, draw)
				globalVars.libAdvDisplay.draw_centered_text('an IP address or', globalVars.top + 24, 255, draw)
				globalVars.libAdvDisplay.draw_centered_text('<key2> to retry', globalVars.top + 33, 255, draw)
				if inputManager.key1_pressed():
					system('python manual_ip_selection.py 1')
				if inputManager.key2_pressed():
					index_ip = 0
	if connected:
		if ip_written is False:
			from fileManager import write_working_ip
			ip_written = write_working_ip(ip_to_sniff)
		return ip_to_sniff
	else:
		return None
