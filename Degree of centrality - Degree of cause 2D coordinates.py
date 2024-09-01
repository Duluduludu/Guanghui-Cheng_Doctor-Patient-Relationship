import matplotlib as mpl
import matplotlib.pyplot as plt

# 设置图形格式
config = {
            "font.family": 'serif',
            "font.size": 14,
            "mathtext.fontset": 'stix',
            "font.serif": ['SimSun'],
            'axes.unicode_minus': False
          }
mpl.rcParams.update(config)

# 假设的中心度（x轴）和原因度（y轴）数据
x = [8.58, 8.03, 9.46, 9.04, 9.38]  # 请根据你的实际数据替换
y = [-0.34, 0.07, 0.93, 0.94, -1.59]  # 请根据你的实际数据替换

# 因子名
factors_name = [r'信息行为模式', r'信息责权归属', r'制度依据', r'社会形象治理', r'社会伦理']  # 请根据你的实际因子名替换

# 画散点图，并增加相应名称、线段和调整大小和位置
plt.scatter(x, y, s=100, c='k')

plt.xlabel('中心度')
plt.ylabel('原因度')
for i in range(len(x)):
    if i == 0:
        plt.text(x[i] + 0.05, y[i] + 0.05, factors_name[i], fontsize=17)
    elif i == 1:
        plt.text(x[i] + 0.05, y[i] + 0.05, factors_name[i], fontsize=17)
    elif i == 2:
        plt.text(x[i] + 0.05, y[i] + 0.05, factors_name[i], fontsize=17)
    elif i == 3:
        plt.text(x[i] + 0.05, y[i] + 0.05, factors_name[i], fontsize=17)
    else:
        plt.text(x[i] + 0.05, y[i] + 0.05, factors_name[i], fontsize=17)

# 画虚线表示中心度和原因度的平均值
plt.vlines(sum(x)/len(x), min(y)-0.5, max(y)+0.5, colors='k', linestyles='dashed')
plt.hlines(0, min(x)-0.5, max(x)+0.5, colors='k', linestyles='dashed')

# 设置坐标轴范围
plt.xlim(min(x)-0.5, max(x)+0.5)
plt.ylim(min(y)-0.5, max(y)+0.5)

# 添加象限标记
plt.text(max(x)+0.3, max(y)-0.1, 'Ⅰ')
plt.text(min(x)-0.4, max(y)-0.1, 'Ⅱ')
plt.text(min(x)-0.4, min(y)+0.1, 'Ⅲ')
plt.text(max(x)+0.3, min(y)+0.1, 'Ⅳ')

plt.show()
