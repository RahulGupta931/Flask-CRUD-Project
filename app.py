from flask import render_template, redirect, url_for, request, Flask, g, current_app, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from alembic import op

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, unique=False)
    last_name = db.Column(db.String(100), nullable=False, unique=False)
    phone_no = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    # __table_args__ = (
    #     db.UniqueConstraint('first_name', name='unique_first_name'),
    # )

    # def __repr__(self):
    #     return '<User %r>' % self.first_name

    # def upgrade():
    #     op.drop_constraint('unique_first_name', 'user', type_='unique')
    #     op.create_unique_constraint('uq_first_name', 'user', ['first_name'])

    # def downgrade():
    #     op.drop_constraint('uq_first_name', 'user', type_='unique')
    #     op.create_unique_constraint('unique_first_name', 'user', ['first_name'])


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        phone_no = request.form.get('phoneNumber')
        address = request.form.get('address')

        new_user = User(first_name=first_name, last_name=last_name,
                        phone_no=phone_no, address=address)
        db.session.add(new_user)
        db.session.commit()
        return render_template('home.html')

    return render_template('home.html')


@app.route('/index', methods=['GET'])
def index():
    data = User.query.all()
    return render_template('index.html', data=data)


@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    if request.method == 'POST':
        user = User.query.get_or_404(id)

        user.first_name = request.form.get('firstName')
        user.last_name = request.form.get('lastName')
        user.phone_no = request.form.get('phoneNumber')
        user.address = request.form.get('address')
        print(user.first_name)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
