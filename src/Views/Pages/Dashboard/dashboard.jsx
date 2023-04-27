import React, { useEffect } from 'react'
import Card from '../../Dashboard/card'
import { useDispatch,useSelector } from 'react-redux'
import{getBugs} from '../../../Controlers/Redux/bugSlice'
import bug from '../../../Models/bugmodel'
import { useNavigate } from 'react-router-dom';

export default () => {
const dispatch = useDispatch();
const bugs = useSelector(state => state.bugs);
const navigate = useNavigate();
let highcount = 0;
let midcount = 0;
let lowcount = 0;
function filterBugs(piority) {
    return bugs?.filter(bug => bug.piority === piority) ?? [];
  }
  
  function redirect(){
    navigate('/viewbugs');
  }
  
  useEffect(() => {
    dispatch(getBugs());
  }, []);
  
  useEffect(() => {
    if (bugs) {
      highcount = filterBugs(1).length;
      midcount = filterBugs(2).length;
      lowcount = filterBugs(3).length;
    }
  }, [bugs]);
  
  return (
    <div className="page-container">
      <Card Piority="1" count={highcount} clicked={redirect }/>
      <Card Piority="3" count={lowcount} clicked={redirect }/>
      <Card Piority="2" count={midcount} clicked={redirect } />
    </div>
  );
  };
  
  
  
  
  
  
  
  