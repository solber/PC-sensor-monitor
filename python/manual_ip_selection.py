import globalVars

currIp = 0

while True:
    with globalVars.canvas(globalVars.device) as draw:
        splitedIp = globalVars.getip().split('.')
        sniffedIpBase = str(splitedIp[0] + '.' + splitedIp[1] + '.' + splitedIp[2])
        fullIp = sniffedIpBase + '.' + str(currIp)

        globalVars.libAdvDisplay.drawCenteredText('Enter the server IP :', globalVars.top, 255, draw)
        draw.rectangle((10, 15, globalVars.width - 10, globalVars.height - 15), outline=255, fill=0)
        draw.polygon([(15, 32), (18, 29), (18, 37)], outline=255, fill=1)
        globalVars.libAdvDisplay.drawCenterTextFont(str(fullIp), globalVars.top+25, 255, draw, globalVars.libAdvDisplay.cinzel15)
        globalVars.libAdvDisplay.drawCenteredText('Press K1 to validate', globalVars.height - 10, 255, draw)
