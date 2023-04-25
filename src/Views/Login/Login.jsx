import React, { useState } from "react";
import { useDispatch } from 'react-redux';
import './Login.css';
import {signIn} from '../../Controlers/Redux/authSlice'

export default ()=>{

    const dispatch=useDispatch();
    const [formInput,setformInput]=useState({
        name:"",
        password:""
    })

    function inputChnaged(e){
        setformInput({
            ...formInput,
            [e.target.name]:e.target.value
        })
    }

    function submit(e){
        dispatch(signIn(formInput));
        e.preventDefault();
    }
    return(
        <div className="loginbg">
            <form action="" className="login-panel">
                <h1>
                    LogIn:
                </h1>

                <input name="name " placeholder="name" onChange={inputChnaged} value={formInput.name}></input>
                <input name="password "  type="password"   placeholder="password" onChange={inputChnaged} value={formInput.password}></input>
                <button type="submit" onClick={submit}>LogIn</button>

            </form>

        </div>
    )
}