from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WorkoutModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Workout(name='{self.name}', sets={self.sets}, reps={self.reps}, weight={self.weight}, date='{self.date}')>"


# Run this ONCE to create the table
with app.app_context():
    db.create_all()

# Request parser for workout data
workout_put_args = reqparse.RequestParser()
workout_put_args.add_argument("name", type=str, help="Name of the Exercise", required=True)
workout_put_args.add_argument("sets", type=int, help="Number of Sets", required=True)
workout_put_args.add_argument("reps", type=int, help="Number of Repetitions", required=True)
workout_put_args.add_argument("date", type=str, help="Date of Workout", required=True)
workout_put_args.add_argument("weight", type=int, help="The Weight for the Exercise", required=True)

# Define the resource fields for marshalling
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'sets': fields.Integer,
    'reps': fields.Integer,
    'date': fields.String,
    'weight': fields.Integer
}

class Workout(Resource):
    @marshal_with(resource_fields)
    def get(self, date):
        result = WorkoutModel.query.filter_by(date=date).all()
        if not result:
            abort(404, message="Could not find workout with that Date.")
        return result

    @marshal_with(resource_fields)
    def post(self):
        args = workout_put_args.parse_args()

        workout = WorkoutModel(
            name=args['name'],
            sets=args['sets'],
            reps=args['reps'],
            date=args['date'],
            weight=args['weight']

        )
        db.session.add(workout)
        db.session.commit()
        return workout, 201

    
    def delete (self, workout_id):
        workout = WorkoutModel.query.get(workout_id)
        if not workout:
            abort(404, message="Could not find workout with the Id.")
        
        db.session.delete(workout)
        db.session.commit()

        return 'successfully deleted', 204

# Add resource to the API
api.add_resource(Workout, "/workout", endpoint="workout_post")
api.add_resource(Workout, "/workout/<string:date>", endpoint="workout_by_date")



if __name__ == "__main__":
    app.run(debug=True)
