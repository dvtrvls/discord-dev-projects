const calcButton = document.querySelector(".calcButton")
const resultP = document.querySelector(".result");
const userInput = document.getElementById("date");

userInput.max = new Date().toISOString().split("T")[0];

calcButton.addEventListener("click", calcAge);

function calcAge()
{
    let birthDate = new Date(userInput.value);
    let todayDate = new Date();

    let d1 = birthDate.getDate();
    let m1 = birthDate.getMonth() + 1;
    let y1 = birthDate.getFullYear();

    let d2 = todayDate.getDate();
    let m2 = todayDate.getMonth() + 1;
    let y2 = todayDate.getFullYear();

    
    let d3, m3, y3;
    y3 = y2 - y1;
    
    if (m2>=m1)
        {
            m3 = m2-m1
        }
    else
        {
            y3--;
            m3 = 12+m2-m1
        }

    if (d2>=d1)
        {
            d3 = d2 - d1;
        }
    else
        {
            m3--;
            d3 = getDaysInMonth(y1, m1); + d2 - d1
        }
    if(m3<0)
        {
            m3 = 11;
            y3--;
        }

    resultP.innerHTML = `You are ${y3} Years, ${m3} Month, and ${d3} days old`

}


function getDaysInMonth(year, month)
{
    return new Date(year, month, 0).getDate();
}




