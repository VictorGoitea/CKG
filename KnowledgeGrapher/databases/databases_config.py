#Database directory
databasesDir = "/Users/albertosantos/Development/Clinical_Proteomics_Department/ClinicalKnowledgeGraph(CKG)/data/databases/"
#Databases
databases = [
            "Internal",
            "HGNC", 
            "RefSeq", 
            "UniProt", 
            "IntAct", 
            "DisGEnet", 
            "HGNC", 
            'DrugBank',
            "DGIdb", 
            "OncoKB", 
            "STRING", 
            #"STITCH", 
            "Mentions", 
            "OncoKB",
            "CancerGenomeInterpreter", 
            "SIDER",
            "HMDB",
            "PathwayCommons",
            'GWASCatalog'
            ]

sources = {
            "Drug":"DrugBank",
            "Metabolite":"HMDB",
            "Protein":"UniProt",
            "Gene":"HGNC"    
            }
