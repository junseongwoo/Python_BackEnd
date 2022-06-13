from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
import config

db = SQLAlchemy()
migrate = Migrate()

# app = Flask(__name__)은 플라스크 애플리케이션을 생성하는 코드
# __name__ 에는 모듈명이 담김 

# create_app 함수 = 애플리케이션 팩토리 
def create_app():
    app = Flask(__name__)

    # config.py 파일에 작성한 항목을 읽기 위해 
    app.config.from_object(config)

    # ORM 
    db.init_app(app)
    migrate.init_app(app, db) 
    from . import models 


    # URL 매핑 
    # route : 애너테이션으로 URL을 매핑하는 함수 = 라우팅 함수 
    # @app.route('/')

    '''
    블루프린트 
    main_views.py 파일에 생성한 블루프린트 객체 bp를 app.register_blueprint(main_views.bp)로 등록
    '''
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app