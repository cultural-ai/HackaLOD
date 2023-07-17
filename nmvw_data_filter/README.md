/**Write the filtering steps here**/

The National Museum of Wereldculturen collection data can be found [here](https://collectie.wereldculturen.nl/thesaurus/#/query/d475fb2c-95cf-438d-9395-4823a7e16dbb).


Filtering through "schilderkunst" or "painting"

```SPARQL
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX edm: <http://www.europeana.eu/schemas/edm/>
select (COUNT(DISTINCT ?s) AS ?n) where { 
    ?s ?p ?o.
    ?s edm:isRelatedTo <https://hdl.handle.net/20.500.11840/termmaster2666>.
    ?s edm:rights ?right .
    FILTER (?right IN("CC-BY-SA 4.0", "PD-anon-70-EU", "Public domain"))
}
```
returns 7751 object


Filtering through "beeldende kunst naar medium" or "visual arts by medium"

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

