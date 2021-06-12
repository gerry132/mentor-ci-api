async function getJsonResp() {
    const API_URL = "http://127.0.0.1:8000/";
    const response = await fetch(API_URL, {
        method: "GET",
    });

    const data = await response.json();

    if (response.ok) {
        //let jsonData = JSON.parse(data).quiz;
        console.log(data);
    } else {
        throw new Error(data.error);
    }
}
