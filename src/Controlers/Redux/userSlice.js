import { createSlice } from "@reduxjs/toolkit";
const slice= createSlice(
    {
        name:"user",
        initialState:[{}],
        reducers:{
            getUser:(state)=>{
                state.push({name:"jaseykaz"})
                state.push({name:"rimahrakhi"})
            }
        }
    }
)

export default slice.reducer;
export const {getUser}=slice.actions;