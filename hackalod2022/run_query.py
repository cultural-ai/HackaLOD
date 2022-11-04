import rdflib
import glob, os, time


# Load data in a graph and run the query and add them to the new graph
def run_query(file = "/Users/sarah_shoilee/Desktop/Sarah/Pressing_Matter_Data/TTLRDFobjects/object_full.ttl"):
    g = rdflib.Graph().parse(file)

    var = "parel"

    q = f"""
    PREFIX dc: <http://purl.org/dc/terms/>
    PREFIX dc11: <http://purl.org/dc/elements/1.1/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    select * where {{ 
        ?s dc11:title ?title .
        ?s dc11:description ?desc .
        FILTER (CONTAINS(?desc, {var}) || CONTAINS(?title, {var}))
    }}"""

    # when cannot read the ttl file
    if len(g) == 0:
        print("NO GRAPH")

    print(len(g.query(q)))

    for row in g.query(q):
        print(row)


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
        new_graph.serialize(destination=os.path.join(directory, "object_full.ttl"))






