import React from 'react';
import logo from './logo.svg';
import './App.css';
import { WorkoutLog } from './Components/WorkoutLog';
import { WorkoutSearch } from './Components/WorkoutSearch';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Fitness
        </p>
      </header>
      <WorkoutLog />
      <WorkoutSearch/>
    </div>
  );
}

export default App;
