import os


"""
可以参考对 上市企业的聚类任务 项目中的 test 文件中对这个问题的实际应用
"""
# path = '制造业'

if not os.path.exists("test.py"):  # 如果没有输入全路径，那么判断则是在当前文件夹下进行
    print('不存在')
else:
    print('存在')

os.mkdir('第一个测试文件夹')  # 创建文件夹
os.makedirs('第二个测试文件夹/第三个测试文件夹')  # 创建子文件夹
os.makedirs('第二个测试文件夹/第四个测试文件夹')  # 重复创建子文件夹
# text1 = '制造业聚类结果_测试/'
# for ind in rk.ind_code_list:
#     text2 = rk.ind_name_list[rk.ind_code_list.index(ind)]
#     path = text1 + ind + text2
#     os.makedirs(path)

