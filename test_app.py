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