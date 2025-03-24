import nbformat

def merge_notebooks(notebook_files, output_file):
    # Create an empty list to store the cells of all notebooks
    all_cells = []
    
    for notebook_file in notebook_files:
        # Load the notebook
        with open(notebook_file, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
            
            # Append all the cells from this notebook
            all_cells.extend(notebook.cells)
    
    # Create a new notebook
    merged_notebook = nbformat.v4.new_notebook()
    
    # Add the merged cells to the new notebook
    merged_notebook.cells = all_cells
    
    # Write the merged notebook to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged_notebook, f)

# Example usage
notebooks_to_merge = ['code.ipynb', 'Final 5.2.1:5.2.3 fixed.ipynb', 'Finalised 5.2.2 and 5.2.4 and 5.2.5.ipynb']
output_notebook = 'merged_notebook.ipynb'
merge_notebooks(notebooks_to_merge, output_notebook)
