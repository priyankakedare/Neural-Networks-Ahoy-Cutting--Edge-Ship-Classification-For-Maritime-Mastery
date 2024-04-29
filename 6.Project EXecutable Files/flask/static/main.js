function predictImage() {
    const input = document.getElementById('imageInput');

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;

            img.onload = function() {
                const resultContainer = document.getElementById('resultContainer');
                const imageDisplay = document.getElementById('imageDisplay');
                const predictionText = document.getElementById('predictionText');

                // Display the uploaded image
                imageDisplay.innerHTML = `<img src="${img.src}" style="max-width: 300px;" />`;

                // Simulate image classification (replace with actual prediction logic)
                const predictedLabel = classifyImage();
                predictionText.innerHTML = `<strong>Prediction:</strong> ${predictedLabel}`;

                // Show the result container
                resultContainer.style.display = 'block';
            };
        };

        reader.readAsDataURL(input.files[0]);
    }
}
function classifyImage() {
    const shipTypes = ['Cargo Ship', 'Carrier Ship', 'Cruise Ship', 'Military Ship', 'Tanker Ship'];
    const randomIndex = Math.floor(Math.random() * shipTypes.length);
    return shipTypes[randomIndex];
}
