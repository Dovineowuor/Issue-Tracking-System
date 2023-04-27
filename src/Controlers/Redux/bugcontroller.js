
 import bugmodel from "E:/alx-zero_day/bugtruckerfrontend/frontend/src/Models/bugmodel.js"

export function retrievebugs(){
    let data=[];

    data.push(new bugmodel ({
        _id:12345,
        name:"test",
        details:"test",
        steps:"test", 
        version:"test",
        assigned:"test",
        creator:"test",
        priority:1,
        time:"test",


    }))

    let sorted =data.sort((a,b)=>{
        return(a.priority-b.priority)
    })
    return sorted
}