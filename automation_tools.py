import json
import requests
from datetime import datetime

class BusinessAutomator:
    """
    A core toolkit for handling business automation workflows,
    processing webhooks, and interacting with external APIs.
    """
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def process_webhook_data(self, payload):
        """
        Parses incoming webhook data (e.g., from Tally, Make, or custom webhooks),
        validates fields, and prepares it for CRM or DB insertion.
        """
        try:
            data = json.loads(payload) if isinstance(payload, str) else payload
            
            # Extract core fields safely
            lead_name = data.get("name", "Unknown Lead")
            lead_email = data.get("email", "No Email Provided")
            source = data.get("source", "Direct Webhook")
            
            processed_lead = {
                "status": "success",
                "processed_at": self.timestamp,
                "lead_info": {
                    "name": lead_name,
                    "email": lead_email,
                    "source": source
                }
            }
            return processed_lead
        except Exception as e:
            return {"status": "error", "message": str(e), "timestamp": self.timestamp}

    def send_to_crm(self, endpoint_url, processed_data):
        """
        Simulates sending structured data to a CRM platform or external web service.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}" if self.api_key else ""
        }
        
        print(f"[{self.timestamp}] Initiating API request to: {endpoint_url}")
        # In production, this would execute: requests.post(endpoint_url, json=processed_data, headers=headers)
        return {"status_code": 200, "message": "Payload delivered successfully to the pipeline."}

# Example of local script validation
if __name__ == "__main__":
    automator = BusinessAutomator(api_key="mock_api_token_12345")
    
    # Simulating a webhook structure coming from an automated form
    sample_webhook = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "source": "Smart Lead Form"
    }
    
    result = automator.process_webhook_data(sample_webhook)
    print("Processed Webhook Result:", json.dumps(result, indent=4))
