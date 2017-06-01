# _*_ encoding:utf-8 _*_
import re, linecache
import MySQLdb
import sys

reload(sys)

sys.setdefaultencoding('utf8')


def prescriptionTreatment(conn, table, fileName):
    """ 修改版本

    :param fileName: 
    :return: 
    """

    sourceFrom = fileName[fileName.find(".txt") + 4:]
    fileName = fileName[:fileName.find(".txt") + 4]

    if sourceFrom == '':
        sourceFrom = u'胡希恕伤寒方证辩证'
    else:
        sourceFrom = unicode(sourceFrom)

    print sourceFrom
    # print isinstance(sourceFrom, unicode)

    f = open(fileName, 'r')
    # 病名
    diseaseNames = []
    # 开方名
    prescriptionNames = []
    # 患者
    patientContents = []
    # 开方
    prescriptions = []
    # 开方原因
    prescriptionsReasons = []

    for line in f:
        content = unicode(line, 'utf-8')
        # print content
        if content.startswith(u'病名：'):
            diseaseName = content[3:]
            diseaseNames.append(diseaseName)
        elif content.startswith(u'开方：'):
            str = content[3:]
            # 开方名
            prescriptionName = str[0:str.find(u"：")]
            # 开方
            prescription = str[str.find(u"：") + 1:]
            prescriptionNames.append(prescriptionName)
            prescriptions.append(prescription)
        elif content.startswith(u'主诉：'):
            str = content[3:]
            patientContents.append(str)
        elif content.startswith(u'开方原因：'):
            prescriptionsReasons.append(content[5:])

    cursor = conn.cursor()

    lis = []
    for x in range(len(diseaseNames)):
        print diseaseNames[x]
        print patientContents[x]
        print prescriptionNames[x]
        print prescriptions[x]
        print prescriptionsReasons[x]

        print sourceFrom

        sql = "insert into "+table+"(diseaseName,patientContent,prescriptionName,prescriptions,prescriptionsReason,sourceFrom) VALUES (" \
                                   "%s,%s,%s,%s,%s,%s)"

        select = "select id from " + table + " where patientContent='" + patientContents[x] + "'"
        if cursor.execute(select) > 0:
            print u"数据已存在"
            cursor.close()
            conn.commit()
            return

        data = (diseaseNames[x], patientContents[x], prescriptionNames[x], prescriptions[x], prescriptionsReasons[x], sourceFrom)
        lis.append(data)
        print cursor.executemany(sql, lis)
        del lis[:]

    conn.commit()
    cursor.close()


def addField(field):
    host = "127.0.0.1"

    user = "root"

    pwd = "w1020392881"

    db = "candyonline"

    table = "mytest_mytest"

    sql = "ALTER TABLE " + table + " ADD " + field + " NVARCHAR (500) NULL"
    db = MySQLdb.connect(host, user, pwd, db, use_unicode=True, charset="utf8")
    try:
        cursor = db.cursor()
        print cursor.execute(sql)
        db.commit()
    except Exception, e:
        print e.message
    finally:
        cursor.close()
        db.close()


def create():
    host = "127.0.0.1"

    user = "root"

    pwd = "w1020392881"

    db = "test"
    conn = MySQLdb.connect(host, user, pwd, db, use_unicode=True, charset="utf8")
    try:
        cursor = conn.cursor()
        sql = "create table emp2(id int(10) PRIMARY ,name varchar(20))"
        print sql
        print cursor.execute(sql)
        conn.commit()
    except Exception, e:
        print e.message
    finally:
        cursor.close()
        conn.close()


def transcoding(field):
    if not isinstance(field, unicode):
        return unicode(field, "gbk", "ignore")
    else:
        return field


def insert(conn, table, field, value):
    """
    
    :param conn: 数据库连接
    :param table: 操作的数据表
    :param field: 插入的字段
    :param value: 插入的字段值
    :return: 返回影响的行数
    """
    value = value.split(',')
    str = '\',\''
    sql = "insert into "+table+"("+field+") VALUES ('"+str.join(value)+"')"
    cursor = conn.cursor()
    res = cursor.execute(sql)
    conn.commit()
    cursor.close()
    return res


def select(conn, table, field, value, field2):

    """
    
    :param conn: 数据库连接
    :param table: 操作的数据表
    :param field: 作为查询条件的字段
    :param value: 作为查询条件的字段值
    :param field2: 要查询的字段
    :return: 返回查询字段的值
    """
    res = ""

    field = transcoding(field)
    value = transcoding(value)
    field2 = transcoding(field2)
    # conn = MySQLdb.connect(host, user, pwd, db, use_unicode=True, charset="utf8")
    sql = "select "+field2+" from "+table+" where "+field+"='"+value+"'"
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    conn.commit()
    cursor.close()

    return res


def delete(conn, table, id):

    """
    
    :param conn: 数据库连接
    :param table: 要操作的数据表
    :param id: 根据id删除行数据
    :return: 返回影响的行数
    """
    res = 0
    sql = "delete from "+table+" where id = "+id
    cursor = conn.cursor()
    res = cursor.execute(sql)
    conn.commit()
    cursor.close()
    return res


def recoginze(conn, input):
    f = ''

    sql = "select singleMedicine from single"
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.execute("select * from prescription")
    f = cursor.fetchall()
    cursor.close()

    singles = input.split(u'，')

    for k in range(len(singles)):
        for j in rs:
            if singles[k].find(j[0]) is not -1:
                singles[k] = j[0]

    index = []
    res = []

    for line in f:
        # print line[1] 药名
        # print line[2] 药方
        prescription2 = re.split(u'，|/|\\n', line[2])
        tmp = list(set(prescription2).intersection(set(singles)))
        index.append(len(tmp))

    for x in range(len(index)):
        # 如果集合中某个数是该集合最大的数，记下该数在数列中的位置
        if index[x] == max(index):
            res.append(x)

    print u"\n药名："
    for x in res:
        print f[x][1]


def command_toast(text):
    return text.encode('gbk', 'ignore')
    # return unicode(text)


def command():
    host = transcoding(raw_input(command_toast("请先初始化数据库\n请输入主机名：")))
    user = transcoding(raw_input(command_toast("请输入用户名：")))
    pwd = transcoding(raw_input(command_toast("请输入密码：")))
    db = transcoding(raw_input(command_toast("请输入数据库名：")))
    conn = MySQLdb.connect(host, user, pwd, db, use_unicode=True, charset="utf8")
    loop(conn)
    conn.close()
    print "\nfinish"


def loop(conn):
    try:
        toast = command_toast("请输入要执行的函数：1.读取文件 2.添加数据 3.查询字段 4.删除 5.查询药名 0.退出\n")
        res = transcoding(raw_input(toast))
        if res == u'1':
            table = raw_input(command_toast("请输入表名："))
            res1 = raw_input(command_toast("请输入要读取的文件路径+来源，默认来源为：胡希恕伤寒方证辩证 "))
            res1 = unicode(res1, "gbk", "ignore")
            if res1.find(".txt") is not -1:
                prescriptionTreatment(conn, table, res1)
                loop(conn)
            else:
                print command_toast("输入的参数不正确")
        elif res == u'0':
            return
        elif res == u'2':
            try:
                table = transcoding(raw_input(command_toast("请输入表名：")))
                field = transcoding(raw_input(command_toast("请输入要插入字段名，并用逗号隔开：")))
                value = raw_input(command_toast("请输入要插入的字段值，并用逗号隔开："))
                insert(conn, table, field, value)
                loop(conn)
            except Exception:
                print command_toast("输入的参数不正确")
        elif res == u'3':
            try:
                table = transcoding(raw_input(command_toast("请输入表名：")))
                field = transcoding(raw_input(command_toast("请输入条件字段：")))
                value = transcoding(raw_input(command_toast("请输入条件字段值：")))
                field2 = transcoding(raw_input(command_toast("请输入要查询的字段：")))
                print select(conn, table, field, value, field2)
                loop(conn)
            except Exception:
                print command_toast("输入的参数不正确")
        elif res == u'4':
            try:
                table = transcoding(raw_input(command_toast("请输入表名：")))
                id = transcoding(raw_input(command_toast("请输入要删除的id：")))
                print delete(conn, table, id)
                loop(conn)
            except Exception as e:
                print command_toast("输入的参数不正确")
        elif res == u'5':
            try:
                prescriptions = transcoding(raw_input(command_toast("请输入药方组合，药方之间用中文逗号隔开：")))
                recoginze(conn, prescriptions)
            except Exception as e:
                print command_toast("输入的参数不正确")
        else:
            print command_toast("输入的参数不正确")
    finally:
        return

command()
