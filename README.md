# Loop for Scientific Research

[简体中文](README.zh-CN.md)

> **v0.01 · Concept preview.** An evolving project plan and proposed architecture. Executable integration is not yet available.

**Bring independent AI perspectives into one evidence-driven research loop.**

A proposed workflow for working through research questions with a team of AI agents: understand the problem, compare approaches, carry out the work, examine the evidence, and decide what to do next. The researcher sets the direction and makes the scientific judgment.

![Proposed research loop: context, independent advice, synthesis, execution, review, and targeted iteration](assets/overview.svg)

This preview includes a design outline, the editable illustration above, and three manual handoff templates.

## What the loop is for

- **Get independent perspectives.** Models develop their own assessments before a replaceable synthesizer compares the options and unresolved disagreements.
- **Connect thinking with work.** An execution team handles literature, simulation, analysis, figures, and other tasks through the available tools.
- **Review the evidence.** Reviewers examine results and their supporting materials, then request specific follow-up work or prepare a decision for the researcher.

Different parts can be changed independently. Start with a small advisory and review team; add focused exploration, writing, broader research, or tool discovery when the question calls for it. Model roles can change with the task.

## Start with the handoffs

The three templates support a manual trial today: define a [research brief](templates/research-brief.md), collect an [advisor memo](templates/advisor-memo.md), and record the [review and next step](templates/review-and-next-step.md).

The proposed starting host is Codex with Subagent Manager, with a small number of external advisors reached through official CLIs. This connection path remains to be implemented and tested here. See the [design](docs/design.md).

**Next:** connect one external advisor to a reusable Codex subtask, preserving the request, reply, and follow-up. Then extend this into a small execution-and-review cycle.

Related standalone building blocks: [Subagent Manager](https://github.com/LiX-Works/subagent-manager), [COMSOL workflow](https://github.com/LiX-Works/COMSOL-Agent-Research-Workflow), [ScholarFetch](https://github.com/LiX-Works/ScholarFetch), and [Origin plotting](https://github.com/LiX-Works/Origin_MCP-Skill_for_Scientific-Plots). Their integration here is planned.

[中文](README.zh-CN.md) · [MIT License](LICENSE)
