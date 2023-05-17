import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Services from './components/pages/Services';
import Products from './components/pages/Products';
import SignUp from './components/pages/SignUp';
import Chatbot from './components/pages/Chatbot';
import PlantDisease from './components/pages/PlantDisease';
import Weather from './components/pages/Weather';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/services' component={Services} />
          <Route path='/products' component={Products} />
          <Route path='/sign-up' component={SignUp} />
          <Route path='/chatbot' component={Chatbot} />
          <Route path='/plantdisease' component={PlantDisease} />
          <Route path='/weather' component={Weather} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
