const days=["Sunday","Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday"    ];
const months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
setInterval(()=> {
    const time = new Date();
    const date =time.getDate();
    const month =time.getMonth();
    const day =time.getDay();
    const hour =time.getHours();
    const min =time.getMinutes();
    if (min<10){
        document.querySelector(".time").innerText= hour+":0"+min;
    }else{
        document.querySelector(".time").innerText= hour+":"+min;
    }
    document.querySelector(".date").innerText= days[day]+", "+months[month]+" "+date;                  
},1000);