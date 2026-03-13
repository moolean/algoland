# Step 1/3 - 教学：为什么每个 Python 项目都该有自己的环境

## 任务速览
- 在 `out/.venv` 创建虚拟环境
- 激活它，并确认当前 `python` 指向这个环境

## 这一步你在学什么
很多 Python 问题其实不是“代码错了”，而是：
- 这个项目用的包版本和另一个项目冲突
- 你以为自己在用项目环境，其实在用系统 Python
- pip 把包装到了错误的位置

`venv` 的作用，就是给当前项目创建一个隔离环境。

## 本步任务
在：
- `out/.venv`

创建虚拟环境并激活。

## 你会用到的命令
### 1) `python3 -m venv <目录>`
创建虚拟环境。

### 2) `source <目录>/bin/activate`
激活虚拟环境。

激活后常见变化：
- 命令行前面可能出现 `(.venv)`
- `python` 和 `pip` 会指向这个环境里的版本

### 3) `which python`
看当前到底在用哪个 python。
这在排查环境问题时非常重要。

## 建议你自己观察
激活前后分别运行：
```bash
which python3 || true
which python || true
```

激活后再看一次，就能体会“路径变了”是什么意思。

## 自检
激活完成后：
```bash
which python
python -V
```
确认路径里包含 `.venv`。

完成后执行：
```bash
./quest submit
```
