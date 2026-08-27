<!--
name: "Skill: Prototype runtime capabilities guidance"
description: "Explains when prototype Artifacts should use user-granted runtime capabilities and requires loading the artifact-capabilities skill before relying on live data or actions"
ccVersion: "2.1.229"
variables:
  - "ARTIFACT_CAPABILITIES_SKILL_NAME"
-->


## When the idea needs real data or real actions.

This is wired fidelity. A prototype that runs against the real thing proves far more than one against a mock. When the idea turns on the user's real data or real actions. Their issues, their calendar, a doc, an API they already use. Reading that live or connected data is a runtime capability. So is acting on the user's behalf from the published page, or handing the viewer a file to save. The control plane grants capabilities per user. You declare them at publish time: load the `${ARTIFACT_CAPABILITIES_SKILL_NAME}` skill before relying on it. It shows this user's capabilities and how to declare the one that fits. Fake only what no available capability covers. And if none fits, stay fully static. And keep saying what is faked.
