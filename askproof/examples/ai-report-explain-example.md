# AI Report Explain Example

## User Input

```text
AI 说：
Updated the export handler, added a debounce around the click event, and fixed the missing dependency in the PDF renderer. I did not run the full test suite because it is slow.
我看不懂这是什么意思。
```

## AskProof Output

```text
当前判断：Explain｜解释 AI 做了什么

用户真正的问题：
你想知道 AI 到底改了什么，以及能不能相信它已经修好。

AI 当前说法是否可信：
完成可信度：中偏低。AI 说明了修改方向，但也明确说没有运行完整测试。

AI 在说什么：
- 它改了“导出”相关的处理逻辑。
- 它给按钮点击加了防重复触发的处理。
- 它修了 PDF 生成器里缺少依赖的问题。
- 它没有跑完整测试，因为测试耗时。

这对项目意味着什么：
- 如果你的问题和“点击导出 PDF”有关，这些修改可能相关。
- 但“可能相关”不等于“已经确认修好”。

已确认的信息：
- AI 至少说明了三个修改点。
- AI 承认没有运行完整测试。

未确认的信息：
- 导出按钮现在是否真的可用。
- PDF 内容是否正确。
- 是否还有其他页面被影响。

风险点：
- 如果不做一次最小验收，后面继续改功能会掩盖问题来源。

下一步最稳妥动作：
让 AI 不用跑完整测试也可以，但必须给出一个最小验证方式。

可直接复制给 AI 的 Prompt：
请用非工程师能理解的语言说明：这次修改解决的是哪个具体问题？你没有跑完整测试，那请给出一个最小验证步骤，证明导出 PDF 现在能正常工作，并列出仍未验证的风险。

你现在最应该问 AI 的一句话：
请给出一个最小验证步骤，证明这次修改真的解决了导出 PDF 问题，并列出仍未验证的风险。
```

