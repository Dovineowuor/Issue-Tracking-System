import React, { useState } from 'react'
import './bugform.css'
import bugmodel from "E:/alx-zero_day/bugtruckerfrontend/frontend/src/Models/bugmodel.js"

export default (props) => {
  const [bugobject,setBugObject]=useState(new bugmodel(props.bug))
  function inputchanged(e){
    setBugObject({
      ...bugobject,
      [e.target.name]:e.target.value
    })
  }
  return (
    <div className="bug-create">
      { props.title=="Edit Bug" && <button className='close-btn' onClick={props.close}>Close</button>}
      <h1>{props.title}</h1>

      <form >
        <label>Name:</label>
        <input name='name' placeholder='Bug Name' required onChange={inputchanged} value={bugobject.name}></input>
        <label>Details:</label>
        <textarea name="details" placeholder='Describe your bug' id="" onChange={inputchanged} value={bugobject.details} ></textarea>
        <label>Steps:</label>
        <textarea name="steps" placeholder='steps to recreacte the bug' id="" onChange={inputchanged} value={bugobject.steps}></textarea>
        <label>Priority</label>
        <select name="priority" id="" onChange={inputchanged} value={bugobject.priority}>
          <option value="1">High</option>
          <option value="2">Medium</option>
          <option value="2">Low</option>

        </select>
        <label>Assigned:</label>
        <select name="Asigned" id="" onChange={inputchanged} value={bugobject.assigned}>
          <option value="u1">Jane</option>
          <option value="u2">Rimah</option>
          <option value="u3">Rakhi</option>

        </select>

        <label>App Version:</label>
        <input type="App version" placeholder='Appversion' onChange={inputchanged} value={bugobject.version} />

        <button type='submit'>{props.title}</button>

      </form>

    </div>
  )
}
