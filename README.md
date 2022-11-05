# HackaLOD
HackaLOD 2022

### Purpose

Building a web app in which users can choose a context from a predefined list, and then explore a 3D exhibition in which the context is presented from different cultural contexts. For each cultural context, a series of artwork is presented to the user that contain a symbol of that concept.

### Dataset Used

#### Symbolism Knowledge Graph

[HyperReal](https://w3id.org/simulation/data) is Knowledge Graph based on cultural symbolism, that contains more than 40000 symbol-symbolic meanings relationships, also called Simulations. The structure of Hyper Real is based on the [Simulation Ontology](https:w3id.org/simulation/ontology) which was designed to describe symbols through N-ary relationships classes (Simulations). Simulations link together a symbol (also called Simulacrum), its symbolic meaning (also called Reality Counterpart) and the cultural context in which the symbol symbolize the symbolic meaning. An example would be the fish-happiness simulation, in which fish is the symbol, happiness is the symbolic meaning, and Buddhist is the context. A visual example of the fish-happiness simulation following the simulation ontology schema can be found in figure 1.


![Fish-happiness](fishhappiness.png)

#### Wikidata

Wikidata is a miscellaneous Knowledge Graph that...

#### NMW collection

...

#### Retrieving labels of symbols in English and Dutch

We queried Wikidata to get labels of entities that represent symbols depicted on paintings [wikihyper.csv](https://github.com/cultural-ai/HackaLOD/blob/main/wikihyper.csv).
To retrieve labels of entities in English and Dutch, we used MediaWiki API [see Jypiter notebook](https://github.com/cultural-ai/HackaLOD/blob/main/getting_wikidata_labels.ipynb).
The resulting file with labels in two languages contain 2,691 entities.
191 entities did not have Dutch labels in Wikidata [qids_no_nl_labels.json](https://github.com/cultural-ai/HackaLOD/blob/main/qids_no_nl_labels.json), so we translated English labels into Dutch using Google Translate API.

#### Querying the symbol labels in the NMVW collection

