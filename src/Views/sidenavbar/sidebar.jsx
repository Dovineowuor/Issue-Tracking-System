import React from "react";
import {Link} from "react-router-dom"
import { useDispatch,useSelector } from 'react-redux';
import {signOut} from '../../Controlers/Redux/authSlice'
import './sidebar.css';



export default()=>{
    const dispatch=useDispatch();

    const{auth}=useSelector(state=>state)

    function SignOut(){
        dispatch(signOut);
    }
    return(
        <div className="sidebar">

            <Link className="navlink" to="/" > <h1 className="brand">Issue-Tracker</h1></Link>

            <ul>
                <li><Link to="/" className="navlink">Dashboard</Link></li>
                <li><Link to="/viewbugs" className="navlink">ViewBugs</Link></li>
             {auth.admin &&  <li><Link to="/create" className="navlink">Create Bug</Link></li>} 

            </ul>
            <button className="navlink logout" onClick={signOut}> Log Out</button>

        </div>
    )
}