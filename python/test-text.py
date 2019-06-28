import globalVars

font5L = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 10)
font3G0 = globalVars.ImageFont.truetype("./lucidaSTWB.ttf", 14)
font3G1 = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 7)

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

while True:
	test = libSensor.get_cpu_info(libSensor.INFO_CPU_TEMP)
	testVal = float((test[1][libSensor.SENSOR_VALUE]).replace(',', '.'))
	testLoad = libSensor.get_cpu_info(libSensor.INFO_CPU_LOAD)
	testLoadVal = round(float((testLoad[5][libSensor.SENSOR_VALUE]).replace(',', '.')))

	with globalVars.canvas(globalVars.device) as draw:
		draw_3graph("Cpu", "Temp", 0, (testVal,0,80))
		draw_3graph("Cpu", "Load", 1, (testLoadVal,0,100))
		#draw_3graph("MB", "Vram", 2, (25,0,50))
		sleep(1)
GPIO.cleanup()
