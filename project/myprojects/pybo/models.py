# models.py 파일에는 모델 클래스들을 정의하여 사용할 것
# pybo는 질문 답변 게시판이므로 질문과 답변에 해당하는 모델이 있어야함 

from pybo import db 

'''
Question과 같은 모델 클래스는 db.Model 클래스를 상속하여 만들어야함 
이 때 사용한 db 객체는 __init__.py 파일에서 생성한 SQLAlchemy 클래스의 객체
고유 번호(id), 제목(subject), 내용(content), 작성일시(create_date) 속성으로 구성
각 속성은 db.Column으로 생성, 
db.Column에 어떤 값들을 전달했는지 살펴보면서 각 속성의 특징을 확인

db.Column() 괄호 안의 첫 번째 인수는 데이터 타입 의미 -> 속성에 저장할 데이터 종류 결정 
db.Text는 글자 수 제한이 없음 
'''
class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 'question.id'는 question 테이블의 id 컬럼을 의미
    #  ondelete는 삭제 연동 설정 
    #  ondelete='CASCADE' : 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다는 뜻 
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    #  db.relationship으로 question 속성을 생성하면 
    #  답변 모델에서 연결된 질문 모델의 제목을 answer.question.subject처럼 참조할 수 있음
    #  db.relationship(참조할 모델 명, backref = 역참조 설정)
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)