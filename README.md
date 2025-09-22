# 🧠 AI Research Assistant

The **AI Research Assistant** is a web application that leverages **large language models** and **real-time search** to generate **detailed, well-structured research reports** on any given topic.

Developed by **Ashna Imtiaz**.

---

## ✨ Features

* **AI-Powered Report Generation**
  Generates comprehensive research reports using the **Groq API**.

* **Real-Time Data Integration**
  Utilizes **SerpAPI** to fetch the most recent and relevant information from the web.

* **Interactive UI**
  A clean, user-friendly interface with collapsible sections for easy navigation and reading.

* **Copy to Clipboard**
  Easily copy the entire report with a single click.

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **APIs:**

  * Groq (for LLM)
  * SerpAPI (for real-time search)

---

## 🚀 Getting Started

### Prerequisites

You will need API keys for both **Groq** and **SerpAPI**.

* **Groq:** Sign up at [https://console.groq.com/](https://console.groq.com/) to get your API key.
* **SerpAPI:** Sign up at [https://serpapi.com/](https://serpapi.com/) to get your API key.

### Installation

```bash
# Clone the repository
git clone https://github.com/AshnaXhaikh/AI-Research-Assistant/
cd https://github.com/AshnaXhaikh/AI-Research-Assistant/

# Install required Python packages
pip install Flask groq serpapi markdown
```

### Usage

```bash
# Run the Flask application
python main.py
```

1. Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Enter your API keys for Groq and SerpAPI in the sidebar.
3. Type your desired research topic and click **"Generate Report"**.
4. The application will fetch search results and use them to create a **detailed report**, displayed on the right side of the screen.
