# Codex Done Check Example

## Fictional Context

Tool: Codex

Project: InvoicePad, a small internal invoice tool.

## User Input

```text
Codex 说：
Implemented the invoice total fix and ran python3 -m py_compile on the edited scripts. The check passed.
```

## AskProof Output

```text
当前判断：Done Check｜完成验收

用户真正的问题：
你想知道这个通过的检查，是否真的证明发票金额问题已经修好。

AI 当前说法是否可信：
完成可信度：中。它提供了一个通过的技术检查，但这个检查可能只证明脚本语法没错，不一定证明发票金额正确。

已确认的信息：
- AI 声称实现了发票总额修复。
- AI 运行了 python3 -m py_compile。
- 该语法检查通过。

未确认的信息：
- 是否用真实示例发票验证过金额。
- 税费、折扣、四舍五入是否正确。
- 页面或导出文件中的金额是否正确显示。

风险点：
- 语法通过不等于业务结果正确。非工程师最关心的是“金额有没有算对”。

下一步最稳妥动作：
让 AI 给出一个业务验收用例，而不是只给技术检查。

可直接复制给 AI 的 Prompt：
Please clarify whether your verification proves the original user-facing problem is fixed, or only proves that the edited files compile. List the remaining manual acceptance checks before we continue.

你现在最应该问 AI 的一句话：
请说明 py_compile 只能证明什么、不能证明什么，并给出一个能验证发票金额正确的最小业务验收用例。
```

