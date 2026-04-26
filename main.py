import random
import secrets
import yaml
import datetime
import time
import getpass
import platform

# 读取配置文件
with open("config.yml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

# 基础配置
GEN_COUNT = cfg["generated_quantity"]
CDK_LEN = cfg["cdk_length"]
ITEM_LIST = cfg["item_list"]

# 文件名格式化
def format_filename(s):
    return s.format(
        user_name=getpass.getuser(),
        time=int(time.time()),
        date=datetime.datetime.now().strftime("%Y%m%d"),
        os=platform.system()
    )

YAML_FILE = format_filename(cfg["file"]["yaml"])
TXT_FILE = format_filename(cfg["file"]["text"])

# 生成 CDK
def generate_cdk():
    return secrets.token_hex(CDK_LEN)[:CDK_LEN]

# 随机器物品
def random_item():
    items = list(ITEM_LIST.items())
    weights = [v[0] for v in ITEM_LIST.values()]
    item, val = random.choices(items, weights=weights)[0]
    min_q = val[1]
    max_q = val[2]
    qty = random.randint(min_q, max_q)
    return f"give %player% {item} {qty}"

# 主逻辑
def main():
    cdk_data = {}
    cdk_codes = []
    
    for _ in range(GEN_COUNT):
        code = generate_cdk()
        cmd = random_item()
        cdk_data[code] = {
            "type": "single",
            "commands": [cmd],
            "remainingUses": 1
        }
        cdk_codes.append(code)
    
    # 写入YAML
    with open(YAML_FILE, "w", encoding="utf-8") as f:
        yaml.dump(cdk_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    # 写入纯文本
    with open(TXT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(cdk_codes))
    
    print(f"✅ 生成完成：{GEN_COUNT} 个 CDK")
    print(f"📄 YAML：{YAML_FILE}")
    print(f"📋 文本：{TXT_FILE}")
    print(f"🎯 导入：/cdk import {YAML_FILE} append")

if __name__ == "__main__":
    main()