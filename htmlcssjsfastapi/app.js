// app.js

function uploadFile() {
    const fileInput = document.getElementById("pdfFileInput");
    const summaryContainer = document.getElementById("summaryContainer");

    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a PDF file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://localhost:8000/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        summaryContainer.innerText = data.summary;
    })
    .catch(error => console.error("Error:", error));
}
