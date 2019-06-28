import globalVars

font5L = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 10)
font3G0 = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 14)
font3G1 = globalVars.ImageFont.truetype("./lucidaSTW.ttf", 7)

def scale_value(actualValue, minValue, maxValue, graphLength): # Used to match a sensor value range with a graph length
	
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

	fill = scale_value(actualValue, minValue, maxValue, 126 - titleSize[0] + 5)
	draw.rectangle((titleSize[0] + 8, graph3Y[position] + 10, fill + titleSize[0] + 4, graph3Y[position] + 16), outline=0, fill=1)	# Filling graph

while True:
	with globalVars.canvas(globalVars.device) as draw:
		draw_3graph("Cpu", "Freq", 0, (38,0,70))
		draw_3graph("Gpu", "Clock", 1, (32,0,90))
		draw_3graph("MB", "Vram", 2, (25,0,50))

GPIO.cleanup()