# VAPI Call Tracker

A Flask application for tracking and monitoring VAPI voice AI calls.

## Features

- Webhook endpoint for receiving call data from VAPI
- Stores call information in SQLite database
- Dashboard interface for viewing call history
- Tracks call duration, transcripts, summaries, and costs

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

The app will start on port 3000 (or PORT environment variable).

## Endpoints

- `/webhook` - POST endpoint for VAPI webhook
- `/dashboard` - Web interface to view call history

## Deployment

Configured for deployment with Procfile (Heroku-compatible).
