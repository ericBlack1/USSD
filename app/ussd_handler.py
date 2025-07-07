from fastapi import Request
from fastapi.responses import PlainTextResponse
from typing import Dict

def handle_ussd(form_data: Dict[str, str]) -> str:
    session_id = form_data.get("sessionId")
    service_code = form_data.get("serviceCode")
    phone_number = form_data.get("phoneNumber")
    text = form_data.get("text", "").strip()

    parts = text.split("*") if text else []

    if len(parts) == 0 or parts[0] == "":
        response = "CON Welcome to TrafficAZ\n"
        response += "1. Check Traffic\n"
        response += "2. Report Traffic\n"
        response += "3. Emergency Alert"
        return response

    elif parts[0] == "1":
        # Check Traffic
        if len(parts) == 1:
            return "CON Enter area name (e.g. Melen):"
        elif len(parts) == 2:
            area = parts[1]
            return f"CON You entered '{area}'. Are you sure? (yes/no)"
        elif len(parts) == 3:
            if parts[2].lower() == "yes":
                # Simulated response
                return "END Traffic in your area is heavy. Use Omnisport road as an alternative."
            else:
                return "END Request cancelled. Dial again to check traffic."

    elif parts[0] == "2":
        # Report Traffic
        if len(parts) == 1:
            return "CON Enter area of congestion:"
        elif len(parts) == 2:
            area = parts[1]
            return f"CON You entered '{area}'. Are you sure? (yes/no)"
        elif len(parts) == 3:
            if parts[2].lower() == "yes":
                # Simulated saving
                return "END Thank you! You've reported traffic at that location."
            else:
                return "END Report cancelled. Dial again to report."

    elif parts[0] == "3":
        return "END Emergency alert received. Authorities will be notified immediately."

    else:
        return "END Invalid input. Please try again."

