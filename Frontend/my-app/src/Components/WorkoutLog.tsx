import { useState } from "react"

export function WorkoutLog(){
    const [name, setName] = useState<string>("")
    const [sets, setSets] = useState<string>("")
    const [reps, setReps] = useState<string>("")
    const [date, setDate] = useState<string>("")
    const [weight, setWeights] = useState<string>("")
    async function handleSubmit(){
        //access DB and upload there

        const workoutData = {
            name: name,
            sets: sets,
            reps: reps,
            date: date,
            weight: weight
        }

        
        const response = await fetch("http://localhost:5000/workout", {
              method: "POST",
              headers: {
                "Content-Type": "application/json" 
              },
              body: JSON.stringify(workoutData)
            });
        }
        
            
          
        
    
    return (
        <div>
            <div>
                <input 
                aria-label="Name" 
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                />
                <input  
                aria-label="Sets" 
                placeholder="Sets"
                value={sets}
                onChange={(e) => setSets(e.target.value)}
                />
                <input  
                aria-label="Reps" 
                placeholder="Reps"
                value={reps}
                onChange={(e) => setReps(e.target.value)}
                />
                <input  
                aria-label="Date" 
                placeholder="Date"
                value={date}
                onChange={(e) => setDate(e.target.value)}/>
                <input 
                aria-label="Weight" 
                placeholder=" Weight"
                value={weight}
                onChange={(e) => setWeights(e.target.value)}
                />
                <button onClick={handleSubmit}>
                    Submit
                </button>
            </div>
        </div>
    )
}