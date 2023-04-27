import React from 'react'
import './bugcard.css'
import pioritycontroller from '../../Controlers/pioritycontroller'


export default (props) => {
    const{name,priority,version}=props.bug;
    const {level,color}=pioritycontroller(priority)
    function clicked(){
        props.clicked(name);
    }
  return (
    <div className="bug-card" onClick={clicked} style={{color:color}}> 
        <h1 className='name'>{name}</h1>
        <h2 className='priority'>{level}</h2>
        <h3 className='version'>{version}</h3>

    </div>
  )
}
