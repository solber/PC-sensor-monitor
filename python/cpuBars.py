import globalVars
import libSensor
from time import sleep

font5L = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 10)
font3G0 = globalVars.ImageFont.truetype("./lucidaSTWB.ttf", 14)
font3G1 = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 7)

draw = None

def scale_value(actualValue, minValue, maxValue, graphLength): # Used to match a sensor value range with a graph length
	if actualValue >= maxValue:
		scaledValue = graphLength
	else:
		scaledValue = (graphLength * actualValue) / (maxValue - minValue)
	return int(scaledValue)


def draw_3graph(title, subtitle, position, (actualValue, minValue, maxValue)): # Designed to draw 3 graph on top of each other

	graph3Y = [0, 22, 44]
	g3TextY = [2, 24, 46]
	titleSize = font3G0.getsize(title)
	
	draw.rectangle((0, graph3Y[position], titleSize[0] + 6, graph3Y[position] + 18), outline=255, fill=1) 		# Device name area
	draw.text((2,g3TextY[position]), title, font=font3G0, fill=0) 												# Device name
	draw.text((titleSize[0] + 8, graph3Y[position]), subtitle, font=font3G1, fill=1)							# Value name
	draw.polygon([(titleSize[0], graph3Y[position]), (titleSize[0] + 6, graph3Y[position]),
		(titleSize[0] + 6, graph3Y[position] + 6)], outline=0, fill=0)											# Cropped angle for device name area
	
	draw.rectangle((titleSize[0] + 6, graph3Y[position] + 8, 127, graph3Y[position] + 18), outline=255, fill=0)	# Empty graph

	fill = scale_value(actualValue, minValue, maxValue, 125 - (titleSize[0] + 8))
	draw.rectangle((titleSize[0] + 8, graph3Y[position] + 10, (titleSize[0] + 8) + fill, graph3Y[position] + 16), outline=0, fill=1)	# Filling graph


def render_bars(serverip):
	libSensor.set_ip(serverip)
	global draw
	while True:
		temp = libSensor.get_cpu_package_temp()
		load = libSensor.get_cpu_total_load()
		clock = libSensor.get_cpu_clock_total_usage()

		with globalVars.canvas(globalVars.device) as draw:
			draw_3graph("TMP", "CPU", 0, (temp, 25, 80))
			draw_3graph("LOD", "CPU", 1, (load, 0, 100))
			draw_3graph("CLK", "CPU", 2, (clock, 0, 3800))
			sleep(1)
