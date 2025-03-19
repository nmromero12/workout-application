import React from 'react';
import logo from './logo.svg';
import './App.css';
import { WorkoutLog } from './Components/WorkoutLog';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Fitness
        </p>
      </header>
      <WorkoutLog />
    </div>
  );
}

export default App;
