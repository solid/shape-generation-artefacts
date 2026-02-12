import os
import re
from pathlib import Path

INPUT_DIR = "../data/raw/shacl"        # Source folder
OUTPUT_BASE = "../data/processed/shapes"  # Output folder base

# Match all @prefix lines individually
PREFIX_PATTERN = re.compile(r"^@prefix\s+.*?\.$", re.MULTILINE)

# Match rdfs:comment on <>
COMMENT_PATTERN = re.compile(
    r"<>[\s\S]*?rdfs:comment\s+\"\"\"[\s\S]*?\"\"\"\s*\.", re.MULTILINE
)

# Default namespace to add if not already present
DEFAULT_NAMESPACE = "@prefix : <http://www.example.org/ns/example#> .\n\n"


def extract_prefixes(content):
    matches = PREFIX_PATTERN.findall(content)
    return "\n".join(matches) + "\n\n" if matches else ""


def extract_comment(content):
    match = COMMENT_PATTERN.search(content)
    return match.group(0) + "\n\n" if match else ""


def extract_shapes(content):
    """
    Extract all NodeShape definitions (with or without prefix).
    Returns a list of (shape_name, shape_definition).
    """
    # Match NodeShape: optional prefix + name
    pattern = re.compile(
        r"((?:\w+:)?\w+)\s+a\s+sh:NodeShape\s*;[\s\S]*?(?=(?:\n(?:\w+:)?\w+\s+a\s+sh:NodeShape)|\Z)",
        re.MULTILINE
    )

    shapes = []
    for match in pattern.finditer(content):
        shape_def = match.group(0).strip()
        full_name = match.group(1)
        # Strip optional namespace prefix from name for file/folder naming
        shape_name = full_name.split(":")[-1]
        shapes.append((shape_name, shape_def))
    return shapes


def save_shape(shape_name, prefixes, comment, shape_definition, source_file):
    """Save each shape to its own folder/file"""
    shape_folder = Path(OUTPUT_BASE) / shape_name
    shape_folder.mkdir(parents=True, exist_ok=True)
    output_file = shape_folder / f"{shape_name}.ttl"

    # Only add default namespace if a ': <...>' prefix is not already present
    if re.search(r"@prefix\s+:\s+<.*?>\s*\.", prefixes):
        namespace_to_add = ""
    else:
        namespace_to_add = DEFAULT_NAMESPACE

    # Add source annotation
    source_annotation = f"\n# Source file: {source_file}\n"

    content_to_write = namespace_to_add + prefixes + comment + shape_definition.strip() + "\n" + source_annotation

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content_to_write)

    print(f"Saved: {output_file}")


def process_directory():
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith((".ttl", ".rdf", ".txt")):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                prefixes = extract_prefixes(content)
                comment = extract_comment(content)
                shapes = extract_shapes(content)

                for shape_name, shape_def in shapes:
                    save_shape(shape_name, prefixes, comment, shape_def, filepath)


if __name__ == "__main__":
    process_directory()
