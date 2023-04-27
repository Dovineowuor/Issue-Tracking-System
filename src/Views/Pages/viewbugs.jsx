import React, { useEffect, useState } from 'react'
import { useDispatch,useSelector } from 'react-redux';
import {getBugs} from '../../Controlers/Redux/bugSlice'
import '../BugCard/bugcard'
//import bugcard from '../BugCard/bugcard';
import Bugcard from '../BugCard/bugcard';
import Bugview from '../BugView/bugview';
import bug from '../../Models/bugmodel';


export default() => {
  const[DISPLAY_BUG,SET_DISPLAY_BUG]=useState({
    name:"",isDisplayed:false
  })
    const dispatch=useDispatch();
    const {bugs}=useSelector(state=>state);

    useEffect(()=>{
        dispatch(getBugs());
    },[bugs.length<1])

    function bugclicked(name){
      SET_DISPLAY_BUG({
        isDisplayed:!DISPLAY_BUG.isDisplayed,
        name:name
      })

    }
  return (
    <div className="page-container">
{bugs.map((bug,key)=>(
    <Bugcard key={key} bug={bug} clicked={bugclicked}/>
) )}
{DISPLAY_BUG.isDisplayed &&<Bugview clicked={bugclicked} bug={bugs.filter((bug)=> bug.name==DISPLAY_BUG.name)[0]}/>}

    </div>
  )
}
