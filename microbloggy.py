from app import appy, db
from app.models import User, Post

@appy.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    appy.run()