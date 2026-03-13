# L5 双模型调度官（15~20分钟）

剧情：你要验证“官方 API”和“自部署 API”的可用性，并记录重试行为。

> 本关要求真实启动 mock 服务，并用命令完成调用与重试。

## 任务
1. 启动 mock 服务（保持后台运行）：
   - `python player/current/lab/mock_api.py`
2. 分别请求：
   - `http://127.0.0.1:8765/official`
   - `http://127.0.0.1:8765/selfhost`
3. 对每个 endpoint 实现“失败后重试直到成功”（至少体现一次 retry）。
4. 将每次请求写入：`submissions/L5/requests_log.jsonl`
   - 每行 JSON 至少包含：`endpoint`、`attempt`、`status`
5. 生成 `submissions/L5/summary.md`，简述两类 API 调用差异（至少2点）。

完成后执行：
```bash
./scripts/onboard check L5
```
