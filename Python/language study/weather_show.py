import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv', index_col = 'point', encoding = 'euc-kr')
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family = font_name)

city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '전주']]
print(city_df)

ax = city_df.plot(kind = 'bar', title = '날씨', figsize = (12, 4), legend = True, fontsize = 12)
ax.set_xlabel('도시', fontsize = 12)
ax.set_ylabel('기온/습도', fontsize = 12)
ax.legend(['기온', '습도'], fontsize = 12)

plt.show()