import React from 'react'
import'./card.css'
import Piority  from '../../Controlers/pioritycontroller'

export default (props) => {
    const{ level,color}= Piority(props.Piority)
  return (
    <div className="dashboard-card" onClick={props.clicked} style={{color:color}}>
    
        <h2>Total:{level}</h2>
        <p>{props.count}</p>
    </div>
  )
}
