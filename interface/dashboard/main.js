document.getElementById('input-form').addEventListener('submit', async function (event) {
    event.preventDefault(); 

    const location = document.getElementById('location').value;
    const soilPh = parseFloat(document.getElementById('soil-ph').value);
    const preference = document.getElementById('preferences').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ location, soil_ph: soilPh, preference })
        });

        if (response.ok) {
            const data = await response.json();
            const recommendationsDiv = document.getElementById('recommendations');
            recommendationsDiv.innerHTML = `
                <h3>Recommended Crops:</h3>
                <ul>${data.recommended_crops.map(crop => `<li>${crop}</li>`).join('')}</ul>
            `;
        } else {
            console.error('Error:', response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
