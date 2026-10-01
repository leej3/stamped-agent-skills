# Record production

The standalone tool exports its current schema with `stamped-assess schema TYPE`, where TYPE is use_case, object, rubric, assessment, or review.
Use these exact schemas; do not invent a parallel format.
Store one YAML mapping per file under a records directory and use unique identifiers throughout.
The toolkit ships a pinned reference bundle and validates checklist identifiers, categories, checksums, and version compatibility offline.

Create use_case, object, and rubric records before the assessment.
Object sources use a full Git commit in revision, or sha256 for other snapshot mechanisms.
Sources describe the assessed snapshot; evidence locators belong in observations.
Components can reference independently assessed object snapshots.
Avoid publishing credentials, sensitive locations, or restricted content in source metadata.

The assessment identifies object, rubric, assessor, recorded_at, conditions, and a plan for every criterion. Record the actual model/runtime and skill source revision or digest when known; mark unknown metadata honestly. Retain the task instructions or a stable reference when this assessment will inform skill evaluation. Record started_at or measured elapsed time only when observed.
Each observation identifies criterion, activity, status, description, and evidence for completed work.
Each judgment cites observations for that criterion.
A finalized assessment accounts for every planned activity and includes every criterion judgment and seven principle summaries.
Finalization permits explicitly blocked or unattempted activities.

`stamped-assess summarize RECORDS` derives activity completion and judgment counts.
Those counts are evidence coverage under this rubric, not a score for universal STAMPED adherence.
Structural validation does not establish that prose conclusions are supported or that external evidence remains accessible.

When using telemetry or automated reports, distinguish host events, agent assertions, criterion judgments, and independent review.
A skill path in tool arguments establishes a candidate, not material use; a successful command establishes neither correct output nor task success.
Attribute the evidence producer and collection method in the evidence description, with a pinned context manifest when needed.
Keep collector configuration and artifact provenance distinct from the assessor's identity and the assessed object's sources.

An empty event store can mean missing delivery or incomplete collection.
Record an established access or environment barrier when an attempted check exposes one; otherwise describe the evidence gap without inventing object failure.
Separate installation inspection, isolated testing, host activation, and live operation when they support different criteria.
Unknown is appropriate when evidence cannot support a judgment.

Assign elapsed_seconds only to the activity actually measured.
Turn wall time includes waits and may cover several skills; concurrent agents' durations overlap.
Leave unavailable timing omitted rather than zero, and do not sum overlapping measurements.
Deduplicate external events by their producer's identity rules and distinguish task, turn, use, and criterion denominators before interpreting counts.

A review digest does not freeze the contents of linked resources.
Retain evidence revisions or digests and accessible snapshots where permitted.
For redacted evidence, identify the derivative separately from the restricted original and state what review cannot establish.
