# Solid Shape Artefacts

## Introduction
This repository contains scripts, intermediate files, and outputs for a process that identified and extracted shape artefacts from SolidOS project repositories. 

The [shapes](./shapes/) identified are used in core SolidOS applications and are shapes that Solid recommends to use.

The shapes will be added to a Solid shape and ontology catalogue. We have a roadmap to make this the marketplace for ontologies and shapes for the Solid ecosystem. The shapes will also used be as a point of reference for the creation of RDF Objects in [@solid/object](https://github.com/solid/object)

The output of this work is:

- a collection of shapes that are used in SolidOS applications, and that Solid recommend to use
- a collection of files from the SolidOS project that contain shape-like artefacts eg form definitions
 
---

## Process

The process involved: 
 * scan of multiple [GitHub repositories](https://github.com/orgs/SolidOS/repositories) associated with the [SolidOS Organisation](https://github.com/solid), to create a file list 
 * download of .ttl files  
 * copying of files that include the SHACL namespace to a separate folder. 
 * identification of SHACL shape-like artefacts e.g. that are used to define forms 
 * creation of shape artefact files


This repository contains:

* Scripts to: 
    * scan GitHub repositories for .ttl files
    * download .ttl files
    * copy .ttl files that contain SHACL namespace
* Downloaded .ttl files

---

## Repository Structure

```text
.
├── scripts/              # Data download and processing scripts
├── data/
│   ├── raw/              # Original downloaded files (unmodified)
│   |    ├── shacl/       # Original downloaded ttl files (unmodified) that contain the SHACL namespace
    |    ├── ttl/         # Original downloaded ttl files (unmodified)
    |    └── ttl-containing-UIForm/ # Original downloaded ttl files (unmodified) containing ui:Form 
│   └── processed/        # Intermediate shape artefacts - related files 
├── shapes/              # Final shapes
├── requirements.txt      # Python dependencies
└── README.md
```

---

## Data Pipeline

The data processing workflow is:

1. Scan SolidOS repositories for ttl files and download raw source data
2. Identify files that contain the SHACL namespace and move to dedicated folder
3.Extract SHACL shape definitions
4. Create SHEX definitions based on forms and existing SHACL shape definitions


## ⚙️ Requirements

* Python 3.9.6
* Required libraries:
  * requests
  * dotenv


Install dependencies:

```bash
pip install -r requirements.txt
```

If you want to create a virtual environment: 

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## How to Reproduce Results

### Scan SolidOS GitHub repositories 
```bash
python scripts/1_getList.py
```
### Download .ttl files 
```bash
python scripts/2_getFiles.py
```
Raw files are saved to:
```
data/raw/ttl
```


### Copy SHACL files 
```bash
python scripts/3_copySHACLfiles.py
```
Raw files will be saved to:
```
data/raw/shacl
```
---

## Data Sources

| Source         | Description               | 
| -------------- | ------------------------- |  
| https://github.com/SolidOS | SolidOS GitHub organisation account that contains multiple repositories |


---

## Output Description

The output folder contains SHACL shapes that are derived from files in the SolidOS GitHub repositories.

---

## Notes & Limitations

* Scripts will overwrite existing outputs.
* Raw data files are not modified.

---

## Reproducibility

To fully reproduce results:

* Use the specified Python version
* Use the exact dependency versions in `requirements.txt`
* Run scripts in the documented order



---

## License

[Code and Data license](LICENSE.md)

