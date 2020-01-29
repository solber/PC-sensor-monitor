serverip = None

WINDOW_NONE = 0
WINDOW_SPLASH = 1
WINDOW_SNIFFER = 2
WINDOW_BARS = 3
WINDOW_MANUAL_IP = 4

currentWindow = WINDOW_NONE


while True:
    if currentWindow is WINDOW_NONE:
        currentWindow = WINDOW_SPLASH
        from splash import render_splash
        render_splash()

    if currentWindow is WINDOW_SPLASH:
        currentWindow = WINDOW_SNIFFER
        from sniffer import render_sniffer
        serverip = render_sniffer()

    if currentWindow is WINDOW_SNIFFER and serverip is not None and serverip != 'manual_ip_selection_window':
        currentWindow = WINDOW_BARS
        from cpuBars import render_bars
        render_bars(serverip)

    if currentWindow is WINDOW_SNIFFER and serverip is not None and serverip == 'manual_ip_selection_window':
        currentWindow = WINDOW_MANUAL_IP
        from manualIpWindow import render_window
        render_window()