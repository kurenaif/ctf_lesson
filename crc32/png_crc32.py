
def reverse(x:int, length:int) -> int:
    assert x.bit_length() <= length

    res = 0

    for i in range(length):
        res <<= 1
        res += (x >> i) & 1

    return res

# https://www.slideshare.net/7shi/crc32#43
def make_crc_forward(buf):
    reversed_buf = 0

    # step 2: reverse bits position (e.g. [11110000, 10101010] => [00001111, 01010101])
    for byte in buf:
        reversed_buf <<= 8
        reversed_buf += reverse(byte, 8)

    # step 3: add 4bytes zero
    reversed_buf <<= 4*8

    # step 4: flip the first 4 bytes
    reversed_buf ^= (0xffffffff << reversed_buf.bit_length() - 32)

    # step 5: crc32
    crc = reversed_buf
    g = 0x104C11DB7

    while crc > g:
        # 先頭が1のbitがくるまでskipする
        diff = crc.bit_length() - g.bit_length()
        crc ^= g << (diff)

    # step 6: reverse bit
    crc = reverse(crc, 32)

    # step 7: flip bits
    crc ^= ((1 << 32) - 1)

    return crc

def make_crc_reverse(buf):
    buf_num = 0
    buf_length = len(buf)
    # len(buf)-1 => 0 まで 逆順に
    for i in range(len(buf)-1, -1, -1):
        buf_num <<= 8
        buf_num += buf[i]

    g = 0x1db710640
    crc = 0xffffffff ^ buf_num

    for i in range(buf_length * 8):
        if crc & 1 == 1:
            crc = crc ^ g
        crc >>= 1

    return crc ^ 0xffffffff

def create_table():
    table = []
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc ^= 0x1db710640
            crc >>= 1
        table.append(crc)
    return table
 
def crc_table(buf, crc):
    crc_table = create_table()
    crc ^= 0xffffffff
    for byte in buf:
        crc = (crc >> 8) ^ crc_table[(crc & 0xff)] ^ crc_table[byte]
    return crc ^ 0xffffffff


file_in = open('./lKDTdJlQ.png', mode='rb')
content = file_in.read()
file_in.close()
magic_bytes = content[:8]
content = content[8:]

while len(content) > 0:
    print("--------------------------------------------------")
    length = int.from_bytes(content[:4], 'big')
    content = content[4:]
    print("length: {}".format(length))
    chunk_type = content[:4]
    content = content[4:]
    print("type: {}".format(chunk_type.decode('utf-8')))
    data = content[:length]
    # crc32(chunk_type, data)
    content = content[length:]
    crc = int.from_bytes(content[:4], 'big')
    print("crc        : {}".format(bin(crc)))
    print("crc table  : {}".format(bin(crc_table(chunk_type + data, 0))))
    # print("crc forward: {}".format(bin(make_crc_forward(chunk_type+data))))
    print("crc reverse: {}".format(bin(make_crc_reverse(chunk_type+data))))
    content = content[4:]
