# Solid Shape Artefacts

## Introduction
A collection of [SHACL shape artefacts](./shapes) from SolidOS project repositories that are used in core SolidOS applications. 

- Shapes will be added to a forthcoming Solid SHACL shape & ontology catalogue 
    - A roadmapped plan will make this *the* marketplace for SHACL shapes & ontologies for the Solid ecosystem 
- The shapes have been referenced for mapped RDF Objects in [@solid/object](https://github.com/solid/object/tree/main/src/solid)

## Repository Structure

```text
.
├── data/                 # raw and processed data
├── scripts/              # scan, download and processing scripts
├── shapes/               # SHACL shapes
├── LICENSE.md            
└── README.md
```

## Process

A scripted process searched SolidOS Github repos for RDF Form and SHACL shape definitions that were then extracted in a process described further in [scripts/README.md](./scripts/README.md)


## Provenance

Each shape artifact has a `readme.md` file describing the source repository/file.

---

## License

MIT

