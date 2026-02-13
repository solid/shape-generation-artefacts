

# Source 

../data/raw/shacl/SolidOS_contacts_pane_shapes_contacts_shapes_ttl.ttl

 non-standard vcard extensions ref https://raw.githack.com/solid/contacts/refs/heads/main/vcard-extension-addressbook.ttl


```

@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#>.
@prefix : <#>.

<> rdfs:label "Shape file for VCARD data in Solid";
  rdfs:comment """The shapes in this file define the way
  contact information is storedd in Solid.  Importantly, this shape,
  defined in the 2014 Note "vCard Ontology - for describing People and Organizations",
  allows direct conversion to and from the widley deployed VCARD format,
  so users should be able import and export and ideally sync their contacts
  between their Solid pod and other systems.

  Note that VCARD has a URL field with a type which allows us to carry
  web URIs such as a hompage URI, a public RDF URI in public data such as dbpedia
  and wikidata, and, critically, a Solid WebID.
  """.

AddressBookShape a sh:NodeShape ;
  sh:targetClass vcard:AddressBook ;
  sh:property [
    sh:path vcard:fn ;
    sh:datatype xsd:string;
    sh:minCount 1;
  ];
  sh:property [
    sh:path vcard:nameEmailIndex ;
    # sh:datatype xsd:string;
    sh:minCount 1;
  ];
  sh:property [
    sh:path vcard:groupIndex ;
    a sh:FollowMe; # Loadme before continuing...
    sh:count 1;
  ] ;
  sh:property [
    sh:path vcard:includesGroup ;
    sh:mincount 0;
  ] ;
  sh:property [
    sh:path vcard:inAddressBook ; ## Invers
    a sh:FollowMe; # Loadme before continuing...
    sh:count 1;
  ] .



# Source file: ../data/raw/shacl/SolidOS_contacts_pane_shapes_contacts_shapes_ttl.ttl

```