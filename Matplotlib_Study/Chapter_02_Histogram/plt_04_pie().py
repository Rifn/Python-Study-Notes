# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

"""
函数功能：绘制定性数据的不同类别的百分比
调用签名：plt.pie(x)
x: 定性数据的不同类别的百分比
"""

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 配置字体，显示中文
mpl.rcParams["axes.unicode_minus"] = False  # 配置坐标轴刻度值模式，显示负号

kinds = "简易箱", "保温箱", "行李箱", "密封箱"  # 此处数据类型不管是定义成元组还是列表
# 都不影响图形的最终绘制，但是当print(kinds)时，打印出来的是元组形式

colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]  # 设置颜色

# 定义数据 get data
soldNums = [0.05, 0.45, 0.15, 0.35]  # 这个soldNums就是饼图函数中的x，用于传递数据

# 绘制饼图 pie chart  // 以下所有参数的定义，既可以先定义，再传递进函数，也可直接在函数括号内定义
plt.pie(soldNums,
        labels=kinds,
        colors=colors,
        startangle=60,  # 该参数是指定起始角度，以极坐标系为基准，逆时针绘制各个类别
        # 当然，当counterclock参数为False时，逆时针绘制
        autopct="%3.1f%%")  # autopct是用来设置百分比信息的字符串格式化方式，默认值为None，不显示百分比
# 上面小数点后的数字代表显示小数点后的位数，适当修改小数点前的位置对程序运行无影响

plt.title("不同类型箱子的销售数量占比")

plt.show()
