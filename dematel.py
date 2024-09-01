import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import font_manager as fm

# 设置中文字体
font_path = 'C:/Windows/Fonts/simhei.ttf'  # Windows 示例路径，请根据实际字体文件路径修改
prop = fm.FontProperties(fname=font_path)
plt.rcParams.update({'font.size': 16})  # 调整全局字体大小
# 定义直接影响矩阵 A（假设为5x5方阵）
A = np.array([[0, 3, 3.25, 4.75, 5.5],
              [3, 0, 5, 3.25, 4.75],
              [5.5, 6.25, 0, 4, 6.25],
              [4, 5, 5, 0, 6.75],
              [5.25, 2, 4, 4, 0]])

# 规范化直接影响矩阵 A
row_sum = np.sum(A, axis=1)
max_sum = np.max(row_sum)
B = A / max_sum

# 计算综合影响矩阵 T
I = np.identity(A.shape[0])
T = np.matmul(B, np.linalg.inv(I - B))

# 计算影响度 D，被影响度 C，中心度 M，原因度 R
D = np.sum(T, axis=1)
C = np.sum(T, axis=0)
M = D + C
R = D - C

# 将影响度、被影响度、中心度、原因度输出为表格
results_df = pd.DataFrame({
    '影响度 (D)': D,
    '被影响度 (C)': C,
    '中心度 (M)': M,
    '原因度 (R)': R
})

# 输出表格到CSV文件
results_df.to_csv('dematel_results.csv', index=False, encoding='utf-8-sig')


# 可视化
# 1. 直接影响矩阵 A
plt.figure(figsize=(8, 6))
sns.heatmap(A, annot=True, cmap="YlGnBu", cbar=True, annot_kws={"size": 14}, 
            xticklabels=np.arange(1, A.shape[1] + 1), yticklabels=np.arange(1, A.shape[0] + 1), fmt='.2f')  # 设置坐标轴刻度为1-5
plt.title("直接影响矩阵 A", fontproperties=prop, fontsize=18)
plt.savefig('直接影响矩阵_A.png')
plt.show()

# 2. 规范影响矩阵 B
plt.figure(figsize=(8, 6))
sns.heatmap(B, annot=True, cmap="YlGnBu", cbar=True, annot_kws={"size": 14}, 
            xticklabels=np.arange(1, B.shape[1] + 1), yticklabels=np.arange(1, B.shape[0] + 1))
plt.title("规范影响矩阵 B", fontproperties=prop, fontsize=18)
plt.savefig('规范影响矩阵_B.png')
plt.show()

# 3. 综合影响矩阵 T
plt.figure(figsize=(8, 6))
sns.heatmap(T, annot=True, cmap="YlGnBu", cbar=True, annot_kws={"size": 14}, 
            xticklabels=np.arange(1, T.shape[1] + 1), yticklabels=np.arange(1, T.shape[0] + 1))
plt.title("综合影响矩阵 T", fontproperties=prop, fontsize=18)
plt.savefig('综合影响矩阵_T.png')
plt.show()

# 4. 影响度 D
plt.figure(figsize=(8, 6))
sns.barplot(x=np.arange(1, len(D) + 1), y=D, hue=np.arange(1, len(D) + 1), palette="viridis", dodge=False)
plt.title("影响度 D", fontproperties=prop, fontsize=18)
plt.xticks(np.arange(1, len(D) + 1), fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('影响度_D.png')
plt.show()

# 5. 被影响度 C
plt.figure(figsize=(8, 6))
sns.barplot(x=np.arange(1, len(C) + 1), y=C, hue=np.arange(1, len(C) + 1), palette="viridis", dodge=False)
plt.title("被影响度 C", fontproperties=prop, fontsize=18)
plt.xticks(np.arange(1, len(C) + 1), fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('被影响度_C.png')
plt.show()

# 6. 中心度 M
plt.figure(figsize=(8, 6))
sns.barplot(x=np.arange(1, len(M) + 1), y=M, hue=np.arange(1, len(M) + 1), palette="viridis", dodge=False)
plt.title("中心度 M", fontproperties=prop, fontsize=18)
plt.xticks(np.arange(1, len(M) + 1), fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('中心度_M.png')
plt.show()

# 7. 原因度 R
plt.figure(figsize=(8, 6))
sns.barplot(x=np.arange(1, len(R) + 1), y=R, hue=np.arange(1, len(R) + 1), palette="viridis", dodge=False)
plt.title("原因度 R", fontproperties=prop, fontsize=18)
plt.xticks(np.arange(1, len(R) + 1), fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('原因度_R.png')
plt.show()
