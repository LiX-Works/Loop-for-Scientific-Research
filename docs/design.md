# Design direction

Loop for Scientific Research is an early project plan for organizing AI-assisted scientific work. Its proposed contribution is the connection between independent advice, tool-based execution, evidence review, and the researcher's decisions. Version 0.01 provides an illustration and manual templates; the runtime remains to be built.

## One research question, several connected loops

**Understand.** Establish the research context, objective, existing evidence, constraints, and what a useful result would look like. Clarify consequential ambiguities before committing substantial work. The research brief provides a common starting point.

**Advise independently.** Give selected models the same brief and supporting materials. Each proposes an approach, identifies weaknesses, and describes the evidence that could distinguish competing explanations. Collect their initial assessments before exposing them to one another's answers.

**Synthesize.** A replaceable synthesizer compares the proposals, preserves meaningful disagreement, and produces an actionable plan. It explains its choices using evidence, feasibility, and research relevance. Model reputation or agreement can inform attention allocation; neither establishes scientific truth.

**Execute.** A coordinator delegates bounded tasks to workers with the relevant tools. These can include literature retrieval, simulation, data analysis, and figure preparation. Workers return supporting files, methods, observed results, and remaining uncertainties alongside their summaries.

**Review and decide.** Reviewers inspect the work against the question and agreed criteria. The synthesis identifies which concerns require more evidence, which require a local correction, and which need the researcher's judgment. Follow-up work goes to the relevant part of the workflow; a writing concern need not restart a simulation.

The outer loop revisits the research approach. Smaller loops can repair an execution failure, resolve a numerical concern, or improve a report. Each should have a reason, a bounded budget, and an explicit outcome, including an inconclusive result.

## A practical starting architecture

The proposed initial host is Codex, using Subagent Manager for task ownership and handoffs. A small bridge to official model CLIs could bring in external advisory or review sessions. This path has not been implemented or tested in this repository.

Native Codex subagents and external model sessions remain distinct. One proposed pattern is for a native subagent to manage an external advisor task and return its output to the parent. The external advisor receives explicitly selected context; it does not automatically inherit the host's tools, permissions, or conversation. Its internal conversation does not automatically become a native Codex subagent transcript. Stopping the native task also requires checking the external process's actual state.

Start with replaceable choices in advice and review rather than a plugin platform. Possible configurations are:

- **Single:** one model, with separate working and review sessions.
- **Dual:** two models give independent views, followed by synthesis.
- **Exploratory:** a temporarily broader panel investigates a difficult decision within a fixed budget.

These are whole-task starting points, not mandatory tiers for every component. Writing, broad investigation, alternative hypotheses, and tool discovery are optional additions. Assignments should follow the task and observed usefulness rather than permanent model-family occupations.

## Evidence and human judgment

Keep claims connected to their sources or computational outputs. Distinguish a proposed explanation, a reproduced result, and a supported new observation. Independent checks should examine original materials or use another calculation path, rather than merely endorse a worker's summary.

Routine work can proceed within an agreed scope. Changes in scientific direction, substantial resource commitments, and unresolved interpretation should return to the researcher. Stop a loop when its question is answered, its budget is reached, or further progress requires a new decision.

## Related work and first step

[Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y) informs hypothesis generation and critique; [Agent Laboratory](https://arxiv.org/abs/2501.04227) illustrates execution with human feedback; [Paper2Agent](https://www.nature.com/articles/s41586-026-11044-y) offers useful examples of verified tool extraction. These are references, not integrated dependencies.

The first implementation target is one external advisor handoff managed by a reusable Codex subtask, recording the request, visible reply, external session identity, and one follow-up. The next target is a bounded scientific task that connects this handoff to execution and review.
