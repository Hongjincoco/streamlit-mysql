import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def main():
    # title = st.text_input('책 제목 입력')
    # author_fname= st.text_input('이름 입력')
    # author_lname= st.text_input('성 입력')
    # released_year = st.number_input('년도 입력')
    # stock_quantity = st.number_input('수량 입력')
    # pages= st.number_input('페이지 수 입력')

    if st.button('저장') :
    try :
        # 1. 커넥터로 부터 커넥션을 받는다.
        connection = mysql.connector.connect(
            host ='database-1.c870clu6imti.us-east-2.rds.amazonaws.com',
            database = 'yhdb',
            user = 'streamlit',
            password = 'yh1234'
        )

        if connection.is_connected() :
            db_info = connection.get_server_info()
            print("MySQL server version : ", db_info)

            # 2. 커서를 가져 온다.
            curser = connection.curser()

            # 3. 원하는 것 실행가능
            # curser.execute('select database();')
            query = """insert into people
			        values(%s, %s, %s, %s) ;"""
            record = ('Mike', datetime.now(),datetime.now(),datetime.now())
            print(datetime.now())
            
            # query = """insert into book ( title, author_fname, author_lname,
			# 			released_year, stock_quantity, pages)
			#         values('%s', '%s', '%s', %s, %s, %s) ;"""

            # record = (title, author_fname,author_lname,released_year,stock_quantity,pages)

            curser.execute(quary, record)
            connection.commit()
            print("{}개 적용됨.".format(curser.rowcount))

            # 4. 실행 후 커서에서 결과를 뺀낸다.
            # record = curser.fetchone()
            # print('Connected to db : ', record)
    except Error as e :
        print('디비 관련 에러 발생', e)

    finally :

        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 전부 닫아 준다.
        curser.close()
        connection.close()
        print('MySQL 커넥션 종료')

if __name__ == '__main__' :
    main()