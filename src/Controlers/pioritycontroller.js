const colors=["#16FF00", "#DF2E38", "#E7AB9A"]
export default(priority)=>{
    const level =["Medium","High","Low"]

    return{
        level:(level[priority-1]),
        color:colors[priority-1]
    }
}