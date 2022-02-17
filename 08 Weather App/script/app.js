// DOM Manipulation

const cityForm = document.querySelector('form');
const time = document.querySelector('img.time');
const icon = document.querySelector('.icon img');

const updateCity = async (city) => {
    const cityDetails = await getCity(city)
    const weather = await getWeather(cityDetails.Key)

    return {cityDetails, weather}
}

cityForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const city = cityForm.city.value.trim();
    cityForm.reset();

    updateCity(city)
        .then(data => updateUI(data))
        .catch(err => console.log(err));

})

// Update UI

const card = document.querySelector('.card');
const details = document.querySelector('.details');

const updateUI = (data) => {
    // const cityDetails = data.cityDetails;
    // const weather = data.weather;

    // We can also write the above as: object destructuring method used below
    const {cityDetails, weather} = data;

    console.log(cityDetails, weather)
    console.log(cityDetails.EnglishName)
    console.log(weather.WeatherText)
    console.log(weather.Temperature.Metric.Value)


    details.innerHTML = `
    <h5 class="my-5">${cityDetails.EnglishName}</h5>
    <div class="my-3">${weather.WeatherText}</div>
    <div class="display-4 my-4">
        <span>${weather.Temperature.Metric.Value}</span>
        <span>&deg;C</span>
    </div>
    `

    let timeSource = null;

    if (weather.IsDayTime) {
        timeSource = 'images/day.png'
    } else {
        timeSource = 'images/night.png'
    }

    time.setAttribute('src', timeSource)

    let iconSource = `images/AccuSvg/${weather.WeatherIcon}.svg`
    icon.setAttribute('src', iconSource)

    if (card.classList.contains('d-none')) {
        card.classList.remove('d-none')
    }

}