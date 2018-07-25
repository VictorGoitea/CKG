##### Internal Databases (jensenlab.org) #####
internal_db_directory = databasesDir + "InternalDatabases/"
internal_db_url = "http://download.jensenlab.org/FILE"
internal_db_files = {"-26":"human_disease_integrated_full.tsv", 
                    "-25":"human_tissue_integrated_full.tsv",
                    "-23":"human_compartment_integrated_full.tsv"}
internal_db_mentions_files = {"-26":"disease_textmining_mentions.tsv", 
                    "-25":"tissue_textmining_mentions.tsv",
                    "-23":"compartment_textmining_mentions.tsv",
                    "9606": "human_textmining_mentions.tsv",
                    "-1": "chemical_textmining_mentions.tsv"}
internal_db_types = {"-26":("Protein","Disease"),
                    "-25":("Protein","Tissue"),
                    "-23":("Protein","Cellular_compartment")}
internal_db_mentions_types = {"-26":("Disease", "Publication"),
                            "-25":("Tissue", "Publication"),
                            "-23":("Cellular_compartment", "Publication"), 
                            "9606":("Protein","Publication"), 
                            "-1":("Chemical","Publication")}
internal_db_mentions_filters = {"-25": ["BTO:0000000"],
                                "-26": ["DOID:4", "DOID:162"],
                                "-23":["GO:0005575", "GO:0005623", "GO:0044464", "GO:0030054"]}
internal_db_sources = {"-25": "TISSUES", "-26": "DISEASES", "-23": "COMPARTMENTS"}

#### Pubmed ######
PMC_db_url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/PMC-ids.csv.gz"
PMC_fields = ["PMID","Journal Title","ISSN","Year","Volume","Issue","Page","DOI","PMCID"]
pubmed_linkout = "https://www.ncbi.nlm.nih.gov/pubmed/PUBMEDID"
