
from streamlit.testing.v1 import AppTest


SAMPLE_INQUIRY = (
    "We're a 12-person marketing agency. "
    "We're losing track of customer follow-ups, "
    "our process is manual and time-consuming, "
    "we're worried about cost, and we're comparing "
    "other vendors."
)


def test_app_opens_without_errors():
    app = AppTest.from_file("app.py").run()

    assert not app.exception


def test_empty_inquiry_shows_warning():
    app = AppTest.from_file("app.py").run()

    app.button[0].click().run()

    assert len(app.warning) > 0


def test_customer_inquiry_generates_a_draft():
    app = AppTest.from_file("app.py").run()

    app.text_area[0].set_value(SAMPLE_INQUIRY)
    app.button[0].click().run()

    assert not app.exception
    assert len(app.text_area) >= 2
    assert "Hi there" in app.text_area[-1].value


def test_draft_references_customer_concerns():
    app = AppTest.from_file("app.py").run()

    app.text_area[0].set_value(SAMPLE_INQUIRY)
    app.button[0].click().run()

    draft = app.text_area[-1].value.lower()

    assert "follow-up" in draft or "follow up" in draft
    assert "cost" in draft or "budget" in draft
    assert "alternative solutions" in draft


def test_friendly_tone():
    app = AppTest.from_file("app.py").run()

    app.selectbox[0].select(
        "Friendly and professional"
    ).run()

    app.text_area[0].set_value(SAMPLE_INQUIRY)
    app.button[0].click().run()

    draft = app.text_area[-1].value

    assert "Thanks for sharing a little about your team." in draft


def test_concise_tone():
    app = AppTest.from_file("app.py").run()

    app.selectbox[0].select("Concise").run()

    app.text_area[0].set_value(SAMPLE_INQUIRY)
    app.button[0].click().run()

    draft = app.text_area[-1].value

    assert "Thanks for sharing your situation." in draft


def test_consultative_tone():
    app = AppTest.from_file("app.py").run()

    app.selectbox[0].select("Consultative").run()

    app.text_area[0].set_value(SAMPLE_INQUIRY)
    app.button[0].click().run()

    draft = app.text_area[-1].value

    assert "discovery call" in draft.lower()
    assert "successful outcome" in draft.lower()


def test_inquiry_without_known_keywords_uses_fallback():
    app = AppTest.from_file("app.py").run()

    app.text_area[0].set_value(
        "Hello, I would like to learn more about your services."
    )
    app.button[0].click().run()

    draft = app.text_area[-1].value.lower()

    assert not app.exception
    assert "current process and priorities" in draft


def test_competitor_inquiry_gets_relevant_follow_up():
    app = AppTest.from_file("app.py").run()

    app.text_area[0].set_value(
        "We are evaluating an alternative and would like to compare options."
    )
    app.button[0].click().run()

    draft = app.text_area[-1].value.lower()

    assert "alternative solutions" in draft
    assert "criteria matter most" in draft


def test_email_edits_persist_and_analysis_remains_visible():
    app = AppTest.from_file("app.py").run()

    # Enter a customer inquiry and analyze it.
    app.text_area[0].set_value(SAMPLE_INQUIRY)
    app.button[0].click().run()

    # Confirm the email draft is displayed.
    assert not app.exception
    assert len(app.text_area) >= 2

    # Edit the email as a user would.
    edited_draft = (
        app.text_area[1].value
        + "\nI will follow up with you next Tuesday."
    )

    app.text_area[1].set_value(edited_draft).run()

    # Confirm the edit survives the Streamlit rerun.
    assert not app.exception
    assert (
        "I will follow up with you next Tuesday."
        in app.text_area[1].value
    )

    # Confirm the original analysis is still displayed.
    assert any(
        "1. Customer summary" in heading.value
        for heading in app.subheader
    )
