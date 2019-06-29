from time import sleep
import globalVars
import libSensor

draw = None


def render_bars(server_ip):
	libSensor.set_ip(server_ip)
	global draw
	from libBars import scale_value, draw_3graph
	while True:
		temp = libSensor.get_cpu_package_temp()
		load = libSensor.get_cpu_total_load()
		clock = libSensor.get_cpu_clock_total_usage()

		with globalVars.canvas(globalVars.device) as draw:
			draw_3graph("TMP", "CPU", 0, (temp, 25, 60), draw)
			draw_3graph("LOD", "CPU", 1, (load, 0, 100), draw)
			draw_3graph("CLK", "CPU", 2, (clock, 0, 3090), draw)
			sleep(1)
