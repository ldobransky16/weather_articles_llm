<!DOCTYPE html>


<h1>Weather Article Generator</h1>

<p>A Flask-based RESTful API that retrieves weather data based on geographic coordinates and generates weather articles using OpenAI’s GPT models. The application integrates with the <a href="https://openweathermap.org/api">OpenWeatherMap API</a> to fetch current weather data and uses OpenAI’s API to generate articles in different modes (e.g., “catastrophic”, “sensational”) based on the weather conditions.</p>

<h2>Features</h2>
<ul>
    <li>Retrieves current weather data based on latitude and longitude.</li>
    <li>Generates weather articles in different modes using OpenAI’s GPT models.</li>
    <li>Supports different languages (English and Slovak).</li>
    <li>Provides a RESTful API with proper documentation using Flask-RESTX.</li>
    <li>Includes a CI/CD pipeline for automated deployment to cloud platforms.</li>
</ul>

<h2>Prerequisites</h2>
<ul>
    <li><strong>Python 3.8+</strong></li>
    <li><strong>Docker</strong> and <strong>Docker Compose</strong> (if running with Docker)</li>
    <li><strong>OpenAI API Key</strong>: Sign up at <a href="https://platform.openai.com/signup/">OpenAI</a> to get an API key.</li>
    <li><strong>OpenWeatherMap API Key</strong>: Sign up at <a href="https://openweathermap.org/api">OpenWeatherMap</a> to get an API key.</li>
    <li><strong>Git</strong>: For cloning the repository.</li>
</ul>

<h2>Installation</h2>

<h3>Clone the Repository</h3>
<pre class="code-block"><code>git clone https://github.com/lukas.dobransky/weather-article-generator.git
cd weather-article-generator
</code></pre>

<h3>Environment Variables</h3>
<p>Create a <code>.env</code> file in the root directory and add the following environment variables:</p>
<pre class="code-block"><code>OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_openweathermap_api_key
SECRET_KEY=your_secret_key
API_KEY=your_api_key  # Optional, if using API key authentication

#Database config
POSTGRES_USER=postgres-user
POSTGRES_PASSWORD=postgres-password
POSTGRES_DB=postgres-db-name
SQLALCHEMY_DATABASE_URI=postgresql://postgres:postgres@db:5432/weatherdb
</code></pre>
<p>Replace <code>your_openai_api_key</code> and <code>your_openweathermap_api_key</code> with your actual API keys.</p>

<h2>Running the Application</h2>

<h3>Using Docker Compose</h3>
<p><strong>Step 1:</strong> Build and run the Docker containers.</p>
<pre class="code-block"><code>docker-compose up --build
</code></pre>
<p>This command will build the Docker images and start the application and database containers.</p>

<p><strong>Step 2:</strong> Access the API documentation.</p>
<p>Open your browser and navigate to <a href="http://localhost:5001/docs">http://localhost:5001/docs</a> to view the Swagger UI documentation.</p>

<h3>Running Locally without Docker</h3>

<p><strong>Step 1:</strong> Create a virtual environment.</p>
<pre class="code-block"><code>python -m venv venv
</code></pre>

<p><strong>Step 2:</strong> Activate the virtual environment.</p>
<ul>
    <li>On Linux/Mac:
        <pre class="code-block"><code>source venv/bin/activate</code></pre>
    </li>
    <li>On Windows:
        <pre class="code-block"><code>venv\Scripts\activate</code></pre>
    </li>
</ul>

<p><strong>Step 3:</strong> Install dependencies.</p>
<pre class="code-block"><code>pip install -r requirements.txt
</code></pre>

<p><strong>Step 4:</strong> Set environment variables.</p>
<p>You can set environment variables in your shell or create a <code>.env</code> file.</p>

<p><strong>Step 5:</strong> Run the application.</p>
<pre class="code-block"><code>flask run
</code></pre>
<p>By default, the application will run on <a href="http://localhost:5001">http://localhost:5001</a>.</p>

<p><strong>Step 6:</strong> Access the API documentation.</p>
<p>Open your browser and navigate to <a href="http://localhost:5001/docs">http://localhost:5001/docs</a> to view the Swagger UI documentation.</p>

<h2>API Documentation</h2>

<h3>Endpoints</h3>

<h4>GET /weather_article/</h4>

<p>Generates a weather article based on location and date.</p>

<p><strong>URL:</strong> <code>/weather_article/</code></p>
<p><strong>Method:</strong> <code>GET</code></p>

<h3>Request Parameters</h3>
<table>
    <tr>
        <th>Parameter</th>
        <th>Type</th>
        <th>Required</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>latitude</code></td>
        <td>float</td>
        <td>Yes</td>
        <td>Latitude of the location (between -90 and 90).</td>
    </tr>
    <tr>
        <td><code>longitude</code></td>
        <td>float</td>
        <td>Yes</td>
        <td>Longitude of the location (between -180 and 180).</td>
    </tr>
    <tr>
        <td><code>date</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Date in <code>YYYY-MM-DD</code> format.</td>
    </tr>
    <tr>
        <td><code>language</code></td>
        <td>string</td>
        <td>No</td>
        <td>Language code (<code>en</code> or <code>sk</code>). Default is <code>en</code>.</td>
    </tr>
</table>

<p><strong>Example Request:</strong></p>
<pre class="code-block"><code>http://localhost:5001/weather_article?latitude=48.7445283&longitude=21.701820&language=sk&date=2024-10-31
</code></pre>

<h3>Successful Response (200 OK):</h3>
<pre class="code-block"><code>{
  "location": {
    "name": "Sample City",
    "country": "US",
    "coordinates": {
      "latitude": 48.7445283,
      "longitude": 21.70182
    }
  },
  "weather": {
    "description": "clear sky",
    "temperature": 20.5,
    "humidity": 55,
    "wind_speed": 3.2
  },
  "article": {
    "catastrophic": {
      "headline": "Disaster Strikes Sample City!",
      "lead": "An unprecedented event has shocked Sample City.",
      "body": "In an unexpected turn of events, the city has faced an unusual weather phenomenon..."
    },
    "sensational": {
      "headline": "Exciting Times in Sample City!",
      "lead": "Residents of Sample City experience thrilling weather.",
      "body": "The weather in Sample City has taken a sensational twist, bringing excitement to all..."
    }
  }
}
</code></pre>

<h3>Error Response (400 Bad Request):</h3>
<pre class="code-block"><code>{
  "error": "Validation Error",
  "details": {
    "latitude": ["Missing data for required field."]
  }
}
</code></pre>

<h3>Notes:</h3>
<ul>
    <li>If the provided date is not today’s date, the application returns mock data with random values.</li>
    <li>The articles are generated in the specified language and mode.</li>
    <li>Modes include “catastrophic” and “sensational”.</li>
</ul>

<h2>Testing</h2>

<p>To test the API endpoints, you can use:</p>
<ul>
    <li><strong>Swagger UI</strong>: Available at <a href="http://localhost:5001/docs">http://localhost:5001/docs</a> (or <a href="http://localhost:5001/docs">http://localhost:5001/docs</a> if using Docker).</li>
    <li><strong>cURL</strong>: Use command-line requests to test endpoints.</li>
    <li><strong>Postman</strong>: Create requests to test API functionality.</li>
</ul>

<p><strong>Example cURL Request:</strong></p>
<pre class="code-block"><code>curl -X GET "http://localhost:5001/weather_article/?latitude=48.7445283&longitude=21.701820&date=2023-10-25&language=en"
</code></pre>

<h2>Deployment</h2>

<h3>CI/CD Pipeline</h3>

<p>The application includes a CI/CD pipeline using GitHub Actions to automate deployment to cloud platforms.</p>

<h3>GitHub Actions (AWS Elastic Beanstalk)</h3>

<p>A GitHub Actions workflow (<code>.github/workflows/deploy.yml</code>) is set up to:</p>
<ul>
    <li>Build and push Docker images to Docker Hub.</li>
    <li>Deploy the application to AWS Elastic Beanstalk.</li>
</ul>

<p><strong>To set up:</strong></p>
<ol>
    <li><strong>AWS Configuration:</strong>
        <ul>
            <li>Create an AWS Elastic Beanstalk application and environment.</li>
            <li>Configure environment variables in Elastic Beanstalk (e.g., <code>OPENAI_API_KEY</code>, <code>WEATHER_API_KEY</code>).</li>
        </ul>
    </li>
    <li><strong>GitHub Secrets:</strong>
        <ul>
            <li>Add AWS credentials and Docker Hub credentials to your repository’s secrets:
                <ul>
                    <li><code>AWS_ACCESS_KEY_ID</code></li>
                    <li><code>AWS_SECRET_ACCESS_KEY</code></li>
                    <li><code>AWS_ACCOUNT_ID</code></li>
                    <li><code>DOCKERHUB_USERNAME</code></li>
                    <li><code>DOCKERHUB_TOKEN</code></li>
                </ul>
            </li>
        </ul>
    </
