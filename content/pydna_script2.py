from pydna import parsers, amplify, primer
from Bio.Restriction import AscI, SalI

# Import vector and insert sequences
vector = parsers.parse("vector.gb")[0]
insert = parsers.parse("insert.gb")[0]

# Digest vector and pcr product
drop_out, vector_digested = vector.cut([AscI, SalI])
drop_left, insert_digested, drop_right = insert.cut([AscI, SalI])

# Ligate the fragments and save to file
vector_insert = (vector_digested + insert_digested).looped()
vector_insert.write("vector_insert.gb")
