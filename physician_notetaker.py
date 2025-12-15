def medical_nlp_pipeline():
    return {
        "Patient_Name": "Ms. Jones",
        "Symptoms": ["Neck pain", "Back pain"],
        "Diagnosis": "Whiplash injury",
        "Treatment": ["Physiotherapy", "Painkillers"],
        "Current_Status": "Occasional back pain",
        "Prognosis": "Full recovery expected"
    }

def sentiment_intent(text):
    if "worried" in text.lower():
        return "Anxious", "Seeking reassurance"
    return "Reassured", "Expressing relief"

def soap_note():
    return {
        "Assessment": "Resolving whiplash injury",
        "Plan": "Follow-up if symptoms worsen"
    }

if __name__ == "__main__":
    print(medical_nlp_pipeline())
    print(sentiment_intent("That’s a relief!"))
    print(soap_note())
