# main.py
from flask import Flask, request, render_template
import asyncio
import markdown

# Assuming your task.py and search.py are correct and accessible
from task import generate_report_with_search
from search import fetch_search_results # This is a synchronous function now

app = Flask(__name__)

async def run_async_tasks(topic, groq_api_key, search_api_key):
    # Run the synchronous function in a separate thread
    search_results = await asyncio.to_thread(fetch_search_results, topic, api_key=search_api_key)
    
    # generate_report_with_search must be an async function
    raw_report = await generate_report_with_search(topic, groq_api_key, search_results)
    
    return raw_report

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    error = None

    topic = request.form.get("topic", "").strip()
    groq_api_key = request.form.get("groq_api_key", "").strip()
    search_api_key = request.form.get("search_api_key", "").strip()
    
    if request.method == "POST":
        if not all([topic, groq_api_key, search_api_key]):
            error = "All fields (Topic, Groq API key, and SerpAPI key) are required."
        else:
            try:
                # Use asyncio.run to execute the async wrapper function
                raw_report = asyncio.run(run_async_tasks(topic, groq_api_key, search_api_key))
                
                if raw_report:
                    report = markdown.markdown(raw_report, extensions=['tables', 'fenced_code'])
                else:
                    report = "<p>No report generated.</p>"
            
            except Exception as e:
                error = f"An error occurred: {str(e)}"
    
    return render_template(
        "index.html",
        report=report,
        error=error,
        topic=topic,
        groq_api_key=groq_api_key,
        search_api_key=search_api_key
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
