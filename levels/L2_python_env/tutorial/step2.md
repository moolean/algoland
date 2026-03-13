# Step 2/3 - 教学：装依赖、改配置、跑脚本

## 任务速览
- 安装 `lab/requirements.txt`
- 复制并修复 `out/hparams.yaml`，把 `threshold` 改成 `0.85`
- 运行评测，生成 `out/eval_result.json`

## 这一步你在学什么
一个非常真实的工作流：
- 环境准备好了吗？
- 依赖装对了吗？
- 配置改对了吗？
- 脚本真的跑通了吗？

很多“训练跑不起来”“评测结果不对”，最后问题都出在这四个环节之一。

## 本步任务
1. 安装 `lab/requirements.txt`
2. 复制 `lab/hparams_bad.yaml` 到 `out/hparams.yaml`
3. 把 `threshold` 改成 `0.85`
4. 运行评测并生成 `out/eval_result.json`

## 你会用到的命令
### 1) `pip install -r 文件`
按依赖文件安装包。

### 2) `cp`
复制配置文件。

### 3) `vim`
编辑配置。

### 4) `python 脚本 --config ... --out ...`
运行脚本并把结果写到指定文件。

## 先理解这个任务为什么存在
原始配置里的阈值是故意写错的。
你的工作不是“瞎试”，而是：
- 先理解配置参数会影响结果
- 再按要求修到正确值
- 最后用输出文件验证结果

## 建议顺序
1. 确认 venv 已激活
2. 安装依赖
3. 复制并修改配置
4. 运行脚本
5. 自己 `cat out/eval_result.json` 看结果

## 自检
结果里应满足：
- `threshold` 是 `0.85`
- `status` 是 `PASS`

完成后执行：
```bash
./quest submit
```
