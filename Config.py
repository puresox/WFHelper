from utils.ImageUtil import *

class Config():
    targets = [
        {
            "path" : "template\lingdang.png",
            "area" : (30,157,111,237),
            "text" : "发现铃铛，点击"
        },
        {
            "path" : "template\lingdang2.png",
            "area" : (0,272,103,429),
            "text" : "发现铃铛，点击"
        },
        {
            "path" : "template\canjia.png",
            "area" : (557,1792,1000,1906),
            "text" : "点击参加按钮"
        },
        {
            "path" : "template\canjia2.png",
            "area" : (496,1985,859,2076),
            "text" : "点击参加按钮"
        },
        {
            "path" : "template\zhunbei.png",
            "area" : (311,1567,770,1710),
            "text" : "点击准备按钮"
        },
        {
            "path" : "template\OK.png",
            "area" : (316,1422,760,1528),
            "text" : "蹭车失败，点击OK"
        },
        {
            "path" : "template\OK2.png",
            "area" : (372,2000,705,2089),
            "text" : "任务结束，点击OK"
        },
        {
            "path" : "template\jixu.png",
            "area" : (368,1995,711,2090),
            "text" : "点击继续"
        },
        {
            "path" : "template\likai.png",
            "area" : (151,1996,493,2090),
            "text" : "离开房间"
        },
        {
            "path" : "template\jixuguanka.png",
            "area" : (563,1429,1003,1533),
            "text" : "继续关卡"
        },
        {
            "path" : "template\shengji.png",
            "area" : (322,1089,794,1250),
            "text" : "升级了！"
        },
        {
            "path" : "template\shengji2.png",
            "area" : (309,1082,770,1145),
            "text" : "升级了！"
        },
        {
            "path" : "template\jiantou.png",
            "area" : (938,305,990,385),
            "text" : "点击箭头，返回游戏"
        }
    ]

    def __init__(self):
        for target in self.targets:
            img = getImageCrop(target["path"],target["area"])
            target["hash"] = getImageHash(image=img)

    