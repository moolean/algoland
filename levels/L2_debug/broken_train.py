# 修复此文件，让程序输出: training ok
import os

def main():
    # 故意设置为错误键名
    lr = float(os.getenv("LEARN_RATE"))
    if lr < 0:
        raise ValueError("lr must be positive")
    print("training ok")

if __name__ == "__main__":
    main()
