'''
ORM을 이용하면 데이터베이스 종류에 상관 없이 일관된 코드를 유지할 수 있어서 
프로그램을 유지·보수하기가 편리하다. 
또한 내부에서 안전한 SQL 쿼리를 자동으로 생성해 주므로 
개발자가 달라도 통일된 쿼리를 작성할 수 있고 
오류 발생률도 줄일 수 있다.
'''

import os 

BASE_DIR = os.path.dirname(__file__) 

# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False 