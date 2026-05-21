
const apiKey = "";
let endpoint = `https://api.openweathermap.org/data/2.5/weather?q=Cebu&appid=${apiKey}&units=metric`

// press button
// get the value in the input
// use it as a parameter in the api requests
// display the necessary details (use conditionals) if success otherwise handle error properly
let weather;
let windSpeed;
let humidity;
let temp;
let currCity;

const searchButton = document.querySelector(".search-cont button");
const searchInput = document.querySelector(".search-cont input");
const weatherIcon = document.querySelector(".weather-icon");
const weatherCont = document.querySelector(".weather-cont");
const loading = document.querySelector(".loading");
async function getWeather(city)
{
    
    weatherCont.style.opacity = 0;
    weatherCont.style.display = "block";
    endpoint = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
    loading.classList.remove("hidden");
    let response = await fetch(endpoint);
    
    try{
        
        if (!response.ok)
            {
            document.querySelector(".city-name").innerHTML = "something went wrong";        
            document.querySelector(".temperature").innerHTML = "--";
            document.querySelector(".currHumidity").innerHTML = "--";
            document.querySelector(".currWindspeed").innerHTML = "--"
            weatherIcon.src = ""
            
             setTimeout(()=> {weatherCont.style.opacity = 1}, 300);
             loading.classList.add("hidden");
                return;
            }
            
        let data = await response.json(); // this is also promised-based i think or maybe because it is asynchronous
        loading.classList.add("hidden");
        weather = data.weather[0].main;
        windSpeed = data.wind.speed;
        humidity = data.main.humidity;
        temp = data.main.temp;
        currCity = data.name;
        setTimeout(()=> {weatherCont.style.opacity = 1}, 300)

        document.querySelector(".city-name").innerHTML = currCity;
        document.querySelector(".temperature").innerHTML = Math.round(temp) + "°c";
        document.querySelector(".currHumidity").innerHTML = humidity + "%" ;
        document.querySelector(".currWindspeed").innerHTML = windSpeed + " km/h";
        document.querySelector(".city-name").innerHTML = currCity;
        
        if (weather === "Clear")
            {
                weatherIcon.src = "/images/clear.png";
                document.body.style.background = "linear-gradient(to right, #56ccf2, #2f80ed)";
            }
        else if (weather === "Clouds")
            {
                weatherIcon.src = "/images/clouds.png";
                 document.body.style.background = "linear-gradient(to right, #757f9a, #d7dde8)";
            }
        else if (weather === "Mist")
            {
                weatherIcon.src = "/images/mist.png"
            }
        else if (weather === "Drizzle")
            {
                weatherIcon.src = "/images/drizzle.png"
            }
        else if (weather === "Snow")
            {
                weatherIcon.src = "/images/snow.png"
            }
        else if (weather === "Rain")
            {
                weatherIcon.src = "/images/rain.png";
                document.body.style.background = "linear-gradient(to right, #373b44, #4286f4)";
            }
        

    } catch (error)
    {
      document.querySelector(".city-name").innerHTML = error.message;  
    }



    


    // use this function using await
}

searchButton.addEventListener("click", ()=>
    {
        console.log("hello");
        getWeather(searchInput.value);
    })

searchInput.addEventListener("keydown", (event) =>
{
    if (event.key === "Enter")
    {
        getWeather(searchInput.value);
    }
});
