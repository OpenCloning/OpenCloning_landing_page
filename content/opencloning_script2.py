insert1 = Dseqrecord("GGTCTCAattaAAAAAttaaAGAGACC", name="insert1")
insert2 = Dseqrecord("GGTCTCAttaaCCCCCatatAGAGACC", name="insert2")
insert3 = Dseqrecord("GGTCTCAatatGGGGGccggAGAGACC", name="insert3")

vector = Dseqrecord("TTTTattaAGAGACCTTTTTGGTCTCAccggTTTT", circular=True, name="vector")

products = golden_gate_assembly([insert1, insert2, insert3, vector], [BsaI])

print(products[0].history())

"""
╙── product (Dseqrecord(o39))
    └─╼ RestrictionAndLigationSource
        ├─╼ insert1 (Dseqrecord(-27))
        ├─╼ insert2 (Dseqrecord(-27))
        ├─╼ insert3 (Dseqrecord(-27))
        └─╼ vector (Dseqrecord(o35))
"""
