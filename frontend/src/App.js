import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import MainLayout from './layout/mainLayout';

import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact>
          <MainLayout>
            <HomePage />
          </MainLayout>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
