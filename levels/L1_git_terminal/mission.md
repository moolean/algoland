# L1 数据考古学家（15~20分钟）

剧情：你接手了一个实验仓库，需要从训练日志里恢复关键信息，并做一次合规 Git 提交。

> 本关要求你**真实运行终端命令**完成任务（grep/awk/sort/cp/sed/git）。

## 任务

1. 从 `player/current/lab/experiments.log` 找出 `val_loss` 最小的一行，输出到：
   - `submissions/L1/best_run.txt`
   - 内容必须是原始整行（不要手写猜测）

2. 统计 `player/current/lab/train.err.log` 的错误类型出现次数（按次数倒序），输出前2名到：
   - `submissions/L1/error_top2.txt`
   - 每行格式：`<error_type> <count>`（例如 `OOM 3`）

3. 修复配置文件：
   - 复制 `player/current/lab/configs/model_bad.yaml` 到 `submissions/L1/model_fixed.yaml`
   - 将其中 `lr` 改为 `0.001`
   - 将其中 `batch_size` 改为 `32`

4. Git 操作要求（在本仓库执行）：
   - 新建并切换分支：`feat/onboarding-l1`
   - 至少 2 次 commit
   - 其中一次 commit message 必须包含：`L1 complete`

完成后执行：
```bash
./scripts/onboard check L1
```
