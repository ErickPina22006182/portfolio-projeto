function diaSemana(dia, mes, ano){
    const semana = [
        "Domingo",
        "Segunda-Feira",
        "Terça-Feira",
        "Quarta-Feira",
        "Quinta-Feira",
        "Sexta-Feira",
        "Sábado"
    ];
    return semana[new Date(`${ano}/${mes}/${dia}`).getDay()];
}


var region = document.querySelector('.region');
var dateFinal = document.querySelector('.date');
var icon = document.querySelector('.icon');
var teste = document.querySelector('.teste');
var temperatura = document.querySelector('.temperatura');

fetch('https://api.weatherapi.com/v1/current.json?key=9498b099bb8a404b995212307221106&q=Lisboa&aqi=no')
.then(response => response.json())
.then(data => {
    console.log(data);
    region.innerHTML = data.location.region;
    name.innerHTML = data.location.name;

    const date = data.location.localtime;
    const ano = date.substr(0,4);
    const mes = date.substr(5,2);
    const dia = date.substr(8,2);

    dateFinal.innerHTML = `${diaSemana(dia,mes,ano)} - ${dia}/${mes}/${ano}`;
    icon.src = data.current.condition.icon;
    temperatura.innerHTML = data.current.temp_c + " °C";

setInterval(showTime, 1000);
function showTime() {
    let time = new Date();
    let hour = time.getHours();
    let min = time.getMinutes();
    let sec = time.getSeconds();
    am_pm = "AM";

    if (hour > 12) {
        hour -= 12;
        am_pm = "PM";
    }
    if (hour === 0) {
        hr = 12;
        am_pm = "AM";
    }

    hour = hour < 10 ? "0" + hour : hour;
    min = min < 10 ? "0" + min : min;
    sec = sec < 10 ? "0" + sec : sec;

    document.getElementById("clock")
            .innerHTML = hour + ":"
        + min + ":" + sec + am_pm;
}
showTime();
});