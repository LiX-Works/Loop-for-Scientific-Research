# Loop for Scientific Research

> **v0.01 · 概念预览。** 这是一个正在逐步完善的项目规划与架构提案，可执行集成尚待建设。

**将不同 AI 的独立观点，接入由证据推动的科研循环。**

一个正在规划中的科研 Agent 工作流：理解问题、比较方案、执行任务、审视证据，再决定下一步。研究者确定方向，并作出科学判断。

![拟议科研循环：理解上下文、独立研判、综合、执行、审核与定向迭代](assets/overview.svg)

本版包含简短设计说明、上图的可编辑源代码，以及三份手工交接模板。

## 这个循环用来做什么

- **获得独立观点。** 各模型先分别研判，再由可替换的综合者比较方案，保留尚未解决的分歧。
- **连接思考与执行。** 执行团队调用已有工具，完成文献、仿真、分析、绘图等工作。
- **根据证据推进。** 审核者检查结果及其依据，提出具体补充任务，或整理成供研究者决策的材料。

各部分可以分别调整。从小规模的研判与审核团队开始，按问题需要加入发散探索、写作、广泛调研或工具发现。模型承担的职责也可以随任务改变。

## 从交接开始

三个模板可用于手工试跑：填写[研究任务简报](templates/research-brief.md)，收集[研判意见](templates/advisor-memo.md)，记录[审核与下一步](templates/review-and-next-step.md)。

拟从 Codex 与 Subagent Manager 起步，通过少量官方 CLI 连接外部顾问。这条连接路径尚未在本项目实现和测试，详见[设计说明](docs/design.md)。

**下一步：** 通过一个可续派的 Codex 子任务连接外部顾问，保留请求、回复与后续追问，再扩展为小型执行与审核循环。

相关独立项目：[Subagent Manager](https://github.com/LiX-Works/subagent-manager)、[COMSOL 工作流](https://github.com/LiX-Works/COMSOL-Agent-Research-Workflow)、[ScholarFetch](https://github.com/LiX-Works/ScholarFetch)、[Origin 绘图](https://github.com/LiX-Works/Origin_MCP-Skill_for_Scientific-Plots)。它们在本项目中的集成仍属规划。

[English](README.md) · [MIT 许可证](LICENSE)
