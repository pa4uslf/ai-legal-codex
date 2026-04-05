# 项目导航

## 项目目的

这是一个面向 Codex 的法律助手技能仓库，用于：
- 审阅合同并输出风险分析
- 生成 NDA、条款、隐私政策和常见商业协议
- 生成 PDF 法律审查报告

## 关键目录

- `legal/SKILL.md`：主路由 skill，负责把法律相关请求分发到具体子 skill
- `skills/`：13 个具体子 skill
- `agents/`：5 份分析框架文档，供完整合同审查时按不同视角复用
- `scripts/generate_legal_pdf.py`：PDF 生成脚本
- `templates/contract-review-template.md`：合同审查报告模板
- `install.sh` / `uninstall.sh`：Codex 安装与卸载脚本

## 推荐阅读顺序

1. `README.md`
2. `legal/SKILL.md`
3. 目标子 skill，例如 `skills/legal-review/SKILL.md`
4. 如涉及完整审查，再看 `agents/*.md`
5. 如涉及 PDF，再看 `scripts/generate_legal_pdf.py`

## 当前适配说明

- 仓库已按 Codex skill 目录约定调整，目标安装位置为 `~/.codex/skills`
- `/legal ...` 示例仍保留作用户提示，但 Codex 中也支持自然语言触发
- `agents/` 中的文档在 Codex 里视为“分析框架提示”，不是必须自动并行执行的运行时代理
