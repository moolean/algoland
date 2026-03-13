# L2 午夜训练崩溃（20~30分钟）

剧情：夜间训练任务崩了，你是值班工程师，需要在30分钟内恢复训练。

> 本关要求真实执行终端命令与代码修复。

## 任务
1. 从 `player/current/lab/train_crash.log` 提取最终报错行（`TypeError...`），输出到：
   - `submissions/L2/root_cause_line.txt`
2. 修复 `player/current/broken_train.py`，使以下命令成功输出 `training ok`：
   - `LEARNING_RATE=0.001 python player/current/broken_train.py`
3. 将运行结果保存到：
   - `submissions/L2/run_output.txt`
4. 在仓库内切换分支 `feat/onboarding-l2`，并提交至少1次（message 包含 `L2 complete`）

完成后执行：
```bash
./scripts/onboard check L2
```
