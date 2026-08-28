<!--
name: tool-description-edit-minimal-old-string-guidance
description: ''
ccVersion: 2.1.235
-->

- Keep `old_string` short. Usually 1-3 lines is enough to be unique in the file. Extra context wastes tokens and is an error.
- The edit FAILS for an `old_string` that is not unique in the file. In that case, add the minimum extra context for uniqueness. Or use `replace_all` to change every instance.
