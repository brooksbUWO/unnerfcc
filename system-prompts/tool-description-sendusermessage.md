<!--
name: "Tool Description: SendUserMessage"
description: "Describes the SendUserMessage tool for sending user-visible Markdown messages and attachments with normal or proactive status"
ccVersion: "2.1.116"
-->
Send a message that the user reads. Text outside this tool is visible in the detail view. But most users do not open it. Put the answer here.

`message` supports markdown. `attachments` accepts two forms per entry. The first form is a file path string (absolute or cwd-relative). Use it for a file that you can read here, such as an image, a diff, or a log. The second form is the exact `{file_uuid, file_name, size, is_image}` object from a device tool such as `attach_file`. Use the path form for a file on your working filesystem. Use the object form for a file already uploaded by the device of the user. In that case, the device gives you the object as a reference. Pass that object through verbatim. Do not try to make a path for it.

`status` labels intent. Use 'normal' for a reply to what the user just asked. Use 'proactive' for a message that you start yourself. Examples are a finished scheduled task or a blocker found during background work. Another example is a need for input on something the user did not ask about. Set the status honestly. Downstream routing uses it.
