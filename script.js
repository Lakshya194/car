document.getElementById("predictionForm").onsubmit = async function(event) {
    event.preventDefault();

    let data = {
        "km driven": document.getElementById("km_driven").value,
        "fuel": document.getElementById("fuel").value,
        "seller type": document.getElementById("seller_type").value,
        "transmission": document.getElementById("transmission").value,
        "owner": document.getElementById("owner").value
    };

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    let result = await response.json();
    document.getElementById("result").innerText = "Predicted Price: $" + result.predicted_price.toFixed(2);
};
