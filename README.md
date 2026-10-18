# Loop for Scientific Research

**English** | [简体中文](README.zh-CN.md)

> **v0.01 · Concept preview.** An evolving project plan and proposed architecture. Executable integration is not yet available.

**Bring independent AI perspectives into one evidence-driven research loop.**

A proposed workflow for working through research questions with a team of AI agents: understand the problem, compare approaches, carry out the work, examine the evidence, and decide what to do next. The researcher sets the direction and makes the scientific judgment.

![Proposed research loop: context, independent advice, synthesis, execution, review, and targeted iteration](assets/overview.svg)

This preview includes a design outline, three editable illustrations, and three manual handoff templates.

## From a question to the next experiment

Advisors first assess the same question independently. A synthesizer compares their views and forms a plan. The execution team gathers sources and computational results; reviewers inspect the evidence and decide what needs attention next.

![Detailed proposed process: shared brief, independent advisors, synthesis, coordinated execution, evidence checks, independent reviewers, and targeted feedback paths](assets/research-cycle.svg)

An execution problem returns for local repair. Missing evidence triggers a targeted check or a new test. A deeper concern reopens the approach. The researcher receives the findings, remaining disagreements, and choices for the next round.

## Change the module, keep the handoff

Choose one advisory setup for the current question: a single model, two independent models, or a wider exploratory panel. They fit the same position in the workflow and hand their assessments to synthesis.

![Proposed module choices: one, two, or five model sessions can fill the same Advice position; review, writing, and search are also replaceable parts](assets/modules.svg)

Review, writing, and search can also be replaced independently. The researcher or an authorized coordinator selects the setup to match the task; a larger panel is an option, not a promise of better results.

## Start with the handoffs

The three templates support a manual trial today: define a [research brief](templates/research-brief.md), collect an [advisor memo](templates/advisor-memo.md), and record the [review and next step](templates/review-and-next-step.md).

The proposed starting host is Codex with Subagent Manager, with a small number of external advisors reached through official CLIs. This connection path remains to be implemented and tested here. See the [design](docs/design.md).

**Next:** connect one external advisor to a reusable Codex subtask, preserving the request, reply, and follow-up. Then extend this into a small execution-and-review cycle.

Related standalone building blocks: [Subagent Manager](https://github.com/LiX-Works/subagent-manager), [COMSOL workflow](https://github.com/LiX-Works/COMSOL-Agent-Research-Workflow), [ScholarFetch](https://github.com/LiX-Works/ScholarFetch), and [Origin plotting](https://github.com/LiX-Works/Origin_MCP-Skill_for_Scientific-Plots). Their integration here is planned.

[中文](README.zh-CN.md) · [MIT License](LICENSE)
