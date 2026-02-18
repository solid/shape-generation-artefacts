import os
from rdflib import Graph
from rdflib.namespace import SH

def extract_shacl_constraints(root_folder):
    unique_constraints = set()

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".ttl"):
                file_path = os.path.join(dirpath, filename)
                print(f"Processing: {file_path}")

                try:
                    g = Graph()
                    g.parse(file_path, format="turtle")

                    for s, p, o in g:
                        if str(p).startswith(str(SH)):
                            unique_constraints.add(str(p))

                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

    return sorted(unique_constraints)


def write_to_file(constraints, output_file, local_names_only=False):
    with open(output_file, "w", encoding="utf-8") as f:
        for c in constraints:
            if local_names_only:
                c = c.split("#")[-1]
            f.write(c + "\n")


if __name__ == "__main__":
    root_folder = r"../shapes"
    output_file = r"../data/shacl_constraints.txt"

    constraints = extract_shacl_constraints(root_folder)

    write_to_file(
        constraints,
        output_file,
        local_names_only=True  # Change to False for full URIs
    )

    print(f"\nDone. {len(constraints)} unique constraints written to:")
    print(output_file)
