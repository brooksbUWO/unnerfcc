<!--
name: "Tool Description: Browser file upload"
description: "Describes the browser file upload tool, which uploads shared files directly to a page file input by element ref and enforces the 10 MB combined size limit"
ccVersion: "2.1.163"
-->
Upload one or more files to a file input element on the page. Do not click on file upload buttons or file inputs. A click opens a native file picker dialog. You cannot see or interact with that dialog. Instead, use read_page or find to locate the file input element. Then use this tool with its ref to upload the files directly. You can upload only files that the user shares with this session. These include attachments, the session's outputs and uploads folders, and folders that the user connects. The tool rejects other paths. The combined size of all files in a single call must stay under 10 MB.
