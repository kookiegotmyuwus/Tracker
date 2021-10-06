import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import 'semantic-ui-css/semantic.min.css';
import Projects from './components/project/index.js';
import Login from "./components/login.js";
import Token from "./components/token.js";
import Headers from "./components/header.js";
import axios from 'axios';
import Dashboard from './components/dashboard';

function App() {
  let tokenSave = String(sessionStorage.getItem('token'));
  let adminSave = String(sessionStorage.getItem('admin'));
  let idSave = String(sessionStorage.getItem('username'));
  
  const [error, seterror] = useState("");
  const [token, settoken] = useState(tokenSave === "null" ? "" : tokenSave);
  const [logIn, setlogIn] = useState(token === "" ? false : true);
  const [admin, setadmin] = useState(adminSave === "true" ? true : false);
  const [user, setuser] = useState(idSave === "null" ? 0 : idSave);
  const [userList, setuserList] = useState([]);
  const apiUrl = 'http://localhost:8000/tracker_app/user/';
  useEffect(() => {
    if (true) {
      axios.get(apiUrl, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token,
        }
      })
        .then(res => {
          console.log(res.data)
          setuserList(res.data)
        })
      
    }

  }, [])
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/token" component={() => (<Token settoken={settoken} setuser={setuser} setlogin={setlogIn} setadmin={setadmin} />)} />
          <Route path="/login" component={() => (<Login login={logIn}/>)} />
          {/* <Route path="/tracker_app/project/:project_name" exact component={ProjectDetail} /> */}
          <Route path="/headers" component={Headers}/>
          <Route path="/dashboard" component={Dashboard}/>
          <Route path="/project" component={() => (<Projects id={user} token={token} users={userList} />)} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
