<!--
name: "Tool Description: NotebookEdit"
description: "Tool description for editing Jupyter notebook cells by replacing, inserting, or deleting a cell using cell IDs from the read tool"
ccVersion: "2.1.162"
variables:
  - "READ_TOOL_NAME"
-->
Replaces, inserts, or deletes a single cell in a Jupyter notebook (.ipynb file).

Usage:
- Before you edit, use the ${READ_TOOL_NAME} tool on the notebook in this conversation. If you do not, this tool fails.
- `notebook_path` must be an absolute path.
- `cell_id` is the `id` attribute shown in the `<cell id="...">` output of the ${READ_TOOL_NAME} tool. It is required for `replace` and `delete`.
- `edit_mode` defaults to `replace`. Use `insert` to add a new cell after the cell with the given `cell_id`. If `cell_id` is omitted, `insert` adds the cell at the start of the notebook. For an insert, `cell_type` is required. Use `delete` to remove the cell.
