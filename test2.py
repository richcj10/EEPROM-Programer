
import re
def crc_poly(data, n, poly, crc=0, ref_in=False, ref_out=False, xor_out=0):
    g = 1 << n | poly  # Generator polynomial

    # Loop over the data
    for d in data:
        # Reverse the input byte if the flag is true
        if ref_in:
            d = reflect_data(d, 8)

        # XOR the top byte in the CRC with the input byte
        crc ^= d << (n - 8)

        # Loop over all the bits in the byte
        for _ in range(8):
            # Start by shifting the CRC, so we can check for the top bit
            crc <<= 1

            # XOR the CRC if the top bit is 1
            if crc & (1 << n):
                crc ^= g

    # Return the CRC value
    return crc ^ xor_out

msg = [b'M', b'1', b'P', b'0', b'0', b'0', b'2', b'8', b'5', b'0', b'C', b'22', b'02', b'23']

def hexify(s):
    return "b'" + re.sub(r'.', lambda m: f'\\x{ord(m.group(0)):02x}', s.decode('latin1')) + "'"

# CRC-8
##crc = crc_poly(msg, 8, 0x07)
##print(hex(crc), '{0:08b}'.format(crc))
##assert crc == 0x78
my_str = "hello world"
my_str_as_bytes = str.encode("m")
a  = bytearray(my_str_as_bytes)
a.append(1)
a.extend('p'.encode('utf-8'))
a.extend('0'.encode('utf-8'))
crc = crc_poly(a, 8, 0x07)
print(hex(crc), '{0:08b}'.format(crc))
a.append(crc)
print(hexify(a)) # ensure it is byte representation
