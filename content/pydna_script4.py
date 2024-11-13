# Follows from previous example
from pydna.assembly import Assembly

# Extend those primers to use them for Gibson
gene_amplicon2, vector_amplicon2 = design.assembly_fragments(
    [gene_amplicon, vector_amplicon], circular=True
)

# Print the primers
for amplicon in [gene_amplicon2, vector_amplicon2]:
    print(amplicon.forward_primer.seq, amplicon.reverse_primer.seq, sep="\n")

# Assemble the fragments
assembly = Assembly([gene_amplicon2, vector_amplicon2])
assembly_product = assembly.assemble_circular()[0]
