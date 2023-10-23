from pybo import db #__init__.py 파일에서 생성한 SQLAlchemy 클래스의 객체

#db.Column(데이터 타입)
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary_key=True : 중복된 값 X
    subject = db.Column(db.String(200), nullable=False) # nullable=False : 빈칸 X
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)