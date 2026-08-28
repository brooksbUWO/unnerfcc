<!--
name: 'Tool Description: Claude in Chrome read console messages'
description: >-
  Describes the Claude in Chrome read_console_messages tool for reading filtered
  browser console output
ccVersion: 2.1.178
-->
Read browser console messages from a specific tab. This includes console.log, console.error, and console.warn. The tool helps you debug JavaScript errors, view application logs, and understand the browser console. It returns messages from the current domain only. If you do not have a valid tab ID, call the browser-occ connection tool first. It gives the available tabs. Pass a pattern to filter the messages. Without a pattern, you can get too many irrelevant messages.
