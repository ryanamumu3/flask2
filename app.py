from flask import Flask, render_template, request, redirect, url_for, abort
from models import db, EmployeeModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('datalist'))

@app.route('/data')
def datalist():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html', employees=employees)

@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        
        # Criação do novo funcionário
        new_employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('datalist'))
    
    return render_template('create.html')

@app.route('/data/<int:id>')
def data(id):
    employee = EmployeeModel.query.get_or_404(id)
    return render_template('data.html', employee=employee)

@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    employee = EmployeeModel.query.get_or_404(id)
    
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.age = request.form['age']
        employee.position = request.form['position']
        db.session.commit()
        return redirect(url_for('data', id=employee.id))
    
    return render_template('update.html', employee=employee)

@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    employee = EmployeeModel.query.get_or_404(id)
    
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('datalist'))
    
    return render_template('delete.html', employee=employee)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criação da tabela no banco de dados
    app.run(host='localhost', port=5000, debug=True)
