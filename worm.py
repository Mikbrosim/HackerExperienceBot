HE = __import__("main")
from time import sleep
import re


def Worm(ips, clearLog, getSoftware, yourIp):
    HE.GetYourSoftware()
    hackedIps = []
    for ip in ips:
        HE.ips.append(ip)
    while len(HE.ips) >= 1:
        ip = HE.ips[0]
        if ip in hackedIps:
            HE.ips.remove(ip)
            print (ip + " is in this list " + hackedIps)
        elif ip == yourIp:
            continue
        else:
            HE.ips.remove(ip)
            if HE.Hack(ip, clearLog, getSoftware, getIps = True):
                program(ip)
            hackedIps.append(ip)

def program(ip):
    HE.Upload("Mikbrosim.vddos")
    HE.GetSoftware(ip)
    HE.Install("Mikbrosim.vddos")