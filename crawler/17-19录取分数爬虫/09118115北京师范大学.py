from urllib.request import urlretrieve
import xlrd
import csv
uni_list=['http://admissionold.bnu.edu.cn/old/2019jz/fsx/bj.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/tj.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/sh.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/cq.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/hlj.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/jilin.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/ln.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/neimeng.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/hebei.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/sd.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/hubei.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/ah.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/henan.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/shan1xi.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/hunan.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/js.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/jx.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/zj.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/fj.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/gd.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/hainan.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/yunnan.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/gz.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/gx.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/xj.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/qh.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/nx.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/gs.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/shan3x.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/xz.xls',
          'http://admissionold.bnu.edu.cn/old/2019jz/fsx/sichuan.xls']
pro_list = ['??????','??????','??????','??????','?????????','??????','??????','?????????','??????','??????','??????','??????','??????','??????','??????','??????',
            '??????','??????','??????','??????','??????','??????','??????','??????','??????','??????','??????','??????','??????','??????','??????']
file_list = ['bj1.xls','tj1.xls','sh1.xls','cq1.xls','hlj1.xls','jilin1.xls','ln1.xls','neimeng1.xls','hebei1.xls',
             'sd1.xls','hubei1.xls','ah1.xls','henan.xls','shan1xi1.xls','hunan1.xls','js1.xls','jx1.xls',
             'zj1.xls','fj1.xls','gd1.xls','hainan1.xls','yunnan1.xls','gz1.xls','gx1.xls','xj1.xls','qh1.xls',
             'nx1.xls','gs1.xls','shan3x1.xls','xz1.xls','sichuan1.xls']
list_values=[]
for i,j,k in zip(uni_list,pro_list,file_list):
    urlretrieve(i, k)
    data = xlrd.open_workbook(k)
    table = data.sheets()[0]
    s = t = 0
    nrows = table.nrows  # ????????????
    for i in range(1, nrows):  # ???0????????????
        s += 1
        alldata = table.row_values(i)  # ????????????excel?????????????????????????????????
        result = alldata[0]  # ???????????????????????????
        if result == '??????':
            t = s  # ?????????????????????????????????
    for x in range(3, t):
        values = ['??????????????????', '2018', j]
        row = table.row_values(x)
        num2018 = [2, 1, 11]
        for i in num2018:
            if row[i] == '':
                values.append('?????????')
            else:
                values.append(row[i])
        values.append('09118115?????????')
        list_values.append(values)
    for x in range(3, t):
        values = ['??????????????????', '2017', j]
        row = table.row_values(x)
        num2017 = [2, 1, 8]
        for i in num2017:
            if row[i] == '':
                values.append('?????????')
            else:
                values.append(row[i])
        values.append('09118115?????????')
        list_values.append(values)
    for x in range(3, t):
        values = ['??????????????????', '2016', j]
        row = table.row_values(x)
        num2018 = [2, 1, 5]
        for i in num2018:
            if row[i] == '':
                values.append('?????????')
            else:
                values.append(row[i])
        values.append('09118115?????????')
        list_values.append(values)






with open("09118115?????????-??????????????????.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["College" , "Year", "Province","Category","Major","Score","Contributor"])
    for i in list_values:
        writer.writerow(i)
