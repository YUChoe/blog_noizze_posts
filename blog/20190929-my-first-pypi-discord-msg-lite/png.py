import binascii
from sys import byteorder

fp = open('094701.png', 'rb')
fp.seek(16)
# byte_chunk = fp.read(4)
# width = struct.unpack('I', byte_chunk)[0]

# byte_chunk = fp.read(8)
# print('PNG file starts with an 8-byte signature', binascii.hexlify(byte_chunk))
# byte_chunk = fp.read(4)
# print('Chunks', binascii.hexlify(byte_chunk))
# byte_chunk = fp.read(4)
# print('IDHR', binascii.hexlify(byte_chunk))
byte_chunk = fp.read(4)
print('width', binascii.hexlify(byte_chunk), int.from_bytes(byte_chunk, byteorder='big'))
byte_chunk = fp.read(4)
print('height', binascii.hexlify(byte_chunk), int.from_bytes(byte_chunk, byteorder='big'))

fp.close()


# print(width)
