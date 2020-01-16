import axios from 'axios'
// npm install js-cookie --save
import Cookies from 'js-cookie';

axios.defaults.baseURL = "http://127.0.0.1:8000/"
var csrf_token = Cookies.get('csrftoken');
export default{
    createUser(data){
        return axios({
            method : 'post',
            url : 'signup',
            data,
            header : {"x-csrfToken" : csrf_token}



        })
    },
    // getUser(){
    //     return 
    // }
}