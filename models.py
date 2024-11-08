from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "employees"  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"<Employee {self.name}, ID {self.employee_id}>"
