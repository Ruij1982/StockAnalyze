import pandas as pd
import numpy as np
import tushare as ts

from utils.common import get_year_and_quarter


def get_report_data(data_name='report_data.csv', start=2010, end=2018):
    report_mapping = {
        'code': '代码',
        'name': '名称',
        'eps': '每股收益',
        'eps_yoy': '每股收益同比',
        'bvps': '每股净资产',
        'roe': '净资产收益率',
        'epcf': '每股现金流量',
        'net_profits': '净利润(万元)',
        'profits_yoy': '净利润同比',
        'distrib': '分配方案',
        'report_date': '发布日期',
    }
    data = _get_ts_data(ts.get_report_data, start, end, report_mapping)
    data.to_csv(data_name, index=False, encoding='gbk')


def get_profit_data(data_name='profit_data.csv', start=2010, end=2018):
    profit_mapping = {
        'code': '代码',
        'name': '名称',
        'roe': '净资产收益率',
        'net_profit_ratio': '净利率',
        'gross_profit_rate': '毛利率',
        'net_profits': '净利润(万元)',
        'eps': '每股收益',
        'business_income': '营业收入(百万元)',
        'bips': '每股主营业务收入(元)'
    }
    data = _get_ts_data(ts.get_profit_data, start, end, profit_mapping)
    data.to_csv(data_name, index=False, encoding='gbk')


def get_operation_data(data_name='operation_data.csv', start=2010, end=2018):
    operation_mapping = {
        'code': '代码', 'name': '名称', 'arturnover': '应收账款周转率', 'arturndays': '应收账款周转天数',
        'inventory_turnover': '存货周转率', 'inventory_days': '存货周转天数', 'currentasset_turnover': '流动资产周转率',
        'currentasset_days': '流动资产周转天数'
    }
    data = _get_ts_data(ts.get_operation_data, start, end, operation_mapping)
    data.to_csv(data_name, index=False, encoding='gbk')


def get_growth_data(data_name='growth_data.csv', start=2010, end=2018):
    growth_mapping = {
        'code': '代码', 'name': '名称', 'mbrg': '主营业务收入增长率', 'nprg': '净利润增长率', 'nav': '净资产增长率',
        'targ': '总资产增长率', 'epsg': '每股收益增长率', 'seg': '股东权益增长率'
    }
    data = _get_ts_data(ts.get_growth_data, start, end, growth_mapping)
    data.to_csv(data_name, index=False, encoding='gbk')


def get_debtpaying_data(data_name='debtpaying_data.csv', start=2010, end=2018):
    debtpaying_mapping = {
        'code': '代码', 'name': '名称', 'currentratio': '流动比率', 'quickratio': '速动比率', 'cashratio': '现金比率',
        'icratio': '利息支付倍数', 'sheqratio': '股东权益比率', 'adratio': '股东权益增长率'
    }
    data = _get_ts_data(ts.get_debtpaying_data, start, end, debtpaying_mapping)
    data.to_csv(data_name, index=False, encoding='gbk')


def get_cashflow_data(data_name='cashflow_data.csv', start=2010, end=2018):
    cashflow_mapping = {
        'code': '代码', 'name': '名称', 'cf_sales': '经营现金净流量对销售收入比率', 'rateofreturn': '资产的经营现金流量回报率',
        'cf_nm': '经营现金净流量与净利润的比率', 'cf_liabilities': '经营现金净流量对负债比率', 'cashflowratio': '现金流量比率'
    }
    data = _get_ts_data(ts.get_cashflow_data, start, end, cashflow_mapping)
    data.to_csv(data_name, index=False, encoding='gbk')


def _get_ts_data(ts_func, start, end, columns_mapping):
    dfs = []
    for year, quarter in get_year_and_quarter(start, end):
        df = ts_func(year, quarter)
        df.code = df.code.astype(np.str)
        df['年'] = year
        df['季度'] = quarter
        df.rename(columns=columns_mapping, inplace=True)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


if __name__ == "__main__":
    # get_report_data()
    # get_profit_data()
    # get_operation_data()
    # get_growth_data()
    # get_debtpaying_data()
    get_cashflow_data()
