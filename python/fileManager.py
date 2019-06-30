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


def write_working_ip(ip_to_write):
    f = open(IP_LIST_PATH, "r")
    if f.mode == 'r':
        contents = f.read()
        pattern = compile(r'<last_ip>(.*)</last_ip>')

        first_time = True
        for (ip) in findall(pattern, contents):
            first_time = False
            if ip != ip_to_write:
                f = open("config/ips.list", "a+")
                f.write("<last_ip>" + str(ip_to_write) + "</last_ip>\r\n")
                return True
        if first_time:
            f = open("config/ips.list", "w+")
            f.write("<last_ip>" + str(ip_to_write) + "</last_ip>\r\n")
            return True
        f.close()
        return False
