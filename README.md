
## Live Demo

Try the application: [AI Sales Assistant](https://ai-sales-assistant-crfcsjeaxagpf4dkj6pqkv.streamlit.app/)

This prototype demonstrates customer inquiry analysis, potential objection identification, sales discovery questions, and editable follow-up email drafts.

# AI Sales Assistant

A free sales enablement prototype that helps sales representatives analyze customer inquiries, identify potential pain points and objections, recommend discovery questions, and draft customer follow-up emails.

## Project Overview

Sales teams spend time reviewing customer conversations, identifying concerns, and preparing follow-up messages. This prototype demonstrates how a lightweight tool can help organize those tasks and support a more consistent sales workflow.

## Features

- **Customer inquiry analysis:** Detects predefined keywords associated with customer pain points and objections.
- **Objection identification:** Flags potential price, budget, and competitor concerns.
- **Recommended next steps:** Suggests a sales approach based on detected keywords.
- **Discovery questions:** Provides questions to help representatives better understand customer needs.
- **Follow-up email drafts:** Generates editable email templates in different tones.
- **Human review checklist:** Reminds representatives to verify claims, pricing, policies, and customer details.

## Technology Stack

- Python
- Streamlit
- Git and GitHub for version control and project sharing

## How It Works

The current prototype uses Python keyword matching and predefined email templates. It does not connect to a live AI model or use a paid API.

The application checks customer inquiry text for specific keywords, displays potential concerns, and recommends a next step. Users can then review the suggested follow-up email.

Keyword matching has limitations. It may miss relevant information, misinterpret a customer's intent, or flag a concern that is not actually present.

## Run Locally

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

7. Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Testing

Test the application with sample inquiries that include:

- Customer follow-up challenges
- Manual or inefficient workflows
- Price and budget objections
- Competitor comparisons
- Inquiries without predefined keywords
- Empty input

Review the results for accuracy and relevance.

## Privacy and Responsible Use

- Enter fictional or anonymized customer information when testing.
- Review all generated drafts before using them.
- Verify pricing, product claims, and company policies.
- Do not treat keyword-based suggestions as definitive conclusions about a customer.

## Future Improvements

- Integrate a language model through an appropriately secured API.
- Improve intent detection beyond keyword matching.
- Add configurable sales playbooks and objection-handling guidance.
- Add automated tests and evaluation examples.
- Support CRM integrations and structured sales reporting.
- Measure response quality, relevance, and time saved.

## Project Goal

This project demonstrates practical skills in Python, application development, sales workflow design, customer experience, and responsible AI implementation. The current version is a foundational prototype intended for further development.

## Testing

The application includes four automated tests covering:

- Application startup without errors
- Empty customer inquiry handling
- Follow-up email draft generation
- Personalization based on customer concerns

### Run the Tests Locally

1. Activate your project's virtual environment.
2. Install the testing dependency:

   ```bash
   python -m pip install pytest
