<!--
name: "Tool Description: Computer request_access"
description: "Describes the computer-use request_access tool for asking user permission to control applications in the session"
ccVersion: "2.1.173"
-->
Request user permission to control a set of applications for this session. Call this tool before any other tool in this server. The user sees a single dialog that lists all requested apps. The user allows the whole set or denies it. Call this tool again mid-session to add more apps. Previously granted apps remain granted. The tool returns the granted apps, the denied apps, and the screenshot filtering capability.
