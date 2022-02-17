// API Calling
// AccuWeather API Key = e4DK2XyYEyasgGGbuPdiUGIw9Br0QRdX

const key = "e4DK2XyYEyasgGGbuPdiUGIw9Br0QRdX";

// 2 requests so 2 different end points
const getCity = async (city) => {
    const baseURL = "http://dataservice.accuweather.com/locations/v1/cities/search";
    const query = `?apikey=${key}&q=${city}`;

    const response = await fetch(baseURL + query);
    const data = await response.json();

    return data[0];
}

const getWeather = async (id) => {
    const baseURL = "http://dataservice.accuweather.com/currentconditions/v1/";
    const query = `${id}?apikey=${key}`;

    const response = await fetch(baseURL + query);
    const data = await response.json();
    
    return data[0];
}
