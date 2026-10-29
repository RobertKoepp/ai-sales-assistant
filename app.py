
import streamlit as st

st.set_page_config(
    page_title="AI Sales Assistant",
    page_icon="💬",
)

st.title("💬 AI Sales Assistant")
st.caption("Free sales enablement portfolio prototype")

st.info(
    "Prototype mode: uses Python rules and templates, "
    "not a live AI model. No API key or paid service required."
)

inquiry = st.text_area(
    "Customer inquiry",
    height=160,
    placeholder=(
        "Example: We're a 12-person agency. We keep missing "
        "customer follow-ups, and we're concerned about price."
    ),
)

tone = st.selectbox(
    "Follow-up tone",
    ["Friendly and professional", "Concise", "Consultative"],
)

if st.button("Analyze inquiry", type="primary"):
    if not inquiry.strip():
        st.warning("Please enter a customer inquiry.")
    else:
        text = inquiry.lower()

        # Identify potential customer pain points.
        pain_points = []

        if any(word in text for word in [
            "follow-up", "follow up", "missed", "losing track"
        ]):
            pain_points.append("Tracking customer follow-ups")

        if any(word in text for word in [
            "manual", "slow", "inefficient", "time-consuming"
        ]):
            pain_points.append("Possible workflow inefficiency")

        # Identify potential objections.
        objections = []

        if any(word in text for word in [
            "expensive", "price", "cost", "budget", "afford"
        ]):
            objections.append("Possible price or budget concern")

        if any(word in text for word in [
            "competitor", "alternative", "other vendor"
        ]):
            objections.append("Comparing alternative solutions")

        # 1. Customer summary
        st.subheader("1. Customer summary")

        if pain_points:
            for item in pain_points:
                st.write(f"- Potential pain point: {item}")
        else:
            st.write("No predefined pain-point keywords detected.")

        if objections:
            for item in objections:
                st.write(f"- Potential objection: {item}")
        else:
            st.write("No predefined objection keywords detected.")

        st.caption(
            "These findings are based on keyword matching, "
            "not AI understanding. Review them manually."
        )

        # 2. Recommend a next step.
        st.subheader("2. Recommended next step")

        if "Possible price or budget concern" in objections:
            st.write(
                "Acknowledge the concern and ask how the customer "
                "evaluates cost. Don't offer an unauthorized discount."
            )
        elif pain_points:
            st.write(
                "Ask how the customer handles the process today "
                "and what they want to improve."
            )
        else:
            st.write(
                "Ask a discovery question to clarify the customer's "
                "main goal and current process."
            )

        st.write("**Suggested discovery questions**")
        st.write("- How do you handle this process today?")
        st.write("- What would you most like to improve?")
        st.write("- What criteria matter most when choosing a solution?")

        # 3. Create a personalized follow-up email.
        st.subheader("3. Follow-up draft")

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

        # 4. Human review checklist.
        st.subheader("4. Human review")

        st.write("- Verify product claims, pricing, and policies.")
        st.write("- Check that the message reflects the customer's needs.")
        st.write("- Review the message before sending.")

        st.success(
            "Analysis complete. Review the output before using it."
        )
