import numpy as np
from scipy import stats

# 示例数据
x = np.array([40.2, 45.2, 50, 55.2, 60.1, 65, 69.9, 74.9, 80, 85.1])
y = np.array([593, 494, 420, 353, 304, 259, 224, 193, 166, 142])
x = 1 / (x + 273.15)
y = np.log(y)

# 计算线性回归的斜率和截距
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
SE_intercept = std_err * np.sqrt(np.sum(x**2) / len(x))

# 计算95%置信概率的t因子
degrees_of_freedom = len(x) - 2#过原点的自由度是减1
t_factor = stats.t.ppf((1 + 0.95) / 2, degrees_of_freedom)

# 输出结果
print(f"相关系数r: {r_value}")
print(f"1 - r: {1 - r_value}")
print(f"斜率、材料常数、B: {slope}")
print(f"截距: {intercept}")
print(f"斜率的标准差: {std_err}")
print(f"截距的标准差 : {SE_intercept}")
print(f"斜率的不确定度: {t_factor * std_err}")
print(f"截距的不确定度: {t_factor * SE_intercept}")
print(f"极限电阻、A: {np.exp(intercept)}")
print(f"极限电阻、A的不确定度: {np.exp(intercept)*t_factor * SE_intercept}")
print(f"50度电阻温度系数: {0 - slope / (273.15 + 50)**2}")
print(f"50度电阻温度系数的不确定度: {t_factor * std_err/(273.15 + 50)**2}")