from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# DeepSeek API configuration
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_API_KEY = "your_deepseek_api_key"

# Robot descriptions
robots = {
    "CRUZR": {
        "name": "CRUZR",
        "description": "CRUZR is a cloud-based intelligent commercial service robot designed for interactive tasks. It features AI-powered interaction, autonomous navigation, facial recognition, and customizable applications. Students can learn about NLP, computer vision, and cloud computing.",
        "image": "aiSTEM_CRUZR.png",
    },
    "WELLI": {
        "name": "WELLI",
        "description": "WELLI is a smart companion robot designed for healthcare and companionship. It supports voice and gesture interaction, emotional expression, and remote monitoring. Students can explore gesture recognition, emotional expression, and remote monitoring.",
        "image": "aiSTEM_WELLI.png",
    },
    "AUCARI": {
        "name": "AUCARI",
        "description": "AUCARI is an open shelf delivery robot designed for autonomous delivery tasks. It features SLAM navigation, multi-robot collaboration, and customizable workflows. Students can learn about SLAM, autonomous navigation, and workflow optimization.",
        "image": "aiSTEM_AUCARI.png",
    },
}

@app.route("/")
def index():
    return render_template("index.html", robots=robots)

@app.route("/ask", methods=["POST"])
def ask():
    selected_robot = request.json.get("robot")
    task = request.json.get("task")

    # Prepare the prompt for DeepSeek
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant for junior education in Australia. Teach students about AI prompt engineering for the following robots: CRUZR, WELLI, and AUCARI. Do not disclose any private or illegal information.",
        },
        {
            "role": "user",
            "content": f"Here are descriptions of the robots:\n\nCRUZR: {robots['CRUZR']['description']}\n\nWELLI: {robots['WELLI']['description']}\n\nAUCARI: {robots['AUCARI']['description']}",
        },
        {"role": "user", "content": f"Task for {selected_robot}: {task}"},
    ]

    # Call DeepSeek API
    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-chat",
                "messages": messages,
                "max_tokens": 200,
                "temperature": 0.7,
            },
        )
        response.raise_for_status()
        ai_response = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        ai_response = f"Error: {str(e)}"

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)