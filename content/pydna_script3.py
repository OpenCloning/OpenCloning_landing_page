from pydna import design

# Find the CDS of interest in the gene and design primers to amplify it
cds_feature = next(feature for feature in gene.features if feature.type == "CDS")
gene_amplicon = design.primer_design(cds_feature.extract(gene), target_tm=60)

# Design primers to amplify the region of interest in the vector
vector_amplicon = design.primer_design(vector[100:2300], target_tm=60)

# Print the primers
print(vector_amplicon.forward_primer, vector_amplicon.reverse_primer)
