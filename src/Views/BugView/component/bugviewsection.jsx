import React from 'react'
import './bugviewsection.css'
export default (props) => {
  return (
    <div className="viewsection">
        <h2>{props.title}</h2>
        <p>{props.info}</p>
    </div>
  )
}
