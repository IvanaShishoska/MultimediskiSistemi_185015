# LZW Decoder

from struct import *
from sys import argv

# go zemame kompresiraniot fajl kako input i brojot na bitovi od komandna linija
# definirame minimalna golemina na tablea
# go otvarame kompresiraniot fajl
# definirame promenlivi

input_file, n = argv[1:]
maximum_table_size = pow(2, int(n))
file = open(input_file, "rb")
compressed_data = []
next_code = 256
decompressed_data = ""
string = ""

# go citame kompresiraniot fajl
while True:
    rec = file.read(2)
    if len(rec) != 2:
        break
    (data,) = unpack('>H', rec)
    compressed_data.append(data)
# go gradime i inicijalizirame direktoriumot

dictionary_size = 256
dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

# iterirame po kodovite
# LZV algoritam za dekompresija

for code in compressed_data:
    if not (code in dictionary):
        dictionary[code] = string + (string[0])
    decompressed_data += dictionary[code]
    if not (len(string) == 0):
        dictionary[next_code] = string + (dictionary[code][0])
        next_code += 1
    string = dictionary[code]

# go zacuvuvame dekompresiraniot string vo fajl

out = input_file.split(".")[0]
output_file = open(out + "_decoded.txt", "w")
for data in decompressed_data:
    output_file.write(data)

output_file.close()
file.close()
