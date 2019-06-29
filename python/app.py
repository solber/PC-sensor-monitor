serverip = None

WINDOW_NONE = 0
WINDOW_SPLASH = 1
WINDOW_SNIFFER = 2

currentWindow = WINDOW_NONE


while True:
    if currentWindow is WINDOW_NONE:
        currentWindow = WINDOW_SPLASH
        from splash import render_splash
        from time import sleep
        render_splash()

    if currentWindow is WINDOW_SPLASH:
        currentWindow = WINDOW_SNIFFER
        from sniffer import render_sniffer
        serverip = render_sniffer()

    if currentWindow is WINDOW_SNIFFER and serverip is not None:
        from cpuBars import render_bars
        render_bars(serverip)
