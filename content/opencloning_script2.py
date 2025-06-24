# Golden Gate
golden_gate_source = RestrictionAndLigationSource(id=1, restriction_enzymes=["BsaI"])
result = await restriction_and_ligation(
    golden_gate_source,
    [seq1, seq2, seq3],
)

# Gibson Assembly
gibson_source = GibsonAssemblySource(id=2)
result = await gibson_assembly(gibson_source, [seq1, seq2, seq3])

# Homologous Recombination
hom_rec_source = HomologousRecombinationSource(id=3)
result = await homologous_recombination(hom_rec_source, [template, insert])
