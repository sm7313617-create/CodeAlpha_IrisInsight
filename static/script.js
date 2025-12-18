document.getElementById("predict-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        sepal_length: parseFloat(document.getElementById("sepal_length").value),
        sepal_width: parseFloat(document.getElementById("sepal_width").value),
        petal_length: parseFloat(document.getElementById("petal_length").value),
        petal_width: parseFloat(document.getElementById("petal_width").value)
    };

    const res = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await res.json();

    document.getElementById("result-area").classList.remove("hidden");
    document.getElementById("predicted-species").innerText =
        "Iris " + result.species;

    if (result.confidence) {
        const conf = document.getElementById("confidence");
        conf.innerText = `Confidence: ${(result.confidence * 100).toFixed(2)}%`;
        conf.classList.remove("hidden");
    }
});
