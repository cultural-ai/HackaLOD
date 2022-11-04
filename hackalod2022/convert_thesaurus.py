import rdflib
import glob, os


def run(directory):
    new_graph = rdflib.Graph()

    try:
        for file in glob.glob(f"{directory}/*.ttl"):
            print(file)
            g = rdflib.Graph().parse(file)
            q = """SELECT * WHERE{
                        ?s ?p ?o.
                    }"""
            for row in g:
                new_graph.add(row)

    finally:
        # store the newly constructed graph in one file
        new_graph.serialize(destination=os.path.join(directory, "thesaurus_full.ttl"))