## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Generate a single self-contained merged LinkML YAML with all imports resolved
[group('model development - extended')]
gen-merged-schema:
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -o {{dest}}/linkml/{{schema_name}}.merged.linkml.yaml {{source_schema_path}}

# Validate one or more metadata files (YAML or JSON) against the schema
[group('model development')]
validate +files:
  uv run linkml-validate -s {{source_schema_path}} -C ExposureLinkageCollection {{files}}
