# LZW Encoder

from sys import argv
from struct import *

# taking the input file and the number of bits from command line
# go zemame input fajlot i brojot na bitovi od komandna linija
# definirame maksimalna golemina na tabela
# go otvarame input fajlot
# go citame inoutot fajlot i gi zacuvuvame informaciite vo promenliva
# defining the maximum table size

input_file, n = argv[1:]
maximum_table_size = pow(2, int(n))
file = open(input_file)
data = file.read()

# go gradime i inicijalizirame direkotriumot

dictionary_size = 256
dictionary = {chr(i): i for i in range(dictionary_size)}
string = ""  # Stringot e null
compressed_data = []  # promenliva za zacuvuvanje na kompresiranite informacii

# iterirame niz input simbolite

# LZV algoritam za kompresija
for symbol in data:
    string_plus_symbol = string + symbol  # get input symbol.
    if string_plus_symbol in dictionary:
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[string])
        if len(dictionary) <= maximum_table_size:
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])

# go zacuvuvame kompresiraniot string (po bajti)
out = input_file.split(".")[0]
output_file = open(out + ".lzw", "wb")
for data in compressed_data:
    output_file.write(pack('>H', int(data)))

output_file.close()
file.close()
