<!--
name: "Data: SDK request user dialog kind field"
description: "Schema description for the open dialog_kind field on SDK request_user_dialog control requests and its client capability contract"
ccVersion: "2.1.234"
-->
Identifier for the dialog the host must render. Open string union. New kinds can be added without bumping the protocol. A kind is only sent in sessions where some attached client declared it in initialize.supportedDialogKinds (declare exactly the kinds you can render). On multi-client transports the request still reaches every attached client. A host that receives a kind it did not declare must not answer it (an error-subtype response is discarded and the dialog stays pending). Never with {behavior: "cancelled"}, which is a real settlement treated as the user dismissing the dialog. An unanswered dialog is cancelled by the CLI after its dialog deadline.
