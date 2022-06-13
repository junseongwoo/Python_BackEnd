from flask import Blueprint 

'''
새로운 URL 매핑이 필요할 때마다 라우팅 함수를 create_app 함수 안에 계속 추가해야 한다. 
이렇게 라우팅 함수가 계속 추가된다면 create_app 함수는 엄청나게 크고 복잡한 함수가 될 것
-> 블루프린트로 해결 -> 라우팅 함수를 체계적으로 관리 
-> URL과 함수의 매핑을 관리하기 위해 사용하는 클래스
'''

'''
애너테이션이 @app.route에서 @bp.route로 변경되었다. 
이 변화에 주목하자. @bp.route에서 bp 객체는 다음처럼 생성되었다.
bp = Blueprint('main', __name__, url_prefix = '/')
1. bp 객체 생성시 사용된 __name__은 모듈명인 "main_views"가 인수로 전달
2. 첫번째 인수로 전달한 "main"은 블루프린트의 "별칭"
3. url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미
ex) main_views.py 파일의 URL 프리픽스에 url_prefix='/' 대신 url_prefix='/main'이라고 입력했다면
    hello_pybo 함수를 호출하는 URL은 localhost:5000/이 아니라 localhost:5000/main/
'''
bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'