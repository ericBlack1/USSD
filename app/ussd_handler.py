from fastapi import Request
from fastapi.responses import PlainTextResponse

def handle_ussd(session_id, phone_number, text):
    # Split the input text by "*" to understand menu progression
    user_response = text.split("*")
    menu_level = len(user_response)

    if text == "":
        # Initial menu
        response = "CON Welcome to TrafficAZ 🚦\n"
        response += "1. Report Traffic\n"
        response += "2. View Traffic Alerts\n"
        response += "3. Exit"
    elif text == "1":
        response = "CON Select Severity:\n1. Heavy\n2. Moderate\n3. Light"
    elif text.startswith("1*"):
        severity = user_response[1]
        if severity in ["1", "2", "3"]:
            response = "END 🚧 Thank you! Traffic report submitted."
        else:
            response = "END ❌ Invalid severity option."
    elif text == "2":
        response = "END 📍 Current Alerts:\n- Bonaberi: Heavy\n- Carrefour Total: Moderate"
    elif text == "3":
        response = "END Thank you for using TrafficAZ!"
    else:
        response = "END ❌ Invalid input. Try again."

    return response

