// Function to call backend API and generate website
async function generate() {
  
  // Get user input from textarea
  const userInput = document.getElementById("prompt").value;

  // Send POST request to FastAPI backend
  const response = await fetch("http://127.0.0.1:8000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      user_input: userInput
    })
  });

  // Convert API response to JSON
  const data = await response.json();

  // Display generated HTML and CSS inside iframe
  const iframe = document.getElementById("preview");
  iframe.srcdoc = data.html + "<style>" + data.css + "</style>";
}
