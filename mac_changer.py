

#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments)=parser.parse_args()
    if not options.interface:
        print("[-] please specify an interface , use --help for more info")
    elif not options.new_mac:
        print("[-] please specify an MAC address , use --help for more info")
    return options


def change_mac(interface , new_mac):
    print("[+] Changing MAC address for " , interface , "to " , new_mac)

    subprocess.call(["ifconfig", interface, "down"])

    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] could not read MAC address")
# parser = optparse.OptionParser()

# parser.add_option("-i", "--interface", dest="interface", help= "Interface to change its MAC address")
# parser.add_option("-m", "--mac", dest="new_mac", help= "New MAC address")
#
# (options, arguments) = parser.parse_args()

#subprocess.call("ifconfig" , shell=True)
# interface = options.interface                      #  input("interface > ")
#
# new_mac = options.new_mac                          #input("new_mac > ")
#(options,arguments) = get_arguments()
options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("Current MAC : ", str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.new_mac)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " , current_mac)
else:
    print("MAC address did not get changed")



# print("[+] Changing MAC address for "+ interface + "to "+ new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

# subprocess.call(["ifconfig",interface,"down"])
#
# subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
#
# subprocess.call(["ifconfig",interface,"up"])