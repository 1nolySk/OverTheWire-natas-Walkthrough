#!/usr/bin/python3

import base64

a = base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=")
a = a.decode("ASCII")

b = '{"showpassword":"no","bgcolor":"#ffffff"}'
out = []

for i in range(len(a)):
	out.append(chr(ord(a[i])^ord(b[i%len(b)])))

out = ''.join(out)

print("key = ",out)

key = "qw8J"

data = '{"showpassword":"yes","bgcolor":"#ffffff"}'

out = []

for i in range(len(data)):
	out.append(chr(ord(data[i])^ord(key[i%len(key)])))

out = ''.join(out)

print("New Cookie = ", base64.b64encode(out))

