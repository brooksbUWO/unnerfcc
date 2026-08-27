<!--
name: "Tool Parameter: SendUserMessage attachments"
description: "Describes optional SendUserMessage attachments as local file paths or pre-resolved file objects"
ccVersion: "2.1.173"
-->
Optional attachments for the user to see with your message. Each entry has one of two forms. The first form is a file path for a local file (absolute or relative to cwd). The second form is a pre-resolved `{file_uuid, file_name, size, is_image}` object from a device tool such as attach_file.
