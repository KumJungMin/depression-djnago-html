import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';
import api from './api';
import DjangoCSRFToken from 'django-react-csrftoken'
// import csrftoken from './csrftoken'
// npm install --save django-react-csrftoken
const App=()=>{
  const handleChangeId =(e)=>{
    setId(e.target.value)
  }
  const handleChangePw1 =(e)=>{
    setPw1(e.target.value)

  }

  const handleChangePw2 =(e)=>{
    setPw2(e.target.value)

  }

  const [id, setId] = useState('')
  const [pw1, setPw1] = useState('')
  const [pw2, setPw2] = useState('')

  const handleSubmit =(e)=> {
    api.createUser({username : id, password1 : pw1, password2 : pw2})

    console.log(id, pw1)
  }

  return(
    <div className="App">
      <form>
      <DjangoCSRFToken/>
        <input
        name = 'id'
        value = {id}
        onChange={handleChangeId} />
        <input
        name = 'pw1'
        value = {pw1}
        onChange={handleChangePw1} />
         <input
        name = 'pw2'
        value = {pw2}
        onChange={handleChangePw2} />
        <button  onClick={handleSubmit} >aa</button>

      </form>
      
    </div>
  )
}



export default App;
