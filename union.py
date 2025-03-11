import nbformat

# Load the two notebooks
with open("taller6_1.ipynb", "r", encoding="utf-8") as f:
    nb1 = nbformat.read(f, as_version=4)

with open("taller6_2.ipynb", "r", encoding="utf-8") as f:
    nb2 = nbformat.read(f, as_version=4)

# Merge notebook2 cells into notebook1
nb1.cells.extend(nb2.cells)

# Save the merged notebook
with open("taller6.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb1, f)

print("Notebooks merged successfully!")
