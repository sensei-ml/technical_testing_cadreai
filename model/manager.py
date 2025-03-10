import os
from typing import Dict, List, Optional
from dotenv import load_dotenv
from openai import OpenAI
import logging
from datetime import datetime
import pandas as pd

class EmailProcessor:
    def __init__(self):
        """Initialize the email processor with OpenAI API key."""
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Define valid categories
        self.valid_categories = {
            "complaint", "inquiry", "feedback",
            "support_request", "other"
        }

    def classify_email(self, email: Dict) -> Optional[str]:
        """
        Classify an email using LLM.
        Returns the classification category or None if classification fails.
        """
        if not email.get("subject") or not email.get("body"):
            logging.error("Email subject or body is missing.")
            return None

        try:
            input_prompt = f'''Classify: {email["subject"]}; {email["body"]} 
                            Categories: {", ".join(self.valid_categories)}
                            Just the category name, if it's "other" return that'''
            response = self.client.chat.completions.create(
                model='gpt-4o-mini-2024-07-18',
                messages=[{'role': 'user', 'content': input_prompt}],
                temperature=0.1,
                stream=False
            )
            answer = response.choices[0].message.content
            return answer
        except Exception as e:
            logging.error(f"Error classifying email: {e}")
            return None

    def generate_response(self, email: Dict, classification: str) -> Optional[str]:
        """
        Generate an automated response based on email classification.
        """
        if not email.get("subject") or not email.get("body"):
            logging.error("Email subject or body is missing.")
            return None

        try:
            output_prompt = f'Write short response for an email: {email["subject"]}; {email["body"]} Category: {classification}'
            response_classification = self.client.chat.completions.create(
                model='gpt-4o-mini-2024-07-18',
                messages=[{'role': 'user', 'content': classification}],
                temperature=0.1,
                stream=False
            )
            automated_response = response_classification.choices[0].message.content
            return automated_response
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return None


class EmailAutomationSystem:
    def __init__(self, processor: EmailProcessor):
        """Initialize the automation system with an EmailProcessor."""
        self.processor = processor
        self.response_handlers = {
            "complaint": self._handle_complaint,
            "inquiry": self._handle_inquiry,
            "feedback": self._handle_feedback,
            "support_request": self._handle_support_request,
            "other": self._handle_other
        }
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def process_email(self, email: Dict) -> Dict:
        """
        Process a single email through the complete pipeline.
        Returns a dictionary with the processing results.
        """
        if not email.get("subject") or not email.get("body"):
            self.logger.error("Email subject or body is missing.")
            return {"error": "Email subject or body is missing.", "email": email}

        try:
            classification = self.processor.classify_email(email)
            response = self.processor.generate_response(email, classification)
            processed_email = {
                "classification": classification,
                "email": email,
                "response": response
            }

            # Handle the email based on its classification
            if classification in self.response_handlers:
                self.response_handlers[classification](email)

            return processed_email
        except Exception as e:
            self.logger.error(f"Error processing email {email['id']}: {e}")
            return {"error": str(e), "email": email}

    def _handle_complaint(self, email: Dict):
        """Handle complaint emails."""
        try:
            response = self.processor.generate_response(email, "complaint")
            self.send_complaint_response(email["id"], response)
            self.create_urgent_ticket(email["id"], "complaint", email["body"])
        except Exception as e:
            self.logger.error(f"Error handling complaint email {email['id']}: {e}")

    def _handle_inquiry(self, email: Dict):
        """Handle inquiry emails."""
        try:
            response = self.processor.generate_response(email, "inquiry")
            self.send_standard_response(email["id"], response)
        except Exception as e:
            self.logger.error(f"Error handling inquiry email {email['id']}: {e}")

    def _handle_feedback(self, email: Dict):
        """Handle feedback emails."""
        try:
            response = self.processor.generate_response(email, "feedback")
            self.log_customer_feedback(email["id"], email["body"])
        except Exception as e:
            self.logger.error(f"Error handling feedback email {email['id']}: {e}")

    def _handle_support_request(self, email: Dict):
        """Handle support request emails."""
        try:
            response = self.processor.generate_response(email, "support_request")
            self.create_support_ticket(email["id"], email["body"])
        except Exception as e:
            self.logger.error(f"Error handling support request email {email['id']}: {e}")

    def _handle_other(self, email: Dict):
        """Handle other category emails."""
        try:
            response = self.processor.generate_response(email, "other")
            self.send_standard_response(email["id"], response)
        except Exception as e:
            self.logger.error(f"Error handling other email {email['id']}: {e}")

    def send_complaint_response(self, email_id: str, response: str):
        """Mock function to simulate sending a response to a complaint."""
        try:
            self.logger.info(f"Sending complaint response for email {email_id}")
            # In real implementation: integrate with email service
        except Exception as e:
            self.logger.error(f"Error sending complaint response for email {email_id}: {e}")

    def send_standard_response(self, email_id: str, response: str):
        """Mock function to simulate sending a standard response."""
        try:
            self.logger.info(f"Sending standard response for email {email_id}")
            # In real implementation: integrate with email service
        except Exception as e:
            self.logger.error(f"Error sending standard response for email {email_id}: {e}")

    def create_urgent_ticket(self, email_id: str, category: str, context: str):
        """Mock function to simulate creating an urgent ticket."""
        try:
            self.logger.info(f"Creating urgent ticket for email {email_id}")
            # In real implementation: integrate with ticket system
        except Exception as e:
            self.logger.error(f"Error creating urgent ticket for email {email_id}: {e}")

    def create_support_ticket(self, email_id: str, context: str):
        """Mock function to simulate creating a support ticket."""
        try:
            self.logger.info(f"Creating support ticket for email {email_id}")
            # In real implementation: integrate with ticket system
        except Exception as e:
            self.logger.error(f"Error creating support ticket for email {email_id}: {e}")

    def log_customer_feedback(self, email_id: str, feedback: str):
        """Mock function to simulate logging customer feedback."""
        try:
            self.logger.info(f"Logging feedback for email {email_id}")
            # In real implementation: integrate with feedback system
        except Exception as e:
            self.logger.error(f"Error logging feedback for email {email_id}: {e}")

    def process_all_emails(self, emails: List[Dict]) -> pd.DataFrame:
        """
        Process all emails in the provided list.
        Returns a DataFrame with the processing results.
        """
        results = []
        for email in emails.to_dict(orient="records"):
            if not email.get('subject') or not email.get('body'):
                self.logger.error(f"Email {email.get('id', 'unknown')} is missing subject or body. Skipping...")
                continue

            start_time = datetime.now()
            self.logger.info(f"Processing email {email['id']}...")
            result = self.process_email(email)
            end_time = datetime.now()
            processing_time = (end_time - start_time).total_seconds()
            self.logger.info(f"Processed email {email['id']} in {processing_time} seconds")
            result['processing_time'] = processing_time
            results.append(result)

        report = pd.DataFrame(results)
        report.to_csv('report/report.csv', index=False)
        return report