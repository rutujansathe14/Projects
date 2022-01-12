let weather={
    apiKey: "8e8ebd09cc8035f31a21e80c6bc7b746",
    fetchWeather: function(city){
        fetch(
            "https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&appid=" +this.apiKey
        ).then((response)=> response.json())
        .then((data)=> this.displayWeather(data));
    },
    
    displayWeather: function(data,info){
        const{lon,lat}=data.coord;
        const{name,visibility}=data;
        const{country}=data.sys;
        const{icon,description}=data.weather[0];
        const{temp,humidity,pressure}=data.main;
        const{speed}=data.wind;
        document.querySelector(".city").innerText=name+", "+country;
        console.log(lon,lat);
        document.querySelector(".icon").src="http://openweathermap.org/img/wn/"+icon+".png";
        document.querySelector(".description").innerText=description;
        document.querySelector(".temp").innerText=temp+"°С";
        document.querySelector(".humidity").innerText="Humidity: "+humidity+"%";
        document.querySelector(".wind").innerText="Wind: "+speed+" m/s";
        document.querySelector(".pressure").innerText="Pressure: ↓ "+pressure+" mb";
        document.querySelector(".visibility").innerText="Visibility: "+visibility/1000+" km";
        document.querySelector(".weather").classList.remove("loading");
        document.body.style.backgroundImage= "url('https://source.unsplash.com/1600x900/?" +name+ "')";

        fetch(
            "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+this.apiKey
        ).then((response)=> response.json())
        .then((info)=> this.getDateTime(info));
    },

    getDateTime: function(info){
        const{timezone}=info;
        document.querySelector(".time").innerHTML=new Date().toLocaleString("en-US",{timeZone:timezone,timeStyle:'short',hourCycle:'h12'});
        document.querySelector(".date").innerHTML=new Date().toLocaleString("en-US",{timeZone:timezone,dateStyle:'full'});
    },

    search: function(){
        this.fetchWeather(document.querySelector(".search-bar").value);
    },
};




document.querySelector(".search button").addEventListener("click",function(){
    weather.search();
});

document.querySelector(".search-bar").addEventListener("keyup",function(event){
    if (event.key=="Enter"){
        weather.search();
    }
});



weather.fetchWeather("Mumbai");

