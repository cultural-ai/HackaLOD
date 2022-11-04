# HackaLOD
HackaLOD 2022

#### Symbolism Knowledge Graph

#### Retrieving labels of symbols in English and Dutch

We queried Wikidata to get labels of entities that represent symbols depicted on paintings [wikihyper.csv](https://github.com/cultural-ai/HackaLOD/blob/main/wikihyper.csv).
To retrieve labels of entities in English and Dutch, we used MediaWiki API [see Jypiter notebook](https://github.com/cultural-ai/HackaLOD/blob/main/getting_wikidata_labels.ipynb).
The resulting file with labels in two languages contain 2,691 entities.
191 entities did not have Dutch labels in Wikidata [qids_no_nl_labels.json](https://github.com/cultural-ai/HackaLOD/blob/main/qids_no_nl_labels.json), so we translated English labels into Dutch using Google Translate API.

#### Querying the symbol labels in the NMVW collection

