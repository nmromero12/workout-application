import { useState } from "react"

export function WorkoutLog(){
    const [name, setName] = useState<string>("")
    const [sets, setSets] = useState<string>("")
    const [reps, setReps] = useState<string>("")
    const [date, setDate] = useState<string>("")
    const [weight, setWeights] = useState<string>("")
    function handleSearch(){
        //access DB and upload there
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
                <button onClick={handleSearch}>
                    Submit
                </button>
            </div>
        </div>
    )
}