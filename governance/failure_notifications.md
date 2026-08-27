# Governance Failure Notifications

## Slack Template

> 🚨 *Freedomlink1 Governance Alert*  
> Pipeline: **{{ workflow_name }}**  
> Branch: **{{ branch }}**  
> Commit: **{{ sha }}**  
> Status: ❌ FAILED  
> Summary: {{ short_reason }}  
> Link: {{ run_url }}

## Email Template

**Subject:** [Freedomlink1] Governance Pipeline FAILED — {{ workflow_name }}

**Body:**

Freedomlink1 governance pipeline has failed.

- Workflow: {{ workflow_name }}
- Branch: {{ branch }}
- Commit: {{ sha }}
- Status: FAILED
- Reason: {{ short_reason }}
- Details: {{ run_url }}

Please investigate immediately and follow the Governance Failure Playbook.
