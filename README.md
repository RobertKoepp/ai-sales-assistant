
# AI Sales Assistant

A sales enablement prototype built with Python and Streamlit that helps sales representatives analyze customer inquiries, identify potential pain points and objections, and draft personalized follow-up emails.

## Live Demo

**[Launch the AI Sales Assistant](https://ai-sales-assistant-crfcsjeaxagpf4dkj6pqkv.streamlit.app/)**

Try the application with a sample customer inquiry and explore its analysis, recommended next steps, and editable email drafts.

## Project Overview

Sales representatives need to understand customer needs, respond to objections, and follow up consistently. This project explores how a lightweight application can support that workflow by organizing customer concerns and generating relevant follow-up messages.

The current version uses Python keyword matching and predefined templates rather than a live AI model. It is a working prototype designed to demonstrate sales workflow design, application development, automated testing, and deployment.

## Features

- **Customer inquiry analysis:** Identifies predefined keywords associated with potential customer pain points.
- **Objection detection:** Flags possible price, budget, and competitor-related concerns.
- **Recommended next steps:** Suggests a sales approach based on detected concerns.
- **Discovery questions:** Provides questions to help sales representatives understand customer needs and current processes.
- **Personalized email drafts:** Uses detected concerns to customize follow-up messages.
- **Multiple communication tones:** Supports friendly and professional, concise, and consultative email styles.
- **Editable output:** Allows representatives to review and edit a draft before using it.
- **Human review guidance:** Reminds users to verify customer details, pricing, product claims, and company policies.

## Technology Stack

- **Python:** Application logic and keyword matching
- **Streamlit:** Interactive web application and user interface
- **pytest:** Automated testing
- **GitHub:** Source code hosting and version control
- **GitHub Actions:** Automated test workflow
- **Streamlit Community Cloud:** Public application deployment

## How It Works

1. A user enters a customer inquiry.
2. The application checks the text for predefined keywords.
3. Potential pain points and objections are displayed.
4. A recommended next step and discovery questions are provided.
5. The application generates an editable email draft using detected concerns and the selected communication tone.
6. The user reviews the output before using it.

The analysis relies on predefined rules. It does not understand customer intent in the way a language model does, and its recommendations may be incomplete or inaccurate.

## Run Locally

### Prerequisites

- Python 3
- Git

### Setup

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/RobertKoepp/ai-sales-assistant.git
cd ai-sales-assistant
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the application dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Automated Testing

The project includes four automated tests covering:

- Application startup without errors
- Empty customer inquiry handling
- Follow-up email draft generation
- Personalization based on detected customer concerns

Install the testing dependency:

```bash
python -m pip install pytest
```

Run the tests:

```bash
python -m pytest -q
```

The current test suite contains nine automated tests covering application startup, input validation, draft generation, personalization, communication tones, and customer objection scenarios.

## Continuous Integration

GitHub Actions runs the automated test suite when changes are pushed to the `main` branch or when a pull request targets `main`.

The workflow installs Python, installs the project dependencies and pytest, and runs the tests. This helps identify regressions as the project evolves.

## Limitations and Responsible Use

- The application does not connect to a live AI model or require an AI API key.
- Keyword matching may miss relevant concerns or flag concerns that are not actually present.
- Email drafts use predefined templates and should not be treated as verified recommendations.
- Users should review all output before sending messages to customers.
- Product claims, pricing, discounts, and company policies must be verified independently.
- Use fictional or anonymized customer information when testing. Do not enter confidential customer data.

## Future Improvements

- Improve intent and objection detection beyond simple keyword matching.
- Explore integration with a language model through a securely configured API.
- Expand automated test coverage and evaluate output quality across more scenarios.
- Add configurable sales playbooks and objection-handling guidance.
- Explore CRM integrations and structured sales reporting.
- Evaluate usability, relevance, and potential time savings.

## Project Goals

This project demonstrates practical experience with Python application development, sales workflow design, customer experience, automated testing, continuous integration, and cloud deployment. It serves as a foundation for further exploration of AI implementation and sales enablement solutions.
