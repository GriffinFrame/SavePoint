// Function to parse CSV data and update the page
function parseCSVData(csvData) {
    // Split the csv so it can be read
    const values = csvData.split(',');
    // Map the CSV data to the corresponding fields
    const data = {
        batteryPercentage: parseFloat(values[0]),
        batteryVoltage: parseFloat(values[1]),
        batteryCurrent: parseFloat(values[2]),
        outputVoltage: parseFloat(values[4]),
        outputCurrent: parseFloat(values[5]),
        inputVoltage: parseFloat(values[6]),
        inputCurrent: parseFloat(values[7]),
        inputPower: parseFloat(values[8]),
        outputPower: parseFloat(values[9]),
    };

    // Update the HTML elements with the parsed data
    document.getElementById('battery-percentage').textContent = `${(data.batteryPercentage * 100).toFixed(2)} %`; //adjust for percentage
    document.getElementById('battery-voltage').textContent = `${data.batteryVoltage.toFixed(2)} V`;
    document.getElementById('battery-current').textContent = `${data.batteryCurrent.toFixed(2)} A`;
    document.getElementById('input-voltage').textContent = `${data.inputVoltage.toFixed(2)} V`;
    document.getElementById('input-current').textContent = `${data.inputCurrent.toFixed(2)} A`;
    document.getElementById('output-voltage').textContent = `${data.outputVoltage.toFixed(2)} V`;
    document.getElementById('output-current').textContent = `${data.outputCurrent.toFixed(2)} A`;
    document.getElementById('input-power').textContent = `${(data.inputVoltage*data.inputCurrent).toFixed(2)} VA`;
    document.getElementById('output-power').textContent = `${(data.outputVoltage*data.outputCurrent).toFixed(2)} VA`;
}

// Fetch the CSV file from the same directory
function fetchCSVData() {
    fetch('data.csv')  
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text();  // Read the response as text
        })
        .then(csvData => parseCSVData(csvData))  // Parse and update the UI with data
        .catch(error => {
            console.error('Error fetching CSV data:', error);
            alert('Failed to fetch CSV data. Ensure the server is running and data.csv is in the correct location.');
        });
}

fetchCSVData();
setInterval(fetchCSVData, 2000);  // Update data every 5 seconds
