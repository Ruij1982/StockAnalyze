import pandas as pd
import numpy as np
import tushare as ts

from datetime import datetime


class Growth:
    def __init__(self, file):
        self.encoding = 'gbk'
        self.file = file
        self.df = pd.read_csv(file, encoding=self.encoding)

    def analyse_lirun(self, year=datetime.now().year-1, duration=3, growth=30, save=True):
        data = self._analyse_by_year(year=year, duration=duration, col='净利润增长率', growth=growth)
        if save:
            self.to_csv(data, '净利润增长分析.csv')

    def analyse_zhuying(self, year=datetime.now().year-1, duration=3, growth=30, save=True):
        data = self._analyse_by_year(year=year, duration=duration, col='主营业务收入增长率', growth=growth)
        if save:
            self.to_csv(data, '主营业务收入增长分析.csv')

    def analyse_meigu(self, year=datetime.now().year-1, duration=3, growth=30, save=True):
        data = self._analyse_by_year(year=year, duration=duration, col='每股收益增长率', growth=growth)
        if save:
            self.to_csv(data, '每股收益增长分析.csv')

    def _analyse_by_year(self, year, duration, col, growth):
        # 待分析年份数据
        years = [year - i for i in range(duration)]
        columns = ['代码', '名称'] + [col]

        result = None
        for year in years:
            condition = (self.df.年 == year) & (self.df.季度 == 4) & (self.df[col] >= growth)
            data = self.df[condition][columns]
            data.rename(columns={col: col + '_' + str(year)}, inplace=True)

            if result is None:
                result = data
            else:
                result = result.merge(data, on=['代码', '名称'])

        return result.sort_values(by='代码')

    def to_csv(self, df, name):
        df.to_csv(name, encoding=self.encoding, index=False)


if __name__ == "__main__":
    path = 'E:\\PycharmProjects\\Tushare\\data\\'
    growth = Growth(path + 'growth_data.csv')
    # growth.analyse_lirun()
    growth.analyse_zhuying()
    growth.analyse_meigu()