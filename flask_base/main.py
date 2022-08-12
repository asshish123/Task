from flask import Flask, request
from flask_restful import abort
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Art@1999@localhost/flaskbase'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

db.create_all()

@app.route('/per', methods = ['POST'])
def create_person():
    person=request.json

    id=person['p_id']
    pname=person['pname']
    color=person['color']
    people=People(id=id,pname=pname,color=color)
    db.session.add(people)
    db.session.commit()

    return jsonify({"success": True,"response":"person is added"})



@app.route('/getper', methods = ['GET'])
def getperson():
     all_pers = []
     pers = People.query.all()
     for per in pers:
          results = {
                    "id":per.id,
                    "pname":per.pname,
                    "color":per.color,}
          all_pers.append(results)

     return jsonify(
            {
                "success": True,
                "pers": all_pers,
                "total_pers": len(pers),
            }
        )


@app.route("/per/<int:id>", methods = ['GET'])
def getpersonbyid(id):
    per = People.query.get(id)

    results =     {
                    "id":per.id,
                    "pname":per.pname,
                    "color":per.color,}
    return jsonify(
            {
                "success": True,
                "pers": results,
            }
        )


@app.route("/pers/<int:id>", methods = ["PATCH"])
def update_person(id):
    per = People.query.get(id)
    pname = request.json['pname']
    color = request.json['color']

    if per is None:
        abort(404)
    else:
        per.pname = pname
        per.color = color
        db.session.add(per)
        db.session.commit()
        return jsonify({"success": True, "response": "Per Details updated"})  


@app.route("/pers/<int:id>", methods = ["DELETE"])
def delete_person(id): 
    per=People.query.get(id)
    db.session.delete(per)
    db.session.commit()
     
    return jsonify({"success": True, "response": "Per Details delelted"}) 



if __name__ == "__main__":
     app.run(debug=True)