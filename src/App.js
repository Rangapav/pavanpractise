// import logo from './logo.svg';
import React from 'react';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom';
import Animal from './Animal';
import Career from './Career';
import Celebrity from './Celebrity';
import Dev from './Dev';
import Explicit from './Explicit';
import Fashion from './Fashion';
import Food from './Food';
import History from './History';
import Money from './Money';
import Movies from './Movie';
import Music from './Music';
import Political from './Political';
import Religion from './Religion';
import Science from './Science';
import Sport from './Sport';
import Travel from './Travel';
import './App.css';

function App() {
  // const newLocal = ;
  return (
    <div className="App">
      <> 
      <h1 className='R'>Chuck Norries</h1>
      <header>
      <Router className="App-router">
      <Link to="/Animal">Animal</Link>
      <Link to="/Career">Career</Link>
      <Link to="/Celebrity">Celebrity</Link>
      <Link to="/Dev">Dev</Link>
      <Link to="/Explicit">Explicit</Link>
      <Link to="/Fashion">Fashion</Link>
      <Link to="/Food">Food</Link>
      <Link to="/History">History</Link>
      <Link to="/Money">Money</Link>
      <Link to="/Music">Music</Link>
      <Link to="/Religion">Religion</Link>
      <Link to="/Science">Science</Link>
      <Link to="/Sport">Sport</Link>
      <Link to="/Travel">Travel</Link>
      
      <Routes>
  <Route exact path="/Animal" element={<Animal />} />
  <Route exact path="/Career" element={<Career />} />
  <Route exact path="/Celebrity" element={<Celebrity />} />
  <Route exact path="/Dev" element={<Dev />} />
  <Route exact path="/Explicit" element={<Explicit />} />
  <Route exact path="/Fashion" element={<Fashion />} />
  <Route exact path="/Movie" element={<Movies />} />
  <Route exact path="/Money" element={<Money />} />
  <Route exact path="/Music" element={<Music />} />
  <Route exact path="/Food" element={<Food />} />
  <Route exact path="/History" element={<History />} />
  <Route exact path="/Political" element={<Political />} />
  <Route exact path="/Religion" element={<Religion />} />
  <Route exact path="/Science" element={<Science />} />
  <Route exact path="/Sport" element={<Sport />} />
  <Route exact path="/Travel" element={<Travel />} />
</Routes>
</Router>
</header>

  
      </>
    </div>

  );
}

export default App;

