const items = document.querySelectorAll("#listContainer li");

const taskInput = document.querySelector("#searchInput");
const addButton = document.querySelector(".row > button");
const listContainer = document.getElementById("listContainer")
const alertExitbutton = document.querySelector(".alert-box button")
const alertBox = document.querySelector(".alert-box")
let tasks = []
addButton.addEventListener("click", addTask);

alertExitbutton.addEventListener("click", ()=>
    {
        alertBox.style.display = "none";
    })

function addTask()
{
    let task = searchInput.value;
    if (task.trim() == '')
        {
            alertBox.style.display = "block";
            return
        }
        let li = document.createElement("li");
        li.textContent = task;
        let span = document.createElement("span");
        span.innerHTML = '\u00d7';
        li.appendChild(span);
        li.classList.add("new-task")
        listContainer.appendChild(li);
         setTimeout(()=>{ li.classList.add("show");}, 100)
   
    taskInput.value = "";
    saveData();
    tasks.push(task);
    
}


listContainer.addEventListener("click", (e)=>
    {
        if (e.target.tagName == "LI")
            {
                e.target.classList.toggle("checked");
            }
        else if (e.target.tagName == "SPAN")
        {
            e.target.parentElement.remove();
        }
        saveData();
    })

function saveData()
{
    localStorage.setItem("data", listContainer.innerHTML)
}
function showData()
{
    listContainer.innerHTML = localStorage.getItem("data");
    const allTasks = document.querySelectorAll("li");
    allTasks.forEach( (task, index) => 
        {
            setTimeout(()=>{ task.classList.add("show");},  300)
        })
}

showData();