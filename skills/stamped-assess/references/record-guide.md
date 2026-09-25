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
