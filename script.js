const taskCount = 25

const tasksDiv = document.getElementById("tasks")

for(let i=0;i<taskCount;i++){

    const div = document.createElement("div")
    div.className="task"

    const input = document.createElement("input")
    input.placeholder="目標"

    const circle = document.createElement("div")
    circle.className="circle"

    const saved = localStorage.getItem("circle"+i)
    if(saved=="1") circle.classList.add("done")

    circle.onclick=()=>{
        circle.classList.toggle("done")

        if(circle.classList.contains("done"))
            localStorage.setItem("circle"+i,"1")
        else
            localStorage.setItem("circle"+i,"0")
    }

    div.appendChild(input)
    div.appendChild(circle)

    tasksDiv.appendChild(div)
}

function clearAll(){
    localStorage.clear()
    location.reload()
}
