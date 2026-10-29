
import streamlit as st

st.set_page_config(
    page_title="AI Sales Assistant",
    page_icon="💬",
    layout="centered",
)

st.title("💬 AI Sales Assistant")
st.caption("A sales enablement portfolio prototype")

st.info(
    "Prototype mode: this version uses Python rules and templates. "
    "It does not call an AI model or send customer messages."
)

st.markdown(
    "Analyze a customer inquiry, identify potential objections, "
    "and generate a follow-up draft."
)

inquiry = st.text_area(
    "Customer inquiry",
    height=180,
    placeholder=(
        "Example: We're a 12-person agency and keep missing "
        "customer follow-ups. We're interested, but worried "
        "about the price."
    ),
)

tone = st.selectbox(
    "Response tone",
    ["Friendly and professional", "Concise", "Consultative"],
)

if st.button("Analyze inquiry", type="primary"):
    if not inquiry.strip():
        st.warning("Enter a customer inquiry first.")
    else:
        text = inquiry.lower()

        # Simple keyword-based rules, not AI reasoning.
        pain_points = []
        if any(word in text for word in [
            "follow-up", "follow up", "missed", "losing track"
        ]):
            pain_points.append("Tracking customer follow-ups")

        if any(word in text for word in [
            "time-consuming", "manual", "slow", "inefficient"
        ]):
            pain_points.append("Potential workflow inefficiency")

        objections = []
        if any(word in text for word in [
            "expensive", "price", "cost", "budget", "afford"
        ]):
            objections.append("Price or budget concern")

        if any(word in text for word in [
            "competitor", "alternative", "other vendor"
        ]):
            objections.append("Comparing alternatives")

        if any(word in text for word in [
            "not sure", "unsure", "concerned", "worried", "risk"
        ]):
            objections.append("Uncertainty or perceived risk")

        st.subheader("1. Customer summary")

        if pain_points:
            st.write("**Potential pain points**")
            for point in pain_points:
                st.write(f"- {point}")
        else:
            st.write(
                "- No predefined pain-point keywords detected. "
                "Review the inquiry manually."
            )

        if objections:
            st.write("**Potential objections**")
            for objection in objections:
                st.write(f"- {objection}")
        else:
            st.write(
                "**Potential objections:** None detected by the "
                "current keyword rules."
            )

        st.write(
            "**Important:** These are keyword-based suggestions, "
            "not a verified interpretation of the customer's intent."
        )

        st.subheader("2. Recommended next step")

        if "Price or budget concern" in objections:
            st.write(
                "Acknowledge the budget concern and ask what "
                "criteria the customer is using to evaluate cost. "
                "Do not offer an unapproved discount."
            )
        elif pain_points:
            st.write(
                "Ask how the customer handles this process today "
                "and what a successful improvement would look like."
            )
        else:
            st.write(
                "Ask a discovery question to clarify the customer's "
                "main goal, current process, and desired outcome."
            )

        st.write("**Suggested discovery questions**")
        st.write("- How are you handling this process today?")
        st.write("- What would you most like to improve?")
        st.write("- What criteria will help you evaluate a solution?")


        st.subheader("3. Follow-up draft")

        # Personalize the draft using detected customer concerns.
        topics = []

        if pain_points:
            topics.append(pain_points[0].lower())

        if "Possible price or budget concern" in objections:
            topics.append("cost and budget")

        if "Comparing alternative solutions" in objections:
            topics.append("comparing alternative solutions")

        if topics:
            context_sentence = (
                "You mentioned " + ", ".join(topics) + "."
            )
        else:
            context_sentence = (
                "I'd like to learn more about your current process "
                "and priorities."
            )

        if "Possible price or budget concern" in objections:
            objection_sentence = (
                "We can discuss the outcomes and budget criteria "
                "that matter most to your team."
            )
        elif "Comparing alternative solutions" in objections:
            objection_sentence = (
                "I'd be interested to learn which criteria matter "
                "most as you compare options."
            )
        else:
            objection_sentence = ""

        if tone == "Concise":
            greeting = "Thanks for sharing your situation."
            body = (
                f"{context_sentence} {objection_sentence} "
                "Would you be open to a short conversation next week?"
            )

        elif tone == "Consultative":
            greeting = (
                "Thanks for explaining your team's current challenges."
            )
            body = (
                f"{context_sentence} {objection_sentence} "
                "Before recommending a solution, I'd like to understand "
                "your current process and what a successful outcome "
                "would look like. Would you be available for a short "
                "discovery call?"
            )

        else:
            greeting = (
                "Thanks for sharing a little about your team."
            )
            body = (
                f"{context_sentence} {objection_sentence} "
                "I'd be happy to learn more and see whether we might "
                "be a fit. Would you be open to a short conversation "
                "next week?"
            )

        draft = f"Hi there,\n\n{greeting} {body}\n\nBest,"

        st.text_area(
            "Edit your follow-up",
            value=draft,
            height=220,
        )


        st.subheader("4. Human review")

        st.write(
            "- Verify product features, pricing, and company policies."
        )
        st.write(
            "- Confirm the draft reflects the customer's actual needs."
        )
        st.write(
            "- Review the response before sending it."
        )

        st.caption(
            "Prototype limitation: keyword rules can miss context, "
            "misread intent, or generate generic recommendations. "
            "No live AI model is used."
        )
