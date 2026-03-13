# L3 安全隧道员（10~15分钟）

剧情：你需要为训练节点配置 SSH 连接（在隔离环境中完成）。

> 本关要求真实执行 ssh-keygen / ssh 命令。

## 任务
1. 生成密钥：
   - `submissions/L3/.ssh/id_ed25519`（空 passphrase）
2. 创建 SSH 配置 `submissions/L3/.ssh/config`，包含别名：`train-node`
   - HostName 127.0.0.1
   - User trainee
   - Port 2222
   - IdentityFile 指向上面的私钥
3. 运行：
   - `ssh -F submissions/L3/.ssh/config -G train-node > submissions/L3/ssh_effective.txt`
4. 提取 effective config 中的 `hostname/user/port` 三行到：
   - `submissions/L3/ssh_summary.txt`

完成后执行：
```bash
./scripts/onboard check L3
```
