from fastapi import Request
from typing import Dict
from fastapi.responses import PlainTextResponse

def handle_ussd(form_data: dict) -> PlainTextResponse:
    session_id = form_data.get("sessionId", "")
    service_code = form_data.get("serviceCode", "")
    phone_number = form_data.get("phoneNumber", "")
    text = form_data.get("text", "").strip()

    # Split text by * to determine menu depth
    user_responses = text.split("*") if text else []

    if not user_responses or user_responses[0] == "":
        return PlainTextResponse(
            content=(
                "CON Welcome to TrafficAZ 🚦\n"
                "1. Report Traffic\n"
                "2. View Alerts\n"
                "3. Exit"
            )
        )

    first_choice = user_responses[0]

    if first_choice == "1":
        # User chose to report traffic
        if len(user_responses) == 1:
            return PlainTextResponse(
                content="CON Select severity:\n1. Light\n2. Moderate\n3. Heavy"
            )
        elif len(user_responses) == 2:
            severity_input = user_responses[1]
            severity_map = {"1": "Light", "2": "Moderate", "3": "Heavy"}
            severity_text = severity_map.get(severity_input)

            if severity_text:
                # TODO: Store report in DB or forward to service here
                return PlainTextResponse(
                    content=f"END ✅ Traffic report ({severity_text}) submitted. Thank you!"
                )
            else:
                return PlainTextResponse(content="END ❌ Invalid severity option.")

        else:
            return PlainTextResponse(content="END ❌ Invalid input. Please try again.")

    elif first_choice == "2":
        # Stubbed traffic alerts
        return PlainTextResponse(
            content=(
                "END 🚧 Current Alerts:\n"
                "- Yaounde: Heavy at Mvan\n"
                "- Douala: Moderate at Bonamoussadi"
            )
        )

    elif first_choice == "3":
        return PlainTextResponse(content="END 👋 Goodbye!")

    else:
        return PlainTextResponse(content="END ❌ Invalid selection. Try again.")

