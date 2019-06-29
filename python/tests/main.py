#CONST
SERVER_IP = None

#screens
SPLASH_SCREEN = 1
SNIFFER_SCREEN = 2

currentscreen = None
loadscreen = SPLASH_SCREEN

print(currentscreen)
print(loadscreen)
while True:

    if currentscreen is not SPLASH_SCREEN and loadscreen is SPLASH_SCREEN:
        loadscreen = None
        import splash
    if currentscreen is not SNIFFER_SCREEN and loadscreen is SNIFFER_SCREEN: import snifferIp
    #loadscreen = None