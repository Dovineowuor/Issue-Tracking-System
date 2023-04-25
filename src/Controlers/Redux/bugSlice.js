import { createSlice } from "@reduxjs/toolkit";
import { retrievebugs } from "./bugcontroller";
const slice=createSlice({
    name:"bug",
    initialState:[],
    reducers:{
        getBugs:state=> retrievebugs(),
        createbugs:(state,action)=>{

        },
        updatebugs:(state,action)=>{

        },
        markcomplete:(state,action)=>{
            
        }
    }
})

export default slice.reducer;
export const {getBugs,createbugs,updatebugs,markcomplete}=slice.actions