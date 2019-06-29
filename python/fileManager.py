from re import compile, findall

#const
IP_LIST_PATH = 'config/ips.list'


def get_ips_to_try():
    f = open(IP_LIST_PATH, "r")
    if f.mode == 'r':
        contents = f.read()
        pattern = compile(r'<last_ip>(.*)</last_ip>')
        f.close()
        return findall(pattern, contents)
    return []


def write_working_ip(ipToWrite):
    f = open(IP_LIST_PATH, "r")
    if f.mode == 'r':
        contents = f.read()
        pattern = compile(r'<last_ip>(.*)</last_ip>')

        firsttime = True
        for (ip) in findall(pattern, contents):
            firsttime = False
            if ip != ipToWrite:
                f = open("config/ips.list", "a+")
                f.write("<last_ip>" + str(ipToWrite) + "</last_ip>\r\n")
                return True
        if firsttime:
            f = open("config/ips.list", "w+")
            f.write("<last_ip>" + str(ipToWrite) + "</last_ip>\r\n")
            return True
        f.close()
        return False
