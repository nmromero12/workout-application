from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
db = SQLAlchemy(app)

class WorkoutModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Workout(name={self.name}, sets={self.sets}, reps={self.reps}, weight={self.weight})"





# with app.app_context():
#     db.create_all() #ONLY DO THIS ONCE THEN DELETE IT



    



workout_put_args = reqparse.RequestParser()
workout_put_args.add_argument("name", type=str, help="Name of the Exercise", required=True)
workout_put_args.add_argument("sets", type=int, help="Number of Sets",required=True)
workout_put_args.add_argument("reps", type=int, help="Number of repetitions",required=True)
workout_put_args.add_argument("date", type=str, help="Date of workout",required=True)
workout_put_args.add_argument("weight", type=int, help="The weight for the exercse used", required=True)
workouts = {}

class Workout(Resource):
    def get(self, workout_id):
        if workout_id not in workouts:
            abort(404, message="Exercise id is not valid")
        
        return workouts[workout_id]
    
    def put(self, workout_id):
        args = workout_put_args.parse_args()
        workouts[workout_id] = args
        return workouts[workout_id]
    

api.add_resource(Workout, "/workout/<int:workout_id>")

if __name__=="__main__":
    app.run(debug=True)