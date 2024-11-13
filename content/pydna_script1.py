from pydna import genbank, parsers, dseqrecord

# Download a sequence from Genbank
gb = genbank.Genbank("hello@email.com")
dseqr = gb.nucleotide("LP002422.1")

# Read a sequence from a file
dseqr = parsers.parse("sequence.gb")[0]

# Instantiate a sequence record
dseqr = dseqrecord.Dseqrecord(seq="ATGC")
