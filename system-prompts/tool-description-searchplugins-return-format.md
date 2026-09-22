<!--
name: 'Tool Description: SearchPlugins return format'
description: >-
  Describes the ranked list return format and follow-up card rendering for
  SearchPlugins.
ccVersion: 2.1.280
-->
This tool returns a ranked list with id, name, description, and whether the plugin is enabled for this session (in a channel session, whether the channel has it). If the results fit and SuggestPluginInstall is one of your tools, call it to show the install card. If not, relay the relevant results in text. If nothing is relevant, continue and do not mention the search.
