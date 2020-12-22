import csv
import re
import os

def writeCSV(Filename, data):
    with open(Filename, "w+",encoding='cp1251', newline="") as File:
        for i in data: 
            writer=csv.writer(File)
            writer.writerow(i.values())
    File.close()

def AUDreadCSV(Filename):
    with open(Filename, "r", newline="") as file:
        datas=[]
        csv_dict = [row for row in csv.reader(Filename)]
        if len(csv_dict) != 0:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    record={'AudienceName': row[0], 'AudiencePO' :row[1] , 'AudienceTO':row[2], 'AudienceNaimenovanie' : row[3]}
                    datas.append(record)
    return datas



def PPSreadCSV(Filename):
    with open(Filename, "r", newline="") as file:
        datas=[]
        csv_dict = [row for row in csv.reader(Filename)]
        if len(csv_dict) != 0:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    temp = re.findall(r'\d+', row[1])
                    res = list(map(int, temp))
                    record={'FIO': row[0],'Uslovia': res, "Dolzhnost": int(row[2]), "Stepen": int(row[3]), "Zvanie": int(row[4]), 'Napravlenie': row[5], 'Education' : row[6] }
                    datas.append(record)
    return datas


def UPreadCSV(Filename):
    with open(Filename, "r", newline="") as file:
        datas=[]
        csv_dict = [row for row in csv.reader(Filename)]
        if len(csv_dict) != 0:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    record={'NameUD': row[0], 'NumberUD' : row[1], 'Teacher': row[2], "Audience":row[3],"Amount":row[4]}
                    datas.append(record)
    return datas


def TeacherreadCSV(Filename):
    with open(Filename, "r", newline="") as file:
        datas=[]
        csv_dict = [row for row in csv.reader(Filename)]
        if len(csv_dict) != 0:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    datas.append(row[0])
    return datas


def KORead(Filename,Records):
    datas=PPSreadCSV(Filename)
    for i in Records:
        for k in datas:
            if i.get("FIO")==k.get('FIO'):
                i.update(k)
    return Records


def findDiscForTeacher():
        Records=[]
        TeacherDict={}
        Disc=[]
        Teeaachers=TeacherreadCSV("PPSDB.csv")
        Recordsss=UPreadCSV("UPDB.csv")
        for Teach in Teeaachers:
            for i in Recordsss:
                temp = re.findall(r'([А-я]+\ [А-я]+\ [А-я]+)',i.get("Teacher"))
                res = list(map(str, temp))
                for k in res:
                    if Teach==k:
                        Disc.append(i.get("NameUD"))
            TeacherDict={"FIO":Teach,"Disc":Disc}
            Disc=[]
            Records.append(TeacherDict)
        return Records


def MTORead(Filename):
    Records=UPreadCSV("UPDB.csv")
    datas=AUDreadCSV(Filename)
    for i in datas:
        for rec in Records:
            temp = re.findall(r'([А-я]+\-\d\d\d)',rec.get("Audience"))
            res = list(map(str, temp))
            for j in res:
                if i.get("AudienceName")==j:
                    i.update({"Discipline":rec.get("NameUD")})
    return datas



        

