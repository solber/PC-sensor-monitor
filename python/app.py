server_ip = None

WINDOW_NONE = 0
WINDOW_SPLASH = 1
WINDOW_SNIFFER = 2

current_window = WINDOW_NONE


while True:
    if current_window is WINDOW_NONE:
        current_window = WINDOW_SPLASH
        from splash import render_splash
        render_splash()

    if current_window is WINDOW_SPLASH:
        current_window = WINDOW_SNIFFER
        from sniffer import render_sniffer
        server_ip = render_sniffer()

    if current_window is WINDOW_SNIFFER and server_ip is not None:
        from cpuBars import render_bars
        render_bars(server_ip)
