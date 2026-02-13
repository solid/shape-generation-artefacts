

# Source

https://github.com/SolidOS/contacts-pane/blob/main/src/ontology/forms.ttl

```

foaf:Agent owl:disjointUnionOf  (
  vcard:Individual
  # @@  schema:robot @@  schem:SoftwareApplication, n0:Agent, n0:Person,
  prov:SoftwareAgent
  # vcard:Group     a group of agents is not (currently) an agent itself.
  # You can't get a decision out of it so it can't own a bank account
  vcard:Organization
).

```

Use of sh:xone:
* If the node validates against exactly one of the shapes → valid
* If it matches none or more than one → invalid
* This mirrors owl:disjointUnionOf.