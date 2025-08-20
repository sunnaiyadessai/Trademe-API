How to Integrate with Trademe API

🚀 Project Overview

This Python script fetches closing soon listings from the [Trade Me Sandbox API](https://developer.trademe.co.nz/api-overview) using OAuth1 authentication. It can be extended to any other categories like Property, Motor, Jobs, and Services etc. 🔥

🚀 Features

🌟 Authenticates using OAuth1

🌟 Queries the `/listings/closing.json` endpoint

🌟 Filters listings by region (Auckland)

🌟 Scalable Integration: Can be extended to fetch data for Motor, Jobs, and other categories.

📦 Tech Stack

Language: Python 🐍

API: Trademe API

Libraries:

requests - For HTTP requests.

requests-oauthlib - For OAuth 1.0a authentication.

python-dotenv - For managing environment variables.

🚀 Getting Started

1️⃣ Clone the Repository

git clone  cd Trademe-API-Integration

2️⃣ Create a Virtual Environment

python3 -m venv venv source venv/bin/activate # For Linux/Mac venv\Scripts\activate # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Create a .env File

Add your API keys and secrets in a .env file:

CONSUMER_KEY=your_consumer_key CONSUMER_SECRET=your_consumer_secret ACCESS_TOKEN=your_access_token ACCESS_TOKEN_SECRET=your_access_token_secret

5️⃣ Run the Script

python get_property_listings.py

🔄 Planned Improvements

🏎️ Additional Categories: Fetch data for Motor, Jobs, and other categories.

📊 Data Visualization: Regional price distribution and trend analysis.

🔒 Security Considerations

DO NOT share your .env file or API keys publicly.

.gitignore is configured to exclude sensitive files.

🛠️ Contributing

Feel free to submit issues and pull requests. For major changes, open an issue first to discuss what you would like to change.

👉 Ready to explore Trademe's data? Let's get started! 🚀🔥
