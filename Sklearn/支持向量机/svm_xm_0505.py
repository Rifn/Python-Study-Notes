import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


pd.set_option("expand_frame_repr", False)       # 当列太多时不换行

# 设置token
token = '3190dcc1ad6ad420fa7f646fe81e69393d42e9d702995a39b2619d2f'
ts.set_token(token)
pro = ts.pro_api()


# 导入000002.SZ前复权日线行情数据，保留收盘价列
df = ts.pro_bar(ts_code='000002.SZ', adj='qfq', start_date='20190101', end_date='20191231')
df.sort_values('trade_date', inplace=True)
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
df = df[['close']]


# 计算当前、未来1-day涨跌幅
df['1d_future_close'] = df['close'].shift(-1)
df['1d_close_future_pct'] = df['1d_future_close'].pct_change(1)
df['1d_close_pct'] = df['close'].pct_change(1)
df.dropna(inplace=True)
# ====1代表上涨，0代表下跌
df.loc[df['1d_close_future_pct'] > 0, '未来1d涨跌幅方向'] = 1
df.loc[df['1d_close_future_pct'] <= 0, '未来1d涨跌幅方向'] = 0

df = df[['1d_close_pct', '未来1d涨跌幅方向']]
df.rename(columns={'1d_close_pct': '当前1d涨跌幅'}, inplace=True)
# print(df.head())
# exit()


# 创建特征 X 和标签 y
y = df['未来1d涨跌幅方向'].values
X = df.drop('未来1d涨跌幅方向', axis=1).values


# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


# 创建一个支持向量分类器
# linear kernel
# svm = SVC(kernel='linear', C=1, random_state=0)
# RBF kernel
svm = SVC(kernel='rbf', random_state=0, gamma=.01, C=1)

# 放入训练集数据进行学习
svm.fit(X_train, y_train)

# 在测试集数据上进行预测
new_prediction = svm.predict(X_test)
print("Prediction: {}".format(new_prediction))

# 测算模型的表现：预测对的个数 / 总个数
print(svm.score(X_test, y_test))
