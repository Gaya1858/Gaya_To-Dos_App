//We use  axios for sending get,post,put and delete requests.
import axios from 'axios';

class TodoDataService{

    // getall returns all the todos for a given user. we attach the token as our authorization header
    // for our axios request.
    getAll(token){
        axios.defaults.headers.common["Authorization"] = "Token"+token;
        return axios.get('http://http://gaya1858.pythonanywhere.com/api/todos/');
    }

    createTodo(data, token){
        axios.defaults.headers.common["Authorization"] = "Token"+token;
        return axios.post('http://http://gaya1858.pythonanywhere.com/api/todos/', data);
    }
    updateTodo(id, data, token){
        axios.defaults.headers.common["Authorization"] = "Token"+token;
        return axios.put(`http://http://gaya1858.pythonanywhere.com/api/todos/${id}`,data);
    }
    deleteTodo(id, token){
        axios.defaults.headers.common["Authorization"] = "Token"+token;
        return axios.delete(`http://http://gaya1858.pythonanywhere.com/api/todos/${id}`);
    }
    completeTodo(id, token){
        axios.defaults.headers.common["Authorization"] = "Token"+token;
        return axios.put(`http://http://gaya1858.pythonanywhere.com0/api/todos/${id}/complete`);
    }
    login(data){
        return axios.post("http://http://gaya1858.pythonanywhere.com/api/login/", data);
    }
    signup(data){
        return axios.post("http://http://gaya1858.pythonanywhere.com0/api/signup/", data);
    }

}
export default new TodoDataService();