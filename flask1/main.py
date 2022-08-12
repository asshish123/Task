
from operator import imod
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import request,abort
from flask import jsonify

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Art@1999@localhost/flask'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db=SQLAlchemy(app)

class student(db.Model):
    roll_no= db.Column(db.Integer, primary_key=True)
    std_name = db.Column(db.String(80), nullable=False)
    std_class = db.Column(db.Integer,nullable=False)

db.create_all()

@ app.route("/student",methods=['POST'])
def poststudent():
    std=request.json
    roll_no=std['roll_no']
    std_name=std['std_name']
    std_class=std['std_class']
    stud=student(roll_no=roll_no,std_name=std_name,std_class=std_class)
    db.session.add(stud)
    db.session.commit()
    return jsonify(
      {
         "Success":True,
          "Response":"Student data s added"
      }
     )
@ app.route("/student",methods=['GET'])
def getstudent(): 
    all=student.query.all()
    data=[]
    for i in all:
        result= {
                 "roll_no":i.roll_no,
                 "std_name":i.std_name,
                 "std_clas":i.std_class
                }  
        data.append(result)
    return jsonify(
        {
              "Success":True,
              "Response":data,
              "len":len(data)
        }
    )
@ app.route("/student/<int:roll_no>",methods=['PATCH'])
def patchstudent(roll_no):
     std=student.query.get(roll_no)
     data=request.json
     std_name=data['std_name']
     std_class=data['std_class']
     std.std_name=std_name
     std.std_class=std_class

     db.session.add(std)
     db.session.commit()

     return jsonify(
        {
            "sucess":True,
            "message":"added"
        }
     )


@ app.route("/student/<int:roll_no>",methods=['DELETE'])
def delstudent(roll_no):
    std=student.query.get(roll_no)
    db.session.delete(std)
    db.session.commit()

    return jsonify(
        {
            "success":True,
            "message":"std deleted"
        }
    ) 


if __name__ == "__main__":
     app.run(debug=True)                     