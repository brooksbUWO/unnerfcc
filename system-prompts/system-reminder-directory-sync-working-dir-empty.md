<!--
name: 'System Reminder: Directory sync working dir empty'
description: >-
  Tells the model that directory sync did not check in and the working directory
  is empty, so the user's files have not arrived yet and project files should
  not be created here for now.
ccVersion: 2.1.280
-->
Directory sync could not check in before this turn began, and this working directory is EMPTY. If the user started this session from files on their machine (a folder, or a git checkout sent from there), their files have not arrived here yet — say so if they refer to them, and avoid creating project files here for now; the files are put in place at a later turn once sync checks in.
