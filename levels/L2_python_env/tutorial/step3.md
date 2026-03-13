# Step 3/3 - 教学：为什么要 freeze 环境

## 任务速览
- 导出当前环境依赖到 `out/pip_freeze.txt`
- 确认关键依赖版本在文件里

## 这一步你在学什么
“我这边能跑、你那边不能跑” 很多时候是环境差异造成的。

`pip freeze` 的作用，就是把当前环境安装的包版本完整记录下来。
它像给环境拍快照。

## 本步任务
导出当前环境依赖到：
- `out/pip_freeze.txt`

## 你会用到的命令
### `pip freeze`
列出当前环境中所有包和对应版本。

### `head` / `grep`
快速查看你关心的内容是否真的写进去了。

## 这一步的关键点
一定要在**正确激活的 venv** 里执行。
否则 freeze 到的是别的环境，就没意义了。

## 自检
你可以执行：
```bash
head -n 20 out/pip_freeze.txt
grep -E 'rich|PyYAML' out/pip_freeze.txt
```
看看关键依赖是否存在。

完成后执行：
```bash
./quest submit
```
