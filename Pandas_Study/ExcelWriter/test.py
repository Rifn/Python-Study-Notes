import pandas as pd
import numpy as np


writer = pd.ExcelWriter("./demo.xlsx")

'''创建数据框1'''
df1 = pd.DataFrame({'V1': np.random.rand(100),
                    'V2 ': np.random.rand(100),
                    'V3': np.random.rand(100)})
# df1.to_excel(writer, sheet_name='sheet1', index=False)

'''创建数据框2'''
df2 = pd.DataFrame({'V1': np.random.rand(100),
                    'V2 ': np.random.rand(100),
                    'V3': np.random.rand(100)})
# df2.to_excel(writer, sheet_name='sheet2', index=False)

'''创建数据框3'''
df3 = pd.DataFrame({'V1': np.random.rand(100),
                    'V2 ': np.random.rand(100),
                    'V3': np.random.rand(100)})
# df3.to_excel(writer, sheet_name='sheet3', index=False)

list1 = [df1, df2, df3]
i = 1
for df in list1:
    m = "sheet" + str(i)
    df.to_excel(writer, sheet_name=m, index=False)
    i = i + 1

'''数据写出到excel文件中'''
writer.save()
