# MC-CDKer-Generator
Minecraft CDK 礼包批量生成工具  
**适配 YanPlugins/CDKer 插件**

## 介绍
一键生成带**权重随机物品**的 CDK 兑换码，  
自动生成 YAML 配置 + 纯文本 CDK 列表，  
适合服务器：节日活动、福利发放、压测、礼包码运营。

## 功能
- 20 位高强度随机 CDK
- 物品带**权重概率**
- 物品数量**随机区间**
- 直接生成 Cdker 插件可用的 yml 配置
- 自动导出 CDK 清单文本（方便发放）
- 内置海量精品物品（下界、末地、深海、深暗之域）

## 支持插件
原插件仓库：  
https://github.com/YanPlugins/CDKer

## 使用方法
1. 安装依赖
```bash
pip install pyyaml
```
2. 运行脚本
```bash
python generate_cdk.py
```
3. 得到两个文件
- `new_year_cdk.yml` → 放入 Cdker 插件
- `cdk_list.txt` → 礼包码列表

## 适用场景
- 服务器节日活动
- 玩家福利礼包
- 开服庆典
- 运营批量礼包

## 物品池包含
- 下界合金 / 远古残骸
- 鞘翅、龙息、龙首
- 海洋之心、导管、三叉戟
- 附魔金苹果、金苹果
- 回响碎片、循声守御
- 钻石、绿宝石、稀有物资