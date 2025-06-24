addgene_source = AddgeneIdSource(id=1, repository_id="52691", repository_name="addgene")
addgene_result = await get_from_repository_id_addgene(addgene_source)

locus_source = GenomeCoordinatesSource(
    id=2,
    type="GenomeCoordinatesSource",
    assembly_accession="GCF_000146045.2",
    sequence_accession="NC_001147.6",
    start=432688,
    end=437345,
    strand=-1,
)
locus_result = await genome_coordinates(locus_source)
