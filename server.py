from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)


@app.route('/users/new')
def results():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def add():
    print(request.form)
    User.save(request.form)
    return redirect('/')

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {'id': id}
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/users/<int:id>')
def show(id):
    data = {'id': id}
    return render_template('show_user.html', user=User.get_one(data))

@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)