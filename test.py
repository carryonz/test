# Python3 各种文件格式的转换：
import json
import pymysql
from datetime import datetime
from xlrd import xldate_as_tuple
import xlrd
import xlwt


# 读CSV
def readCSV():
    ls = []
    with open('../ls/textfile/price2016.csv', 'r', encoding='utf-8') as in_csv:
        for line in in_csv:
            line = line.replace('\n', '')
            ls.append(line.split(','))
    return ls


# 写csv
def writeCSV(ls):
    out_csv = open('../ls/textfile/out_csv', 'w', encoding='utf-8')
    for i in range(len(ls)):
        out_csv.write(','.join(ls[i]) + '\n')
    print("写入成功！")


# 读json

def readJson():
    in_json = open("test.json", 'r',encoding='utf-8-sig')
    ls = json.load(in_json)
    # print(ls)
    # data = list(ls[0].keys())
    data=[]
    for item in ls:
        data.append(list(item.values()))
    in_json.close()
    for item in data:
    	print(item[1][0])
        # print(''.join(item) + '\n')
    print('读入json完成')


# 写json

def writeJson(ls):
    out_json = open('new.json', 'w')
    for i in range(1, len(ls)):
        ls[i] = dict(zip(ls[0], ls[i]))
    json.dump(ls[1:], out_json, sort_keys=True, indent=4, ensure_ascii=False)
    out_json.close()


# 读TEXT
def readText():
    in_text = open('../ls/textfile/test_text.txt', 'r')
    for line in in_text.readlines():
        print(line)
    print('input OK!')


# 写TEXT
def writeText(ls):
    out_text = open('../ls/textfile/out_text.txt', 'w')
    for i in range(len(ls)):
        out_text.write(' '.join(ls[i]) + '\n')


# 读sql文件
def readsql():
    cursor, db = login()
    sql = "select * from course"
    doit(sql, cursor, db)
    data = cursor.fetchall()
    for d in data:
        print('编号:', d[0], end='\t')
        print('名称:', d[1], end='\t')
        print('地点:', d[2], end='\t')
        print('时长:', d[3], end='\t')
        print('考试时间:', d[4], end='\t')
        print("\n")
    db.close()


# 写sql文件
def writesql(file):
    cursor, db = login()
    fw = open('../ls/textfile/' + file, 'r', encoding="utf-8")
    for line in fw:
        line = line.replace(' ', ',')
        ans = line.split(',')
        print(ans[0], ans[1], ans[2], ans[3], ans[4])
        sql = "insert into course(`number`,`name`,place,duration,examTime) values ('{}','{}','{}','{}','{}')".format(ans[0],
                                                                                                                 ans[1],
                                                                                                                 ans[2],
                                                                                                                 ans[3],
                                                                                                                 ans[4])
        doit(sql, cursor, db)



# 读excel文件
def readexcel():
    cur, db = login()
    data = xlrd.open_workbook("../ls/textfile/test.xlsx", "r")
    sheet = data.sheet_by_index(0)
    for i in range(1, int(sheet.nrows)):
        ans = sheet.row_values(i)
        print(ans[0], ans[1], ans[2], ans[3], ans[4])
        sql = "insert into course(`number`,`name`,place,duration,examTime) values ('{}','{}','{}','{}','{}')".format(ans[0],
                                                                                                                 ans[1],
                                                                                                                 ans[2],
                                                                                                                 ans[3],
                                                                                                                 ans[4])
        doit(sql, cur, db)


def writeexcel(ls):
    cur, db = login()
    sql = 'select * from course'
    cur.execute(sql)
    fileds = [filed[0] for filed in cur.description] #列表生成式，所有字段
    all_data = cur.fetchall() #所有数据
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
    col = 0
    for filed in fileds:
        sheet.write(0, col, filed)
        col += 1

    row = 1

    for data in all_data:
        for col, field in enumerate(data):  # 控制列数
            sheet.write(row, col, field)
        row += 1  # 每次写完一行，行数加1
    book.save('../ls/textfile/%s.xls' %ls)
    # pass

def login():
    db = pymysql.Connect(host="localhost", user="root", password="XXXXX", db="pythontest")
    cur = db.cursor()
    cur.execute("use students")
    return cur, db


def doit(sql, cur, db):
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

if __name__ == '__main__':
    # ls = readCSV()
    # writeCSV(ls)
    readJson()
    # writeJson(ls)
    # readText()
    # writeText(ls)
    # readsql()
    # file = "sql.txt"
    # writesql(file)
    # readexcel()
    # ls = "course"
    # writeexcel(ls)