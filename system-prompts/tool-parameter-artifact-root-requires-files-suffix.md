<!--
name: 'Tool Parameter: Artifact root requires files suffix'
description: >-
  Clarifies that root may stand alone on an Artifact made from a type, where a
  data file_path is served relative to root unless a files entry states its
  served path.
ccVersion: 2.1.321
-->
 — except for an Artifact made from an Artifact type (or being created from one), where it may stand alone: a data `file_path` is then served at its path relative to `root`, unless a `files` map entry states its served path. Send it with every such publish, set to the folder that holds the Artifact's files at their served paths
