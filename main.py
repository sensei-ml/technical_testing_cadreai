from utils.process_data import emails_to_dataframe
from model.manager import EmailAutomationSystem, EmailProcessor

def run():
    sample_emails = [
        {
            "id": "001",
            "from": "angry.customer@example.com",
            "subject": "Broken product received",
            "body": "I received my order #12345 yesterday but it arrived completely damaged. This is unacceptable and I demand a refund immediately. This is the worst customer service I've experienced.",
            "timestamp": "2024-03-15T10:30:00Z"
        },
        {
            "id": "002",
            "from": "curious.shopper@example.com",
            "subject": "Question about product specifications",
            "body": "Hi, I'm interested in buying your premium package but I couldn't find information about whether it's compatible with Mac OS. Could you please clarify this? Thanks!",
            "timestamp": "2024-03-15T11:45:00Z"
        },
        {
            "id": "003",
            "from": "happy.user@example.com",
            "subject": "Amazing customer support",
            "body": "I just wanted to say thank you for the excellent support I received from Sarah on your team. She went above and beyond to help resolve my issue. Keep up the great work!",
            "timestamp": "2024-03-15T13:15:00Z"
        },
        {
            "id": "004",
            "from": "tech.user@example.com",
            "subject": "Need help with installation",
            "body": "I've been trying to install the software for the past hour but keep getting error code 5123. I've already tried restarting my computer and clearing the cache. Please help!",
            "timestamp": "2024-03-15T14:20:00Z"
        },
        {
            "id": "005",
            "from": "business.client@example.com",
            "subject": "Partnership opportunity",
            "body": "Our company is interested in exploring potential partnership opportunities with your organization. Would it be possible to schedule a call next week to discuss this further?",
            "timestamp": "2024-03-15T15:00:00Z"
        }
    ]
    data = emails_to_dataframe(emails = sample_emails, columns_to_preprocess = ['subject', 'body'])
    print(data)

if __name__ == '__main__':
    run()
