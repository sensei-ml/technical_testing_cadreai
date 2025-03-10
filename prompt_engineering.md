
# Prompt engineering iteration tests

Prompt testing of the system to generate automatic responses.
**Model:** GPT-4o mini.

# Assumptions
1. The email address, and the timestamp are irrelevant at the time of generating the text of the automatic responses. But, they are taken into account if you want to generate a system that takes into account the sender and the time that sends it.
2. This prompt engineering task will be solved taking into account the elementary structure of the prompt: Input, Output, Context and Instruction.
3. The input prompt is generated to classify the according the subject and body, this is how we can define the context of the prompt.
4. The output prompt takes the result of the input prompt and generates the automatic response.

The 4 tests made with the data provided.

## Test 1

**input prompt:** 
Give the direct instruction, the categories context and indicate the final result with the "category" word

```
Classify: {email["subject"]}; {email["body"]} 
Categories: {", ".join(self.valid_categories)}
category
```
**output_prompt:**
Give the instruction and the parameters.

```
Write short response for: {email["subject"]}; {email["body"]} Category: {classification}
```

Results:

| Email id | Classification                  | Reponse    |
|----------|---------------------------------|--------|
| 001      | Category: complaint             | Sure! If you have a specific complaint you'd like to address or need help with, please provide more details, and I'll do my best to assist you. Whether it's about a product, service, or any other issue, I'm here to help!|        
| 002      | Category: inquiry               | It seems like you're interested in making an inquiry. How can I assist you today? Please provide more details or specify the topic you're inquiring about! |        
| 003      | Category: feedback             | Sure! What kind of feedback are you looking for? It could be related to a specific project, a piece of writing, a presentation, or something else entirely. Please provide more details so I can assist you effectively! |         
| 004      | support_request                | It seems like you might need assistance with something specific. Could you please provide more details about your support request? Whether it's technical help, information, or something else, I'm here to help!   |       
| 005      | The appropriate category for the provided text is "inquiry." | Got it! If you have a specific inquiry or question you'd like to ask, feel free to share, and I'll do my best to assist you. |

## Test 2

**input prompt:** 
Give the direct instruction, the categories context, specify to return the final result in a one single word.

```
Classify: {email["subject"]}; {email["body"]} 
Categories: {", ".join(self.valid_categories)}
Just the category name
```
**output prompt:**
Give the instruction and the parameters, add more context about it is an email

```
Write short response for an email: {email["subject"]}; {email["body"]} Category: {classification}
```

Results:

| Email id | Classification                  | Reponse    |
|----------|---------------------------------|--------|
| 001      | complaint        | It seems like you might want to express a complaint or need assistance with a specific issue. Could you please provide more details about what you're experiencing or what you would like to address? This will help me assist you better.|        
| 002      | inquiry          | Of course! What would you like to inquire about? Feel free to ask any question or provide more details on the topic you're interested in. |        
| 003      | feedback         | Of course! What specific feedback are you looking for? It could be about a project, writing, a presentation, or something else. Please provide more details so I can assist you effectively. |         
| 004      | support_request  | It seems like you might need assistance with something specific. Could you please provide more details about your support request? Whether it's technical support, customer service, or something else, I'm here to help! |       
| 005      | inquiry          | Of course! What would you like to inquire about? Feel free to ask any questions or provide more details on the topic you're interested in. |

## Test 3

**input prompt:** 
Give the direct instruction, the categories context, specify to return the final result in a one single word. Add to being estrict and stick to the valid_categories values.

```
Classify: {email["subject"]}; {email["body"]} 
Categories: {", ".join(self.valid_categories)}
Just the category name, strict and stick with the categories
```
**output prompt:**
Add roleplay, act like an automatic response system...

```
Write short response for an email, act like an automatic response system: {email["subject"]}; {email["body"]} Category: {classification}
```

Results (Same results as in test 2):

| Email id | Classification                  | Reponse    |
|----------|---------------------------------|--------|
| 001      | complaint        | It seems like you might want to express a complaint or need assistance with a specific issue. Could you please provide more details about what you're experiencing or what you would like to address? This will help me assist you better.|        
| 002      | inquiry          | Of course! What would you like to inquire about? Feel free to ask any question or provide more details on the topic you're interested in. |        
| 003      | feedback         | Of course! What specific feedback are you looking for? It could be about a project, writing, a presentation, or something else. Please provide more details so I can assist you effectively. |         
| 004      | support_request  | It seems like you might need assistance with something specific. Could you please provide more details about your support request? Whether it's technical support, customer service, or something else, I'm here to help! |       
| 005      | inquiry          | Of course! What would you like to inquire about? Feel free to ask any questions or provide more details on the topic you're interested in. |

## Test 4

**input prompt:** 
Give the direct instruction, the categories context, specify to return the final result in a one single word. Indicate explicitly to don't try to classify the "other" category.

```
Classify: {email["subject"]}; {email["body"]} 
Categories: {", ".join(self.valid_categories)}
Just the category name, if it's "other" return that
```
**output prompt:**
Remove the roleplay is not neccesary.

```
Write short response for an email: {email["subject"]}; {email["body"]} Category: {classification}
```

Results ("Other" Appears in the classification.):

| Email id | Classification                  | Reponse    |
|----------|---------------------------------|--------|
| 001      | complaint        | It seems like you might want to express a complaint or need assistance with a specific issue. Could you please provide more details about what you're experiencing or what you would like to address? This will help me assist you better.|        
| 002      | inquiry          | Of course! What would you like to inquire about? Feel free to ask any question or provide more details on the topic you're interested in. |        
| 003      | feedback         | Of course! What specific feedback are you looking for? It could be about a project, writing, a presentation, or something else. Please provide more details so I can assist you effectively. |         
| 004      | support_request  | It seems like you might need assistance with something specific. Could you please provide more details about your support request? Whether it's technical support, customer service, or something else, I'm here to help! |       
| 005      | other          | Of course! What would you like to inquire about? Feel free to ask any questions or provide more details on the topic you're interested in. |