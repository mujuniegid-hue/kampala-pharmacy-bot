# Kampala Pharmacy Chatbot

A command-line chatbot that helps pharmacy staff answer common customer
questions consistently: opening hours, services, prescription processing
time, and documents needed for repeat prescriptions.

Built for AI Masterclass 2, Week 3, Step 13.

## What it does

- Answers questions using a system prompt containing the pharmacy's facts
- Remembers the conversation, so follow-up questions like "how long will
  it take?" make sense
- Streams replies word by word
- Refuses to give medical advice and does not guess about stock

## Setup

1. Install Python 3 and clone this repository.
2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install the libraries:
   pip install -r requirements.txt
4. Get a free API key from Google AI Studio.
5. Copy `.env.example` to `.env` and paste your key in it.

## Run

python chat.py

Type `quit` to exit.

## Example conversation

See `test_conversation.txt` for an unedited three-turn test, where later
questions depend on earlier ones.

## How memory works

The model remembers nothing between calls. The program keeps a list called
`history` and sends the whole list with every request, using the roles
"user" and "model".

## Important notes

- The services, processing time and document list are PLACEHOLDERS for this
  assignment. Confirm them with the pharmacy owner before real use.
- The bot has no access to a stock list, so it directs staff to check shelves.
- Known issue: occasional missing spaces between words in replies.
- Model names change over time. If you get a "not found" error, update the
  MODEL line in `chat.py`.