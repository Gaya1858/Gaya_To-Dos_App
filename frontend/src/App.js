import './App.css';
import React from "react";
import {Switch, Route, Link} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

import AddTodo from "./components/add-todo";
import TodosList from "./components/todos-list";
import Login from "./components/login";
import Signup from "./components/signup";

import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Navbar";
import TodoDataService from "./services/todos";


function App() {
    // null tobe the initial value of the user
    // useState returns an array of two values: the current state value and a function that lets you update
    // we assign the current state user to user, and the function to update it to setUser
    const [user, setUser] = React.useState(null);
    const [token, setToken] = React.useState(null);
    const [error, setError] = React.useState('');

    // with login, we set the user state, the login function will be called from the Login component
    // which we will implement and revisit later.
    async function login(user=null){
        TodoDataService.login(user).then(response =>{
            setToken(response.data.token);
            setUser(user.username);
            localStorage.setItem('token',response.data.token);
            localStorage.setItem('user',user.username);
            setError('');

        })
            .catch(e =>{
                console.log('login', e);
                setError(e.toString());
            });
    }
    // logout simply puts user to null.
    async function logout(){
        setToken('');
        setUser('');
        localStorage.setItem('token','');
        localStorage.setItem('user','');
    }
    // signup for now works in a similar fashion.
    async function signup(user=null){
        TodoDataService.signup(user).then(response =>{
            setToken(response.data.token);
            setUser(user.username);
            localStorage.setItem('token',response.data.token);
            localStorage.setItem('user',user.username);
        })
            .catch(e =>{
            console.log(e);
            setError(e.toString());
        })
    }

  return (
    <div className="App">
        <Navbar style={{background: 'aqua', color: 'black', paddingTop:20,paddingBottom:20}}>
            <div className="container-fluid">
                <Navbar.Brand>TodosApp</Navbar.Brand>

                <Nav className="me-auto">
                    <Container>
                        <Link className="nav-link" to="/todos">Todos</Link>
                        {user? (
                            <Link className="nav-link" onClick={logout}>Logout({user})</Link>
                        ): (
                                <>
                                <Link className="nav-link" to="/login">Login</Link>
                                <Link className="nav-link" to="/signup">Sign Up</Link>
                                </>
                            )}
                    </Container>
                </Nav>
            </div>
        </Navbar>
        <div className="container mt-4">
                    <Switch>
                        <Route exact path={["/","/todos"]} render={(props) =>
                            <TodosList{...props} token={token}/>}>
                        </Route>
                        <Route path="/todos/create" render={(props) =>
                            <AddTodo{...props} token={token}/>}>
                        </Route>
                        <Route path="/todos/:id/" render={(props) =>
                            <AddTodo{...props} token={token}/>}>
                        </Route>
                        <Route path="/login" render={(props) =>
                            <Login{...props} login={login}/>}>
                        </Route>
                        <Route path="/signup" render={(props) =>
                            <Signup{...props} signup={signup}/>}>
                        </Route>
                    </Switch>
        </div>
        <footer className="text-center text-lg-start  mt-4" style={{background:'darkgrey', color:'beige'}}>
            <div className="text-center p-4">
                 &copy; Copyright - <a target="_blank"
                               className="text-reset fw-bold text-decoration-none"
                               href="https://twitter.com/Gaya86229157">Gaya Kanagaraj</a>
            </div>
        </footer>
    </div>
  );
}

export default App;
