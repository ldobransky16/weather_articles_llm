import openai
import logging
import json
from flask import current_app

logger = logging.getLogger(__name__)

def generate_article_text(weather_data, language, mode, date):
    openai.api_key = current_app.config['OPENAI_API_KEY']

    # Construct the prompt for OpenAI
    prompt = create_prompt(weather_data, language, mode, date)

    try:
        system_message = f"""
You are an assistant that generates {mode} weather articles.
Please create an article based on the provided weather data.
The article should be in {language}.
Return the article in JSON format with the following structure:
{{
  "headline": "Your headline",
  "lead": "Your lead paragraph",
  "body": "The main body of the article"
}}
Ensure all fields are included and start with the date in a user-friendly format.
"""
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # Or 'gpt-3.5-turbo' if that's what you're using
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7,
            n=1,
            # stop=None,  # Uncomment if you have specific stop conditions
        )
        content = response.choices[0].message['content'].strip()
        try:
            json_data = json.loads(content)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON response.")
            json_data = "Error: Could not parse JSON."

        return json_data

    except Exception as e:
        logger.exception(f"Error generating article text: {e}")
        return "Error generating article content."

def create_prompt(weather_data, language, mode, date):
    today = date.strftime('%Y-%m-%d')
    prompt = (f"wrote {mode} article. Today is {today}. data: {weather_data} are from {date} day. Response have to be in {language} language.")
    return prompt
