def generate_visa_roadmap(visa_data):
    """
    Generates a step-by-step visa application roadmap
    based on common visa application phases.
    """

    roadmap = [
        {
            "phase": "Document Preparation",
            "timeline": "Day 1–7",
            "risk": "Missing or incorrect documents"
        },
        {
            "phase": "Application Submission",
            "timeline": "Day 7–10",
            "risk": "Incorrect form details"
        },
        {
            "phase": "Biometrics / Interview",
            "timeline": "Week 2–3",
            "risk": "Unclear travel or study intent"
        },
        {
            "phase": "Application Processing",
            "timeline": visa_data.get("processing_time", "Varies"),
            "risk": "Background or financial verification issues"
        },
        {
            "phase": "Decision",
            "timeline": "Final step",
            "risk": "Visa refusal"
        }
    ]

    return roadmap


def display_visa_roadmap(roadmap):
    print("\n🧭 Visa Application Roadmap\n")

    for step in roadmap:
        print(f"📌 {step['phase']}")
        print(f"   ⏱ Timeline: {step['timeline']}")
        print(f"   ⚠️ Risk: {step['risk']}\n")
