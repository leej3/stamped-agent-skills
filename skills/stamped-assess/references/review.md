# Review and improvement

Use the review queue to prioritize disagreements, unresolved essential criteria, initial rubric calibration, and a continuing sample.
Review judgments against their evidence and intended target.
Do not treat agreement between agents as human approval.

Create a separate review record using `stamped-assess digest RECORDS ASSESSMENT_ID`.
Record the actual reviewer kind and decisions for specific criteria: agree, disagree, or needs_evidence.
A suggested status preserves the original assessment rather than overwriting it.
Corrections use new records with supersedes links.
Human identity is an asserted field until established through the contribution review process.
Never fill it with a human's identity for work the agent performed.

For before/after comparisons, retain exact object versions and rubric, identify the intervention, and compare equivalent conditions.
Changed rubric criteria or reference versions require explicit reconciliation.
A comparison_group is a link, not proof of a controlled experiment.
Do not infer skill effectiveness from an object's improvement alone.
A useful evaluation compares matched tasks, records the exact skill and agent configuration, and repeats assessments independently.

When evaluating an instrumented assessor, separate collector errors, assessor errors, and defects in the assessed object.
Describe changes to the collector or skill in the evaluation protocol; the assessment intervention field describes object changes.
Predeclare the task fixtures, grading criteria, equivalent resources, and measures such as unsupported judgments, missed evidence, correction burden, and measured review time.
Include missing delivery, duplicated events, successful commands with incorrect outputs, and incomplete provenance among cases when relevant.
Vary execution order and separate execution from grading; hide treatment labels from reviewers where practical.
One smoke test establishes behavior in its fixture, not causal effectiveness.

Review sampled quiet successes and confident positive judgments as well as flagged disagreements.
Report the sampling frame, selection rule, reviewed denominator, and collection gaps; agents can agree because they share an unsupported assumption.
The existing queue helps prioritize review but does not measure its own error-detection rate.
