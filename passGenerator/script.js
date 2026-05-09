const button = document.querySelector("button");
const passwordBox = document.getElementById("password");
const copy = document.querySelector(".inputBox img");

const passwordLength = 12;


const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const lowercase = uppercase.toLowerCase();
const specialChar  = "!@#$%^&*()?";
const numbers = "12345678";
const allChar = uppercase + lowercase + specialChar + numbers;

function generatePassword()
{
    let password = "";
    while (password.length != passwordLength){
    password += allChar[Math.floor(Math.random() * allChar.length)];
    }
    passwordBox.value = password;
}


function copyPassword()
{
    passwordBox.select();
    document.execCommand("copy");

}

button.addEventListener("click", generatePassword);
copy.addEventListener("click", copyPassword)






