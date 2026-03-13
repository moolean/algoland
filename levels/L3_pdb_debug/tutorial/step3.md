# Step 3/3 - 教学：修复 JSONL 实验汇总脚本，让报告选出正确 best run

## 任务速览
- 复制 `lab/batch_report_bug.py` 到 `out/batch_report_fixed.py`
- 修复它，让脚本正确输出最佳实验
- 把运行结果写入 `out/final_report.txt`

## 这一步你在学什么
算法工作里，很多问题不在模型本身，
而在**离线分析脚本把实验结果汇总错了**。

这一步模拟的就是这种场景：
- 实验结果已经落在 JSONL 里
- 读取逻辑没问题
- 但“best run” 的挑选条件写反了
- 最终报告会把最差实验当成最好实验

## 核心概念
### 1) 这题里的脚本在做什么
脚本会：
- 读取 `experiment_results.jsonl`
- 逐行解析每个 run 的指标
- 选出最佳实验
- 生成最终报告

### 2) 这种 bug 为什么常见
真实工作里，
大家更容易关注模型训练本身，
却忽略最后这层结果汇总代码。

结果是：
- 指标都算对了
- 但 best run 挑错了
- 后面的结论和汇报都会跟着错

### 3) 这一步练什么
这一步不是让你自己写 JSONL 处理器，
而是让你接手已有脚本，把它改通。

## 本步任务
请你自己完成这条链路：
- 复制 `lab/batch_report_bug.py`
- 在副本里修复 best run 选择逻辑
- 运行修复后的脚本
- 把结果写入 `out/final_report.txt`

## 自检
提交前确认：
```bash
python out/batch_report_fixed.py
cat out/final_report.txt
```

最终结果应清楚表明：
- `best=run_a`
- `val_score=0.873`

完成后执行：
```bash
./quest submit
```
