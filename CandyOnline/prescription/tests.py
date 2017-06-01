# _*_ encoding:utf-8 _*_
import MySQLdb, numpy
from Aprior import generate, createC1, scanD, apriori

# myDat = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
# generate(myDat)
# myDat = [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]
def test2():
    myDat = [['256', '241', '56', '14', '38', '151', '52'], ['256', '360', '56', '38', '151', '345', '243', '257', '250'], ['256', '14', '9', '80', '151', '1', '53', '257', '255', '307'], ['256', '56', '345', '151', '38', '12', '14', '171', '257', '250', '247', '243'], ['256', '14', '80', '152', '136', '151', '188', '52', '326', '257', '255', '307'], ['256', '168', '52', '89', '41', '151', '38', '31', '257', '309', '247', '243'], ['256', '38', '168', '171', '55', '56', '151', '83', '14', '171', '49', '191', '85', '257', '309', '247', '243'], ['256', '9', '33', '257', '318', '243'], ['256', '151', '143', '80', '165', '257', '247', '109'], ['262', '46', '14', '24', '50', '187', '32', '31', '9', '14', '41', '77', '250', '112', '243']]

    generate(myDat)


def test():
    fileName = r'F:\wushijia\workspace\530\pm.txt'
    f = open(fileName, 'r')

    # res = []
    # host = "127.0.0.1"
    #
    # user = "root"
    #
    # pwd = "w1020392881"
    #
    # db = "candyonline"
    #
    # db = MySQLdb.connect(host, user, pwd, db, use_unicode=True, charset="utf8")
    # try:
    #     cursor = db.cursor()
    #     sql = "select nums from nums_tmp_copy"
    #     cursor.execute(sql)
    #     res = cursor.fetchall()
    #     cursor.close()
    #     db.commit()
    # except Exception, e:
    #     print e.message
    # finally:
    #     db.rollback()
    #     cursor.close()
    #     db.close()
    #
    myDat = []
    # for r in res:
    #     for n in str(r[0]).split(',|\\n'):
    #         # print n.split(',')
    #         myDat.append(n.split(','))
    #
    for line in f:
        tmp = line.split(',|\n')[0].split('\n')[0]
        myDat.append(tmp.split(','))
    # print myDat
    # ck = createC1(myDat)
    # print ck
    # L, S = scanD(myDat, ck, 0.5)
    # print L
    # print S
    # print 'LK-------------------------SK---------------------------'
    # LK, SK = apriori(myDat, 0.5)
    # print LK
    # print SK
    generate(myDat)
test()
# test2()
