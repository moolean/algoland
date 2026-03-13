import argparse, json, yaml

p = argparse.ArgumentParser()
p.add_argument("--config", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()

cfg = yaml.safe_load(open(args.config, "r", encoding="utf-8"))
base = float(cfg.get("base_score", 0.0))
th = float(cfg.get("threshold", 1.0))
status = "PASS" if base >= th else "FAIL"

with open(args.out, "w", encoding="utf-8") as f:
    json.dump({"base_score": base, "threshold": th, "status": status}, f, ensure_ascii=False)

print(status)
