## NMWV Data Prepapration 

The National Museum of Wereldculturen collection data can be found [here](https://collectie.wereldculturen.nl/thesaurus/#/query/d475fb2c-95cf-438d-9395-4823a7e16dbb).


### Filtering through "schilderkunst" or "painting"

```SPARQL
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX edm: <http://www.europeana.eu/schemas/edm/>
select DISTINCT ?s where { 
    ?s ?p ?o.
    ?s edm:isRelatedTo <https://hdl.handle.net/20.500.11840/termmaster2666>.
    ?s edm:rights ?right .
    FILTER (?right IN("CC-BY-SA 4.0", "PD-anon-70-EU", "Public domain"))
}
```
returns 7751 object

The filtered objects' URIs are [here](painting_objects.csv).



### Filtering through "beeldende kunst naar medium" or "visual arts by medium"



```SPARQL
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX edm: <http://www.europeana.eu/schemas/edm/>
select (COUNT(DISTINCT ?s) AS ?n) where { 
    ?s ?p ?o.
    ?s edm:isRelatedTo ?term.
    ?term skos:broader <https://hdl.handle.net/20.500.11840/termmaster24843>.
    ?s edm:rights ?right .
    FILTER (?right IN("CC-BY-SA 4.0", "PD-anon-70-EU", "Public domain"))
}
```
returns 27837 objects

The filtered objects' URIs are [here](visual_art.csv).

Narrower terms of visual art are: 
| term | PrefLabel | AltLabel |
| ------------- |:-------------:| -----:|
| https://hdl.handle.net/20.500.11840/termmaster2666 | schilderkunst    | painting | 
| https://hdl.handle.net/20.500.11840/termmaster2667 |	grafiek (ook modern drukwerk)|	prints |
| https://hdl.handle.net/20.500.11840/termmaster2665 | tekenkunst| drawing  |
| https://hdl.handle.net/20.500.11840/termmaster2668	|   beeldhouwkunst	| sculpture |
|   https://hdl.handle.net/20.500.11840/termmaster2670  | audio-visuele kunst   |   audiovisual arts    |
|   https://hdl.handle.net/20.500.11840/termmaster24844	|   installatie (kunstwerk) |	installations (artworks)    

### Copyrights:
Possible copyright lists:
- "(not assigned)" 
- "CC-BY-SA 4.0" 
- "PD-anon-70-EU"
- "Copyright"
- "Public domain"
- "CC-BY-NC-ND 4.0"
- "Copyrightstatus onbekend"
- "Copyright, wel tonen"
- "Copyright, ontsluiten met toestemming"

