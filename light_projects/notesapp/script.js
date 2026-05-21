const createButton = document.querySelector(".create");
const buttonSound = new Audio("buttonClick.mp3")
const notesContainer = document.querySelector(".notes-container");
let notes = document.querySelectorAll(".inputBox")

function loadStorage()
{
    notesContainer.innerHTML = localStorage.getItem("notes")
}

loadStorage();

createButton.addEventListener("click", ()=>
    {
        buttonSound.play();
        let p = document.createElement("p");
        p.classList.add("inputBox");
        p.contentEditable = "true";
        let img = document.createElement("img");
        img.src = "./images/delete.png";
        p.appendChild(img);
        notesContainer.appendChild(p);
        updateStorage();
    });


notesContainer.addEventListener("click", function(e)
{
    if (e.target.tagName == "IMG")
        {
            e.target.parentElement.remove();
             buttonSound.play();
             updateStorage();
        }
    else if (e.target.tagName == "P")
        {
            notes = document.querySelectorAll(".inputBox");
            notes.forEach(note =>
                {
                    note.onkeyup = function()
                    {
                        updateStorage();
                    }
                })
            

        }
})



function updateStorage()
{
    localStorage.setItem("notes", notesContainer.innerHTML)
}