document.getElementById('input-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const soilPh = document.getElementById('soil-ph').value;
    const preference = document.getElementById('preferences').value;

    const response = await fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ location, soil_ph: soilPh, preference })
    });

    const data = await response.json();
    const resultsDiv = document.getElementById('recommendations');
    resultsDiv.innerHTML = data.recommendations.map(rec => `<p>${rec.crop}: ${rec.suitability}% suitability</p>`).join('');
});
