# Cursor Done Check Example

## Fictional Context

Tool: Cursor

Project: ShopLite, a small checkout demo.

## User Input

```text
Cursor 说：
Fixed the checkout button bug in CheckoutButton.tsx. It should work now.
```

## AskProof Output

```text
当前判断：Done Check｜完成验收

用户真正的问题：
你想知道 Cursor 改了按钮代码后，是否真的证明结账按钮可以用了。

AI 当前说法是否可信：
完成可信度：低。它提到了一个文件，但没有说明是否打开页面、点击按钮或看到正确结果。

已确认的信息：
- AI 声称修改了 CheckoutButton.tsx。
- AI 声称 checkout button bug 已修复。

未确认的信息：
- 是否运行了项目预览。
- 是否点击过结账按钮。
- 是否确认原来的错误消失。
- 是否检查了页面或浏览器控制台是否还有报错。

风险点：
- 这可能只是代码层面的修改，不一定证明用户真的能完成结账流程。

下一步最稳妥动作：
让 AI 把“改了文件”和“验证了用户流程”分开说明。

可直接复制给 AI 的 Prompt：
Please do not continue editing yet. Show the files you changed, the exact user flow you verified in the app preview, the observed result, and anything still unverified. If you did not open the preview or reproduce the original issue, mark it as unverified.

你现在最应该问 AI 的一句话：
请先证明结账按钮在页面里真的可用，说明你改了哪些文件、验证了哪个用户流程、看到了什么结果，以及哪些仍未验证。
```

