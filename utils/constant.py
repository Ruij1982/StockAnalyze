import tushare as ts
import pandas as pd


def adjust_output():
    pd.set_option('display.height', 1000)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


FILES_PATH = 'E:/股票数据/'

# 业绩报告
report_path = FILES_PATH + '业绩报告'
report_translation = {
    'code': '代码',
    'name': '名称',
    'eps': '每股收益',
    'eps_yoy': '每股收益同比',
    'bvps': '每股净资产',
    'roe': '净资产收益率',
    'epcf': '每股现金流量',
    'net_profits': '净利润(万元)',
    'profits_yoy': '净利润同比( %)',
    'distrib': '分配方案',
    'report_date': '发布日期',
}
report_func = ts.get_report_data

# 盈利能力
profit_path = FILES_PATH + '盈利能力'
profit_translation = {
    'code': '代码', 'name': '名称', 'roe': '净资产收益率(%)', 'net_profit_ratio': '净利率(%)',
    'gross_profit_rate': '毛利率(%)', 'net_profits': '净利润(万元)', 'eps': '每股收益',
    'business_income': '营业收入(百万元)', 'bips': '每股主营业务收入(元)'
}
profit_func = ts.get_profit_data

# 营运能力
operation_path = FILES_PATH + '营运能力'
operation_translation = {
    'code': '代码', 'name': '名称', 'arturnover': '应收账款周转率(次)', 'arturndays': '应收账款周转天数(天)',
    'inventory_turnover': '存货周转率(次)', 'inventory_days': '存货周转天数(天)', 'currentasset_turnover': '流动资产周转率(次)',
    'currentasset_days': '流动资产周转天数(天)'
}
operation_func = ts.get_operation_data

# 成长能力
growth_path = FILES_PATH + '成长能力'
growth_translation = {
    'code': '代码', 'name': '名称', 'mbrg': '主营业务收入增长率(%)', 'nprg': '净利润增长率(%)', 'nav': '净资产增长率', 'targ': '总资产增长率',
    'epsg': '每股收益增长率', 'seg': '股东权益增长率'
}
growth_func = ts.get_growth_data

# 偿债能力
debtpaying_path = FILES_PATH + '偿债能力'
debtpaying_translation = {
    'code': '代码', 'name': '名称', 'currentratio': '流动比率', 'quickratio': '速动比率', 'cashratio': '现金比率', 'icratio': '利息支付倍数',
    'sheqratio': '股东权益比率', 'adratio': '股东权益增长率'
}
debtpaying_func = ts.get_debtpaying_data

# 现金流量
cashflow_path = FILES_PATH + '现金流量'
cashflow_translation = {
    'code': '代码', 'name': '名称', 'cf_sales': '经营现金净流量对销售收入比率', 'rateofreturn': '资产的经营现金流量回报率', 'cf_nm': '经营现金净流量与净利润的比率',
    'cf_liabilities': '经营现金净流量对负债比率', 'cashflowratio': '现金流量比率'
}
cashflow_func = ts.get_cashflow_data