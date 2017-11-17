import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ruhvejri392wef'
    
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'user.sqlite')
    
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/assets/img/'
    
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass
