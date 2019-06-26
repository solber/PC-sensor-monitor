#Imports
from requests import get
from json import loads
import globalVars
import inputManager
from os import system
from re import compile, findall

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

MAX_IP_CHECK = 45

# end const
indexIp = 0
connected = False
ipWritten = False
ipsToTryFirst = []


def sniff_ip(IP):
	try:
		response = get('http://' + str(IP), verify=False, timeout=0.5)
	except:
		return False
	if response.status_code == STATUS_OK:
		try:
			jsonContent = loads(response.content)
			global connected
			connected = True
			return True
		except:
			return False

	return False


def get_ip_to_sniff(Ip):
		splitedIp = Ip.split('.')
		sniffedIpBase = str(splitedIp[0] + '.' + splitedIp[1] + '.' + splitedIp[2])
		return sniffedIpBase + '.' + str(indexIp) + ':' + str(SENSOR_SERVER_PORT)


def draw_progress_bar():
	draw.rectangle((MARGIN_X, MARGIN_Y, globalVars.width - MARGIN_X, globalVars.height - MARGIN_Y), outline=255, fill=0)

	if indexIp >= 0:
		draw.rectangle((MARGIN_X + PADDING, MARGIN_Y_BAR, MARGIN_X + PADDING + BAR_SIZE, globalVars.height - MARGIN_Y_BAR), outline=255, fill=1)
		draw.rectangle((MARGIN_X + SPACING_BAR * indexIp, MARGIN_Y_BAR, MARGIN_X + BAR_SIZE + SPACING_BAR, globalVars.height - MARGIN_Y_BAR), outline=255, fill=1)


def get_ip_to_try_first():
	f = open("config/ips.list", "r")
	if f.mode == 'r':
		contents = f.read()
		pattern = compile(r'<last_ip>(.*)</last_ip>')

		global firstTime
		firstTime = True
		global ipsToTryFirst
		ipsToTryFirst = findall(pattern, contents)
		f.close()

# fetch ips from config/ips.list. those ips are last known working ips and will be sniffed first
get_ip_to_try_first()

while True:
	with globalVars.canvas(globalVars.device) as draw:
		if not connected:
			ipToSniff = ''
			for (ip) in ipsToTryFirst:
				if sniff_ip(ip):
					ipToSniff = ip
			if not connected:
				Ip = globalVars.get_ip()
				ipToSniff = get_ip_to_sniff(Ip)

				if sniff_ip(ipToSniff) is False and indexIp < MAX_IP_CHECK:
					indexIp = indexIp + 1
					draw_progress_bar()
		# is connected
		else:
			globalVars.libAdvDisplay.draw_centered_text('Connected', globalVars.top + 27, 255, draw)

			if ipWritten is False:
				f = open("config/ips.list", "r")
				if f.mode == 'r':
					contents = f.read()
					pattern = compile(r'<last_ip>(.*)</last_ip>')

					firstTime = True
					for (ip) in findall(pattern, contents):
						firstTime = False
						if ip != ipToSniff:
							f = open("config/ips.list", "a+")
							f.write("<last_ip>" + str(ipToSniff) + "</last_ip>\r\n")
							ipWritten = True
					if firstTime:
						f = open("config/ips.list", "w+")
						f.write("<last_ip>" + str(ipToSniff) + "</last_ip>\r\n")
					f.close()

		if indexIp < MAX_IP_CHECK:
			globalVars.libAdvDisplay.draw_centered_text('Searching for server', globalVars.top, 255, draw)
			globalVars.libAdvDisplay.draw_centered_text(ipToSniff, globalVars.height - 12, 255, draw)
		elif indexIp >= MAX_IP_CHECK and connected is False:
			globalVars.libAdvDisplay.draw_centered_text('No server found', globalVars.top, 255, draw)
			globalVars.libAdvDisplay.draw_centered_text('Press <key1> to type', globalVars.top + 15, 255, draw)
			globalVars.libAdvDisplay.draw_centered_text('an IP address or', globalVars.top + 24, 255, draw)
			globalVars.libAdvDisplay.draw_centered_text('<key2> to retry', globalVars.top + 33, 255, draw)
			if inputManager.key1_pressed():
				system('python manual_ip_selection.py 1')
			if inputManager.key2_pressed():
				indexIp = 0

GPIO.cleanup()
