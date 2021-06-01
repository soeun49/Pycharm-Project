from pymongo import MongoClient
import re

def connect():
    client=MongoClient("mongodb://localhost:27017")
    return client

def collection():
    conn=connect()
    db=conn['mydatabase']
    coll=db['pymongo']
    return coll



def phone_book(projection={}):
    while True:
        print("전화번호 관리 프로그램")
        print("1.리스트 | 2.등록 | 3.삭제 | 4.검색 | 5.종료 ")
        menunum=int(input("메뉴번호"))
        if menunum ==1:
            select()
            continue
        if menunum ==2:
            insert_by_input()
            continue
        if menunum ==3:
            delete()
            continue
        if menunum ==4:
            search()
            continue
        if menunum ==5:
            print("프로그램 종료")
            break

    else:
        print("다시 입력해주세요")


def select():
    coll=collection()
    all_data=list(coll.find({},{"_id":False}))
    for data in all_data:
        print(data)

def insert_by_input():
    coll=collection()
    x=input("이름:")
    y=input("휴대전화:")
    z=input("집전화:")
    xs=coll.insert_one(
        {"name":x,"hp":y,"tel":z})
    print("등록되었습니다")

def delete():
    coll=collection()
    y=input("이름:")
    x=coll.delete_many({"name":y})
    print(x.deleted_count, "개의 전화번호가 삭제되었습니다")

def search():
    coll=collection()
    x=input("이름:")
    y=list(coll.find({"name":x, "_id":False}))
    for data in y:
        print(data)
        print(len(data), "개의 전화번호를 찾았습니다")


if __name__ == "__main__":
    phone_book()
    # connect()
    # collection()
    # select()
    # insert_by_input()
    # delete()
    # search()
