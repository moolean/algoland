# Step 1/2 - 教学：把现成示例代码改到同时支持两种 API 风格

## 任务速览
- 修改 `lab/api_client.py`
- 让 OpenAI 风格调用正常返回
- 让 Anthropic 风格调用也正常返回

## 这一步你在学什么
这一关不要求你从零写 API 调用器。

题目已经给了你一份示例代码：
- `lab/api_client.py`

你要做的是读懂它，然后把其中写错的地方改对。

## 核心概念
### 1) 这份代码已经帮你做好了什么
示例代码已经帮你处理了：
- 发送 POST 请求
- JSON 序列化
- 读取响应

所以这一步的重点不是写网络代码，
而是看懂：
- URL 对不对
- headers 对不对
- body 字段对不对
- 返回值提取对不对

### 2) OpenAI 风格和 Anthropic 风格哪里不同
你要重点注意两类差异：
- 请求头不同
- 返回 JSON 结构不同

OpenAI 风格常看：
- `choices[0].message.content`

Anthropic 风格常看：
- `content[0].text`

### 3) 这一步怎么做
你不需要重写整份文件。
先直接运行它，看看哪里报错、哪里返回结构不匹配，
再做最小修改。

## 本步任务
请你修改 `lab/api_client.py`，让下面两段调用都跑通：
- `call_openai_once()`
- `call_anthropic_once()`

本关会在后台自动记录你是否真的调对，
你不需要额外生成结果文件。

## 自检
这一步不要直接跑整份文件，先只跑当前需要验证的入口：
```bash
python lab/run_step1.py
```

至少要确保：
- `openai:` 后面能正常返回文本
- `anthropic:` 后面也能正常返回文本
- 不再因为请求头或返回字段写错而报错

完成后执行：
```bash
./quest submit
```
