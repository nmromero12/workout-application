import { useState, useEffect } from "react";


export type Workout = {
    id: number
    name: string
    sets: number
    reps: number
    date: string
    weight: number

}


export function WorkoutSearch() {
    const [date, setDate] = useState<string>("");
    const [workout, setWorkout] = useState<Workout | null>(null);
    const fetchData = () => {
        fetch(`http://localhost:5000/workout/${date}`).then((response) => response.json()).then((data) => {
            setWorkout(data)
        })
        
    };


    return (



        <div>
            
            
            <input
            placeholder="Enter date" 
            onChange={(event) => {
                setDate(event.target.value)
            }}/>
            <button onClick={fetchData}>Search</button>
            {workout &&(
            <div>
                <h1>Exercise: {workout.name}</h1>
                <h1>Sets: {workout.sets}</h1>
                <h1>Reps: {workout.reps}</h1>
                <h1>Weight: {workout.weight}</h1>
            </div>
            )}


        </div>
    )
}
