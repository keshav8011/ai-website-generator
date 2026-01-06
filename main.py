# Import required libraries
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# Enable CORS so frontend (HTML/JS) can communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Allow requests from any origin
    allow_methods=["*"],     # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],     # Allow all headers
)

# Define the expected request body using Pydantic
class Prompt(BaseModel):
    user_input: str  # Stores the website description entered by user


@app.post("/generate")
def generate_website(prompt: Prompt):
    """
    API endpoint to generate website code based on user input.
    This function simulates AI-generated output.
    It can later be connected to OpenAI or any LLM.
    """

    # Generate basic HTML dynamically using user input
    html = f"""
    <html>
      <head>
        <title>Generated Website</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>
        <nav>My AI Website</nav>
        <section class="hero">
          <h1>{prompt.user_input.title()}</h1>
          <p>This website was generated using AI logic.</p>
        </section>
      </body>
    </html>
    """

    # Basic CSS styling for layout and look
    css = """
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
    }
    nav {
        background-color: #333;
        color: white;
        padding: 15px;
        text-align: center;
        font-size: 18px;
    }
    .hero {
        padding: 40px;
        text-align: center;
    }
    """

    # Simple JavaScript (placeholder for future interactivity)
    js = """
    console.log("AI-generated website loaded successfully");
    """

    # Return generated website files as JSON
    return {
        "html": html,
        "css": css,
        "js": js
    }
