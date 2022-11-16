# 首先安装xlrd包    pip install xlrd
# 执行文件报错：XLRDError: Excel xlsx file; not supported
# 需要降低xlrd版本
# pip uninstall xlrd
# pip install xlrd==1.2.0

import xlrd


def xlxs_read(name, index):
    excel = xlrd.open_workbook(name)  # 打开一个xlsx文件
    sheet = excel.sheets()[index]  # 打开第一个sheet页
    # sheet = word.sheet_by_name('管理控制台')   #根据sheet页名称或id切换
    # sheet = word.sheet_by_index(0)
    return sheet


if __name__ == '__main__':
    context = xlxs_read('2.xlsx', 0)  # 得到索引为0的sheet页
    # context = xlxs_read(r'K:\PythonProjects\venv\test',0)   #也可以使用绝对路径，r表示字符串里的\不转义
    for i in range(1, context.nrows):  # 返回行数 context.nrows   列数：context.ncols
        rows = context.row_values(i)  # 得到指定行的内容，列表形式返回
        print(rows)
        print(rows[0])  # 得到某一行的第一列数据
        print(context.cell(0, 0).value)  # 得到某一行某一列的值
