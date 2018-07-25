##### RefSeq #########
refseq_url = "ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/GCF_000001405.37_GRCh38.p11/GCF_000001405.37_GRCh38.p11_feature_table.txt.gz"
headerEntities = {"Transcript":["ID", ":LABEL", "name", "class", "assembly", "taxid"], 
                "Chromosome":["ID", ":LABEL", "name", "taxid"],
                "LOCATED_IN": ['START_ID', 'END_ID','TYPE','start','end','strand', 'source'],
                "TRANSCRIBED_INTO": ['START_ID', 'END_ID','TYPE', 'source']}
