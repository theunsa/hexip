"""Simple script to convert IPv4 address to hex.

Useful for PXE booting config and whatever other case
you can come up with.
"""
import sys


def validate_ip4(iplist):
    return all([(v>=0 and v<=255) for v in iplist])


def ip4_to_hex(ipstr):
    iplist = [int(v) for v in ipstr.split('.')]
    if not validate_ip4(iplist):
        raise Exception("Not valid IPv4 address.")
    hexip = "%0.2X%0.2X%0.2X%0.2X" % tuple(iplist)
    return hexip


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: hexip <IP4 address>"
    else:
        try:
            ipstr = sys.argv[1]
            hexip = ip4_to_hex(ipstr)
            print "%s = %s" % (ipstr, hexip)
        except Exception as e:
            print "Error! Exception: %s" % e
