const answerButtons = document.querySelector("#answerButtons");
const questionText = document.querySelector("#question");
const nextbutton = document.querySelector("#nextBtn");

let currQIndex = 0;
let score = 0;
let correctButton;


let questions = [
    {
        question: "What does HTML stand for?",
        answers: [
            {text: "Hyper Text Markup Language", isCorrect: true},
            {text: "High Transfer Machine Language", isCorrect: false},
            {text: "Hyperlink Text Management Language", isCorrect: false},
            {text: "Home Tool Markup Language", isCorrect: false},
        ]
    },

    {
        question: "Which language is mainly used for styling web pages?",
        answers: [
            {text: "Python", isCorrect: false},
            {text: "CSS", isCorrect: true},
            {text: "C++", isCorrect: false},
            {text: "Java", isCorrect: false},
        ]
    },

    {
        question: "What does JS stand for in web development?",
        answers: [
            {text: "JavaStructure", isCorrect: false},
            {text: "JustStyle", isCorrect: false},
            {text: "JavaScript", isCorrect: true},
            {text: "JetSyntax", isCorrect: false},
        ]
    },

    {
        question: "Which method is used to print something in the browser console?",
        answers: [
            {text: "console.print()", isCorrect: false},
            {text: "print.console()", isCorrect: false},
            {text: "console.log()", isCorrect: true},
            {text: "log.console()", isCorrect: false},
        ]
    },

    {
        question: "Which company developed JavaScript?",
        answers: [
            {text: "Microsoft", isCorrect: false},
            {text: "Google", isCorrect: false},
            {text: "Netscape", isCorrect: true},
            {text: "Apple", isCorrect: false},
        ]
    }
];

let lastQIndex = questions.length - 1;
let isLast;

function startQuiz()
{  
    currQIndex = 0;
    score = 0;
    isLast = false;
    nextbutton.innerHTML = "Next";
    showQuestion();
}
function resetState()
{
    questionText.innerHTML = "";
    answerButtons.innerHTML = "";
    nextbutton.style.display = "none";

}

function showQuestion()
{
    resetState();
    let currentQ = questions[currQIndex];
    
    let currentQNo = currQIndex + 1;

        if (currQIndex == questions.length)
        {
            questionText.innerHTML = `You got ${score} over ${questions.length}`;
            nextbutton.innerHTML = "Restart";
            isLast = true;
    
            nextbutton.style.display = "block";

        }
        else{

    questionText.innerHTML = currentQNo + ". " + currentQ.question;

    currentQ.answers.forEach(answer => {
        let button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        
        button.dataset.correct = answer.isCorrect; // i think we are putting metadata in the button
        if (answer.isCorrect)
        {
            correctButton = button;
        }
        button.addEventListener("click", selectAnswer);
        answerButtons.appendChild(button);
    })}
}

function selectAnswer(e)
{
    
    let selectedButton = e.target;
    let buttons =  document.querySelectorAll("#answerButtons > button")
    console.log(selectedButton.dataset.correct)
    let isCorrect = selectedButton.dataset.correct == "true";
    
    if (isCorrect)
        {
            selectedButton.classList.add("correct");
            score += 1;
        }
    else
    {   

        selectedButton.classList.add("incorrect");
        correctButton.classList.add("correct");
    }
    buttons.forEach(button =>
        {
            if (button == selectedButton || button == correctButton);
            else {
            button.disabled = true;
            button.classList.add("darkened")}
        })
    

       
    nextbutton.style.display = "block";
}


nextbutton.addEventListener("click", ()=>
    {
         currQIndex += 1;
        if(currQIndex > questions.length)    
            {
                startQuiz();
            }
        else{ 
        showQuestion();
           }

    })
showQuestion();
// next question -> empty all shit
