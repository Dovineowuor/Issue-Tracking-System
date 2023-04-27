import React, { useState } from 'react'
import './bugview.css'
import Bugviewsection from './component/bugviewsection'
import bugmodel from "../../Models/bugModels";

import { useDispatch } from 'react-redux'
//import {markComplete} from '../../Controlers/Redux/authSlice'
import { markcomplete } from '../../Controlers/Redux/bugSlice'
import Editpanel from '../edit&delete/editpanel'
import EditBug from '../Bugcreate/bugform'





export default(props) => {
    const dispatch=useDispatch();
    const bug= new bugmodel(props.bug);
    const [displayedit, setdisplayedit] = useState(false);

    function editclicked(){
      setdisplayedit(!displayedit)

    }
     function deleteclicked(){

     }
  return (
    <>
    <div className="bug-view">
      <Editpanel editclicked={editclicked} deleteclicked={deleteclicked}/>
        <button className='close-btn' onClick={props.clicked}>Close</button>
        <h1>{bug.name}</h1>
        <Bugviewsection title="Details" info={bug.details}/>
        <Bugviewsection title="Steps" info={bug.steps}/>
        <Bugviewsection title="Priority" info={bug.priority}/>
        <Bugviewsection title="Creator" info={bug.creator}/>
        <Bugviewsection title="App Version" info={bug.version}/>
        <Bugviewsection title="Time Created" info={bug.time}/>

        <button onClick={()=>{dispatch(markcomplete)}}>MarkComplete</button>





    </div>
    {displayedit &&  <EditBug title="Edit Bug" bug={bug} close={editclicked}/> }

    </>
  )
}
