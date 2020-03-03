import binascii
import base64

a = "3d3d516343746d4d6d6c315669563362"
#hex to bin
b = binascii.unhexlify(a)
#reverse the string and then base64 decode
res = base64.b64decode(b[::-1])
#print string object
print(res.decode("ASCII"))
