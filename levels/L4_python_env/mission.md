# L4 环境炼金术（10~15分钟）

剧情：你要复现实验环境并跑通最小评测。

> 本关要求真实创建 venv、安装依赖并执行脚本。

## 任务
1. 在 `submissions/L4/.venv` 创建虚拟环境并激活。
2. 安装 `player/current/lab/requirements.txt`。
3. 将 `player/current/lab/hparams_bad.yaml` 复制到 `submissions/L4/hparams.yaml`，把 `threshold` 改成 `0.85`。
4. 运行评测脚本（`python player/current/lab/run_eval.py --config submissions/L4/hparams.yaml --out submissions/L4/eval_result.json`）并生成：
   - `submissions/L4/eval_result.json`
   - `submissions/L4/pip_freeze.txt`（`pip freeze > ...`）

完成后执行：
```bash
./scripts/onboard check L4
```
