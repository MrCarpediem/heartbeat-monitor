# Heartbeat Monitor

A real-time monitoring system that aggregates and summarizes updates from team communication sources (Slack, Email, Notion) to provide heartbeat-style status updates for projects and teams.

## Features

- **Periodic Monitoring**: Runs on a configurable interval to check for new updates
- **Multi-Source Integration**: Collects data from Slack, Email, and Notion sources
- **Intelligent Classification**: Automatically categorizes updates as urgent or informational based on priority
- **Deduplication**: Prevents duplicate messages from appearing in digests
- **Clean Summaries**: Generates formatted digests highlighting critical information
- **Modular Architecture**: Easy to extend with new sources or classification logic

## Installation

1. Ensure you have Python 3.8+ installed

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (see Configuration section)

## Usage

Run the main application:
```bash
python -m app.main
```

The monitor will start and begin generating digests at the configured interval. Press `Ctrl+C` to stop the monitoring.

### Sample Output

```
==================================================
⏱ 2026-03-26 10:30:00 - Running heartbeat cycle...

 URGENT:
- Client blocked on API issue
- Client requested urgent update on delivery timeline

 INFO:
- Daily standup completed
- Task marked as completed in project board
```

## Configuration

Create a `.env` file in the root directory with the following variables:

- `INTERVAL_SECONDS`: Time interval between digest generations in seconds (default: 5)
- `ENV`: Environment setting (default: dev)

### API Configuration

#### Slack Setup
1. Create a Slack App at https://api.slack.com/apps
2. Add `channels:history` and `channels:read` OAuth scopes
3. Install the app to your workspace
4. Get the Bot User OAuth Token and Channel ID

#### Email Setup (IMAP)
1. Enable IMAP in your email settings
2. Generate an App Password (for Gmail) or use your regular password
3. Note your IMAP server (e.g., `imap.gmail.com` for Gmail)

#### Notion Setup
1. Create an integration at https://www.notion.com/my-integrations
2. Get your Internal Integration Token
3. Share your database with the integration
4. Get your Database ID from the URL

Example `.env` file:
```
INTERVAL_SECONDS=30
ENV=production

# Slack API Configuration
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token-here
SLACK_CHANNEL_ID=C1234567890

# Email API Configuration (IMAP)
EMAIL_HOST=imap.gmail.com
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_FOLDER=INBOX

# Notion API Configuration
NOTION_TOKEN=secret_your-notion-integration-token
NOTION_DATABASE_ID=your-database-id
```

## Project Structure

```
hb/
├── app/
│   ├── __init__.py
│   ├── main.py          # Application entry point
│   ├── scheduler.py     # Periodic task scheduler
│   ├── digest.py        # Digest generation service
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py  # Configuration management
│   ├── sources/
│   │   ├── __init__.py
│   │   ├── manager.py   # Source management
│   │   ├── slack.py     # Slack API integration
│   │   ├── email.py     # Email IMAP integration
│   │   └── notion.py    # Notion database integration
│   └── utils/
│       ├── classifier.py # Message classification logic
│       └── llm.py       # Summary formatting service
├── tests/
│   └── test_digest.py   # Unit tests
├── requirements.txt     # Python dependencies
├── .env                 # Environment configuration (create this file)
└── README.md           # This file
```

## Testing

Install pytest for testing:
```bash
pip install pytest
```

Run the test suite:
```bash
pytest tests/
```

## Dependencies

- **fastapi**: Web framework (prepared for future API endpoints)
- **uvicorn**: ASGI server for FastAPI
- **python-dotenv**: Environment variable management
- **requests**: HTTP client library for API calls
- **schedule**: Task scheduling library
- **slack-sdk**: Official Slack API client for real-time messaging
- **notion-client**: Official Notion API client for database integration
- **imapclient**: IMAP client for email access

## Architecture Overview

The system follows a modular architecture:

1. **Sources**: Individual modules for each data source (Slack, Email, Notion)
2. **Manager**: Orchestrates data collection from all sources
3. **Classifier**: Categorizes messages by priority and removes duplicates
4. **LLM Service**: Formats the final digest (placeholder for future AI summarization)
5. **Scheduler**: Runs the digest generation on a timer
6. **Main**: Application entry point

## Future Enhancements

- Real API integrations for Slack, Email, and Notion
- LLM-powered intelligent summarization and insights
- Web dashboard for digest visualization
- Notification channels (email, Slack, webhooks)
- Configurable priority thresholds and rules
- Historical digest storage and analytics
- REST API for external integrations
- Docker containerization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License.

- Real API integrations for Slack, Email, and Notion
- LLM-powered intelligent summarization
- Web dashboard for digest visualization
- Notification channels (email, Slack, etc.)
- Configurable priority thresholds
- Historical digest storage