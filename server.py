from flask import Flask, request, render_template
from controllers import email
from controllers import user as user_ldap
from models.User import User


app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
@app.route('/hello/<email>', methods=['GET', 'POST'])
def hello(email=None):
    if request.method == 'POST':
        user = User(request.form['first_name'], request.form['first_name'], request.form['department_number'],
                    request.form['phone_number'], request.form['email'], request.form['password'])
        user_ldap.create_user(user)

    return render_template('form.html', email=email)


@app.route("/send/<receiver>")
def sendEmail(receiver):
    email.send_mail(receiver)
    return 'Done'


@app.route("/response")
def response():
    print(request.args)
    return 'Done'


if __name__ == '__main__':
    app.run()
