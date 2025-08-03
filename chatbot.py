
import random

responses = {
    "admission": "Admissions open from June to August.",
    "courses": "We offer B.Tech, B.Sc, and M.Tech programs.",
    "fees": "The annual fees range from ₹50,000 to ₹1,20,000.",
    "hostel": "Yes, we have separate hostels for boys and girls."
}

print("College Enquiry Chatbot. Type 'exit' to quit.")

while True:
    query = input("Ask a question: ").lower()
    if "exit" in query:
        print("Goodbye!")
        break
    found = False
    for key in responses:
        if key in query:
            print("Bot:", responses[key])
            found = True
            break
    if not found:
        print("Bot: Sorry, I don't understand.")
