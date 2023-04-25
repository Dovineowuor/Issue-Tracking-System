import React from 'react'
import './editpanel.css'
export default ( props)=> {
  return (
    <div className="edit-panel">
        <button onClick={props.editclicked}>Edit</button>
        <button onClick={props.deleteclicked}>Delete</button>
    </div>
  )
}
