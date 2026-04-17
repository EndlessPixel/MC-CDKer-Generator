import random
import secrets
import yaml
import os

# 物品池：id / 权重 / 数量区间（闭区间）
POOL = [
    # 下界/末地类
    ("minecraft:netherite_scrap",        10, (1, 3)),
    ("minecraft:netherite_ingot",         6, (1, 2)),
    ("minecraft:ancient_debris",          5, (1, 2)),
    ("minecraft:dragon_breath",           8, (8, 16)),
    ("minecraft:elytra",                  3, (1, 1)),
    ("minecraft:dragon_head",             4, (1, 1)),
    ("minecraft:shulker_shell",           7, (2, 4)),
    ("minecraft:chorus_fruit",            6, (16, 32)),
    ("minecraft:popped_chorus_fruit",     5, (8, 16)),
    ("minecraft:end_crystal",             4, (2, 4)),

    # 海洋/宝藏类
    ("minecraft:heart_of_the_sea",        5, (1, 2)),
    ("minecraft:nautilus_shell",          8, (4, 8)),
    ("minecraft:conduit",                 2, (1, 1)),
    ("minecraft:turtle_helmet",           3, (1, 1)),
    ("minecraft:scute",                   6, (3, 5)),
    ("minecraft:trident",                 3, (1, 1)),
    ("minecraft:prismarine_shard",        7, (12, 24)),
    ("minecraft:prismarine_crystals",     6, (8, 16)),
    ("minecraft:dark_prismarine",         5, (8, 16)),
    ("minecraft:sea_lantern",             4, (4, 8)),

    # 音乐/头颅类
    ("minecraft:music_disc_wait",         3, (1, 1)),
    ("minecraft:music_disc_otherside",    2, (1, 1)),
    ("minecraft:music_disc_5",            2, (1, 1)),
    ("minecraft:creeper_head",            4, (1, 1)),
    ("minecraft:zombie_head",             4, (1, 1)),
    ("minecraft:skeleton_skull",          4, (1, 1)),
    ("minecraft:wither_skeleton_skull",   2, (1, 1)),
    ("minecraft:piglin_head",             3, (1, 1)),

    # 药水/食物类
    ("minecraft:enchanted_golden_apple",  6, (1, 2)),
    ("minecraft:golden_apple",            8, (4, 8)),
    ("minecraft:honey_bottle",            9, (8, 16)),
    ("minecraft:dried_kelp_block",        7, (16, 32)),
    ("minecraft:pumpkin_pie",             8, (12, 24)),

    # 深暗类
    ("minecraft:echo_shard",              6, (3, 6)),
    ("minecraft:sculk_catalyst",          5, (1, 2)),
    ("minecraft:sculk_shrieker",          4, (2, 4)),
    ("minecraft:reinforced_deepslate",    3, (4, 8)),

    # 杂项硬通货
    ("minecraft:emerald",                 9, (16, 32)),
    ("minecraft:diamond",                 7, (8, 16)),
    ("minecraft:gold_ingot",              8, (12, 24)),
    ("minecraft:iron_ingot",              9, (16, 32)),
    ("minecraft:lapis_lazuli",            8, (16, 32)),
    ("minecraft:redstone",                8, (16, 32)),
    ("minecraft:quartz",                  7, (16, 32)),
    ("minecraft:blaze_rod",               7, (8, 16)),
    ("minecraft:ghast_tear",              5, (4, 8)),
    ("minecraft:ender_pearl",             6, (8, 16)),
]

def rand_cdk():
    # 生成20位安全随机 CDK
    return secrets.token_hex(20)[:20]

def gen_one():
    # 按权重随机抽取物品
    item, weight, (min_q, max_q) = random.choices(
        [(i[0], i[1], i[2]) for i in POOL],
        weights=[i[1] for i in POOL]
    )[0]
    qty = random.randint(min_q, max_q)
    return {
        "type": "single",
        "commands": [f"give %player% {item} {qty}"],
        "remainingUses": 1
    }

def main(cnt=100):
    cdk_data = {}
    cdk_list = []

    for _ in range(cnt):
        cdk = rand_cdk()
        cdk_data[cdk] = gen_one()
        cdk_list.append(cdk)

    # 写入 Cdker 插件配置
    with open("new_year_cdk.yml", "w", encoding="utf-8") as f:
        yaml.dump(
            cdk_data, f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False
        )

    # 写入 CDK 列表文本
    with open("cdk_list.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(cdk_list))

    # 输出信息
    print(f"\n✅ 生成完成！共 {cnt} 个 CDK")
    print(f"📄 插件配置：new_year_cdk.yml")
    print(f"📋 CDK 清单：cdk_list.txt")
    print(f"🎯 适用插件：YanPlugins/CDKer")

if __name__ == "__main__":
    main()