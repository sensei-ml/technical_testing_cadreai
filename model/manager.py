import os
from typing import Dict, Optional
from dotenv import load_dotenv
from openai import OpenAI
import logging

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
        
        TODO: 
        1. Design and implement the classification prompt
        2. Make the API call with appropriate error handling
        3. Validate and return the classification
        """
        self.input_prompt = f'''Classify: {email["subject"]}; {email["body"]} 
                                Categories: {", ".join(self.valid_categories)}
                                category'''
            
        self.response = self.client.chat.completions.create(
            model='gpt-4o-mini-2024-07-18',
            messages=[{'role': 'user', 'content': self.input_prompt},],
            temperature=0.1,
            stream=False
        )
        self.anwser = self.response.choices[0].message.content
        return self.anwser

    def generate_response(self, email: Dict, classification: str) -> Optional[str]:
        """
        Generate an automated response based on email classification.
        
        TODO:
        1. Design the response generation prompt
        2. Implement appropriate response templates
        3. Add error handling
        """
        self.output_prompt = f'Write short response for: {email["subject"]}; {email["body"]} Category: {classification}'
        self.response_classification = self.client.chat.completions.create(
            model='gpt-4o-mini-2024-07-18',
            messages=[{'role': 'user', 'content': classification},],
            temperature=0.1,
            stream=False
        )
        self.automated_response = self.response_classification.choices[0].message.content
        return self.automated_response

        


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

    def process_email(self, email: Dict) -> Dict:
        """
        Process a single email through the complete pipeline.
        Returns a dictionary with the processing results.
        
        TODO:
        1. Implement the complete processing pipeline
        2. Add appropriate error handling
        3. Return processing results
        """
        self.classification = self.processor.classify_email(email)
        self.response = self.processor.generate_response(email, self.classification)
        self.processed_email = {
            "classification": self.classification,
            "email": email,
            "response": self.response
        }
        return self.processed_email

    def _handle_complaint(self, email: Dict):
        """
        Handle complaint emails.
        TODO: Implement complaint handling logic
        """
        response = self.processor.generate_response(email, "complaint")
        send_complaint_response(email["id"], response)
        create_urgent_ticket(email["id"], "complaint", email["body"])

    def _handle_inquiry(self, email: Dict):
        """
        Handle inquiry emails.
        TODO: Implement inquiry handling logic
        """
        response = self.processor.generate_response(email, "inquiry")
        send_standard_response(email["id"], response)

    def _handle_feedback(self, email: Dict):
        """
        Handle feedback emails.
        TODO: Implement feedback handling logic
        """
        response = self.processor.generate_response(email, "feedback")
        log_customer_feedback(email["id"], email["body"])

    def _handle_support_request(self, email: Dict):
        """
        Handle support request emails.
        TODO: Implement support request handling logic
        """
        response = self.processor.generate_response(email, "support_request")
        create_support_ticket(email["id"], email["body"])

    def _handle_other(self, email: Dict):
        """
        Handle other category emails.
        TODO: Implement handling logic for other categories
        """
        

class MockService():
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.email_processor = EmailProcessor()
        self.automation_system = EmailAutomationSystem(self.email_processor)

    def send_complaint_response(self, email_id: str, response: str):
        """Mock function to simulate sending a response to a complaint"""
        self.logger.info(f"Sending complaint response for email {email_id}")
        # In real implementation: integrate with email service


    def send_standard_response(self, email_id: str, response: str):
        """Mock function to simulate sending a standard response"""
        self.logger.info(f"Sending standard response for email {email_id}")
        # In real implementation: integrate with email service


    def create_urgent_ticket(self, email_id: str, category: str, context: str):
        """Mock function to simulate creating an urgent ticket"""
        self.logger.info(f"Creating urgent ticket for email {email_id}")
        # In real implementation: integrate with ticket system


    def create_support_ticket(self, email_id: str, context: str):
        """Mock function to simulate creating a support ticket"""
        self.logger.info(f"Creating support ticket for email {email_id}")
        # In real implementation: integrate with ticket system


    def log_customer_feedback(self, email_id: str, feedback: str):
        """Mock function to simulate logging customer feedback"""
        self.logger.info(f"Logging feedback for email {email_id}")
        # In real implementation: integrate with feedback system