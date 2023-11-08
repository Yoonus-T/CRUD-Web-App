from flask import Flask, abort,render_template,request,redirect
from models import db,userModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from app import db  

# Create the database tables
with app.app_context():
    db.create_all()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':


        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        gender = request.form['gender']
        age = request.form['age']
        address = request.form['address']
        users = userModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender, 
            age=age,
            address=address,
        )
        db.session.add(users)
        db.session.commit()
        return redirect('/')
 
 
@app.route('/')
def RetrieveList():
    users = userModel.query.all()
    return render_template('datalist.html',users = users)
 
 
@app.route('/<int:id>')
def Retrieveuser(id):
    users = userModel.query.filter_by(id=id).first()
    if users:
        return render_template('data.html', users = users)
    return f"Employee with id ={id} Doesn't exist"
 
 
@app.route('/<int:id>/edit',methods = ['GET','POST'])
def update(id):
    user = userModel.query.filter_by(id=id).first()

    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        gender = request.form['gender']
        age = request.form['age']
        address = request.form['address']

        user = userModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender, 
            age=age,
            address=address,
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/')
        return f"user with id = {id} Does nit exist"
 
    return render_template('update.html', user = user)
 
 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    users = userModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/')
        abort(404)
     #return redirect('/')
    return render_template('delete.html')
 
app.run(host='0.0.0.0', port=5000)
app.run(host='0.0.0.0', port=5000, debug=True)
