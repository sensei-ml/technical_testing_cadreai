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
        input_prompt = f'''Classify: {email["subject"]}; {email["body"]} 
                           Categories: {", ".join(self.valid_categories)}
                           category'''
        response = self.client.chat.completions.create(
            model='gpt-4o-mini-2024-07-18',
            messages=[{'role': 'user', 'content': input_prompt}],
            temperature=0.1,
            stream=False
        )
        answer = response.choices[0].message.content
        return answer

    def generate_response(self, email: Dict, classification: str) -> Optional[str]:
        """
        Generate an automated response based on email classification.
        """
        output_prompt = f'Write short response for: {email["subject"]}; {email["body"]} Category: {classification}'
        response_classification = self.client.chat.completions.create(
            model='gpt-4o-mini-2024-07-18',
            messages=[{'role': 'user', 'content': classification}],
            temperature=0.1,
            stream=False
        )
        automated_response = response_classification.choices[0].message.content
        return automated_response


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

    def _handle_complaint(self, email: Dict):
        """Handle complaint emails."""
        response = self.processor.generate_response(email, "complaint")
        self.send_complaint_response(email["id"], response)
        self.create_urgent_ticket(email["id"], "complaint", email["body"])

    def _handle_inquiry(self, email: Dict):
        """Handle inquiry emails."""
        response = self.processor.generate_response(email, "inquiry")
        self.send_standard_response(email["id"], response)

    def _handle_feedback(self, email: Dict):
        """Handle feedback emails."""
        response = self.processor.generate_response(email, "feedback")
        self.log_customer_feedback(email["id"], email["body"])

    def _handle_support_request(self, email: Dict):
        """Handle support request emails."""
        response = self.processor.generate_response(email, "support_request")
        self.create_support_ticket(email["id"], email["body"])

    def _handle_other(self, email: Dict):
        """Handle other category emails."""
        response = self.processor.generate_response(email, "other")
        self.send_standard_response(email["id"], response)

    def send_complaint_response(self, email_id: str, response: str):
        """Mock function to simulate sending a response to a complaint."""
        self.logger.info(f"Sending complaint response for email {email_id}")
        # In real implementation: integrate with email service

    def send_standard_response(self, email_id: str, response: str):
        """Mock function to simulate sending a standard response."""
        self.logger.info(f"Sending standard response for email {email_id}")
        # In real implementation: integrate with email service

    def create_urgent_ticket(self, email_id: str, category: str, context: str):
        """Mock function to simulate creating an urgent ticket."""
        self.logger.info(f"Creating urgent ticket for email {email_id}")
        # In real implementation: integrate with ticket system

    def create_support_ticket(self, email_id: str, context: str):
        """Mock function to simulate creating a support ticket."""
        self.logger.info(f"Creating support ticket for email {email_id}")
        # In real implementation: integrate with ticket system

    def log_customer_feedback(self, email_id: str, feedback: str):
        """Mock function to simulate logging customer feedback."""
        self.logger.info(f"Logging feedback for email {email_id}")
        # In real implementation: integrate with feedback system

    def process_all_emails(self, emails: List[Dict]) -> pd.DataFrame:
        """
        Process all emails in the provided list.
        Returns a DataFrame with the processing results.
        """
        results = []
        for email in emails.to_dict(orient="records"):
            start_time = datetime.now()
            self.logger.info(f"Processing email {email['id']}...")
            result = self.process_email(email)
            end_time = datetime.now()
            processing_time = (end_time - start_time).total_seconds()
            self.logger.info(f"Processed email {email['id']} in {processing_time} seconds")
            result['processing_time'] = processing_time
            results.append(result)
            report = pd.DataFrame(results)
            report.to_csv('llm-email-classifier-test/report/report.csv', index=False)
        return report