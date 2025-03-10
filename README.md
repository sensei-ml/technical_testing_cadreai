# LLM Email Classifier

## Overview

The LLM Email Classifier is a system designed to classify and respond to emails using a language model. It processes emails, classifies them into predefined categories, and generates automated responses based on the classification.


## Files and Directories

- **data/**: Directory containing email data in CSV format.
  - **emails.csv**: Given data saved in .csv file.
  - **text_emails.csv**: Additional sample email data.
- **model/**: Directory containing the email processing logic.
  - **manager.py**: Contains the `EmailProcessor` and `EmailAutomationSystem` classes.
- **report/**: Directory containing the processing report.
  - **report.csv**: Report generated after processing emails.
- **utils/**: Directory containing utility functions.
  - **process_data.py**: Functions for processing email data using NLP techniques removing stopwords and lematise the email subject and body.
- **.env**: Contains environment variables, including the OpenAI API key access.
- **llm_api_test.py**: Script to test the OpenAI API.
- **main.py**: Main script to run the email processing demonstration.
- **README.md**: Project documentation
- **prompt_engineering.md**: Documentation on prompt engineering iteration tests and results.
- **requirements.txt**: List of dependencies required for the project.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd llm-email-classifier-test
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY=OPENAI_API_KEY
        ```

## Usage

To run the email processing demonstration, execute the `main.py` 

### Run samples

1. The logs of the provided data.

```
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Downloading NLTK resource: wordnet...
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\mleon\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
2025-03-09 23:16:21,754 - Processing email 1...
2025-03-09 23:16:23,486 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:24,921 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:25,868 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:25,871 - Sending complaint response for email 1
2025-03-09 23:16:25,872 - Creating urgent ticket for email 1
2025-03-09 23:16:25,872 - Processed email 1 in 4.118609 seconds
2025-03-09 23:16:25,873 - Processing email 2...
2025-03-09 23:16:26,157 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:26,869 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:27,550 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:27,551 - Sending standard response for email 2
2025-03-09 23:16:27,551 - Processed email 2 in 1.677954 seconds
2025-03-09 23:16:27,551 - Processing email 3...
2025-03-09 23:16:27,840 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:29,095 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:29,806 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:29,810 - Logging feedback for email 3
2025-03-09 23:16:29,810 - Processed email 3 in 2.259795 seconds
2025-03-09 23:16:29,810 - Processing email 4...
2025-03-09 23:16:30,270 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:31,621 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:32,784 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:32,787 - Creating support ticket for email 4
2025-03-09 23:16:32,787 - Processed email 4 in 2.977058 seconds
2025-03-09 23:16:32,787 - Processing email 5...
2025-03-09 23:16:33,149 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:33,817 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:34,649 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 23:16:34,655 - Sending standard response for email 5
2025-03-09 23:16:34,655 - Processed email 5 in 1.86752 seconds
    classification                                              email                                           response  processing_time
0        complaint  {'id': 1, 'from': 'angry.customer@example.com'...  It seems like you might want to express a comp...         4.118609
1          inquiry  {'id': 2, 'from': 'curious.shopper@example.com...  Of course! What would you like to inquire abou...         1.677954
2         feedback  {'id': 3, 'from': 'happy.user@example.com', 's...  Of course! I’d be happy to help with feedback....         2.259795
3  support_request  {'id': 4, 'from': 'tech.user@example.com', 'su...  It seems like you might need assistance with s...         2.977058
4            other  {'id': 5, 'from': 'business.client@example.com...  It seems like your message is incomplete. Coul...         1.867520
```


2. Logs using new data from the text_emails.csv file.

```
2025-03-09 22:29:36,323 - Processing email 6...
2025-03-09 22:29:37,142 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:38,109 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:38,895 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:38,897 - Creating support ticket for email 6
2025-03-09 22:29:38,897 - Processed email 6 in 2.573179 seconds
2025-03-09 22:29:38,898 - Processing email 7...
2025-03-09 22:29:39,380 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:40,210 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:40,995 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:41,005 - Logging feedback for email 7
2025-03-09 22:29:41,005 - Processed email 7 in 2.107196 seconds
2025-03-09 22:29:41,005 - Processing email 8...
2025-03-09 22:29:41,470 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:42,240 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:43,004 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:43,005 - Sending standard response for email 8
2025-03-09 22:29:43,006 - Processed email 8 in 2.001112 seconds
2025-03-09 22:29:43,007 - Processing email 9...
2025-03-09 22:29:43,352 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:44,092 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:45,026 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:45,028 - Creating support ticket for email 9
2025-03-09 22:29:45,028 - Processed email 9 in 2.020664 seconds
2025-03-09 22:29:45,028 - Processing email 10...
2025-03-09 22:29:45,495 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:46,235 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:46,973 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:46,975 - Sending standard response for email 10
2025-03-09 22:29:46,975 - Processed email 10 in 1.947845 seconds
2025-03-09 22:29:46,977 - Processing email 11...
2025-03-09 22:29:47,344 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:48,150 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:48,945 - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2025-03-09 22:29:48,949 - Sending standard response for email 11
2025-03-09 22:29:48,949 - Processed email 11 in 1.971632 seconds
    classification                                              email                                           response  processing_time
0  support_request  {'id': 6, 'from': 'frustrated.buyer@example.co...  It seems like you might need assistance with s...         2.573179
1         feedback  {'id': 7, 'from': 'loyal.customer@example.com'...  Of course! I’d be happy to         2.107196
2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  Of course! What would you like to inquire abou...         2.001112
3  support_request  {'id': 9, 'from': 'it.support@example.com', 's...  It seems like you might need assistance with s...         2.020664
2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  Of course! What would you like to inquire abou...         2.001112
3  support_request  {'id': 9, 'from': 'it.support@example.com', 's...  It seems like you might need assistance with s...         2.020664
2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  Of course! What would you like to inquire abou...         2.001112        
3  support_request  {'id': 9, 'from': 'it.support@example.com', 's...  It seems like you might need assistance with s...         2.020664        
2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  Of course! What would you like to inquire abou...         2.001112        
3  support_request  {'id': 9, 'from': 'it.support@example.com', 's...  It seems like you might need assistance with s...         2.020664        
2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  Of course! What would you like to inquire abou...         2.001112
3  support_request  {'id': 9, 'from': 'it.support@example.com', 2          inquiry  {'id': 8, 'from': 'gadget.enthusiast@example.c...  Of course! What would you like to inquire abou...         2.001112
 with s...         2.020664
4          inquiry  {'id': 10, 'from': 'event.organizer@example.co...  Of course! What would you like to inquire abou...         1.947845        
 with s...         2.020664
4          inquiry  {'id': 10, 'from': 'event.organizer@example.co...  Of course! What would you like to inquire abou...         1.947845  S C:\Users\mleon\Documents\PERSONAL_GROWING\OPORTUNITIES\TEST FOR CA
 with s...         2.020664
4          inquiry  {'id': 10, 'from': 'event.organizer@example.co...  Of course! What would you like to inquire abou...         1.947845
5            other  {'id': 11, 'from': 'mystery.sender@example.com...  It seems like your message is incomplete. Coul...         1.971632
```