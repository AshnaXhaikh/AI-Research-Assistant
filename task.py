import asyncio
from groq import Groq

async def ask_groq(prompt: str, api_key: str) -> str:
    """
    Send a prompt to Groq API and get the generated response.

    Parameters:
        prompt (str): The input text to generate a response from.
        api_key (str): User's Groq API key.

    Returns:
        str: Generated text from Groq.
    """
    try:
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a research assistant that writes detailed, well-cited research reports."},
                {"role": "user", "content": prompt}
            ],
            n=1
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"Groq API error: {str(e)}"


def generate_base_prompt(topic: str, include_search: str = None) -> str:
    """
    Create the base prompt for generating a research report.
    Optionally include real-time search results.
    """
    prompt = (
        f"Generate a detailed research paper on the topic: '{topic}'. "
        "The report should include introduction, background and context, "
        "current state of research and technology, key findings or insights, "
        "case studies or examples, future directions or trends, and references. "
        "Make it suitable for academic or professional readers."
    )
    if include_search:
        prompt += f"\n\nRecent web findings:\n{include_search}"
    return prompt


async def enhance_report(initial_report: str, topic: str, api_key: str, include_search: bool = False) -> str:
    """
    Enhance the initial report with more technical details, examples, and clarity.
    """
    search_note = " with recent web insights" if include_search else ""
    enhancement_prompt = (
        f"Here is an initial research report on '{topic}'{search_note}:\n\n{initial_report}\n\n"
        "Enhance this report by adding more technical details, examples, "
        "improving clarity and depth, simulating visual sequences, describing "
        "charts or infographics if applicable, suggesting practical applications "
        "and implications, while keeping an academic tone."
    )
    return await ask_groq(enhancement_prompt, api_key)


async def generate_report(topic: str, api_key: str) -> str:
    """
    Generate a research report in two steps: initial draft and enhanced draft.
    """
    initial_report = await ask_groq(generate_base_prompt(topic), api_key)
    return await enhance_report(initial_report, topic, api_key)


async def generate_report_with_search(topic: str, api_key: str, search_results: str) -> str:
    """
    Generate a research report using both the topic and real-time search results.
    """
    initial_report = await ask_groq(generate_base_prompt(topic, include_search=search_results), api_key)
    return await enhance_report(initial_report, topic, api_key, include_search=True)
