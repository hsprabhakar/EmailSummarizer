import textwrap
from openai import OpenAI

def llm_test(email_data):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize the following emails."},
            {
                "role": "user",
                "content": email_data
            }
        ]
    )

    return completion.choices[0].message.content


def llm_summarize_JSON(email_data):
    client = OpenAI()

    system_message = textwrap.dedent("""\
            You are an expert email summarizer that is capable of reading, understanding, and summarizing email data in JSON format. You will be receiving multiple email message to digest, all in the JSON format shown below.

            An example JSON body you will see is shown below:
            x = {
            "From": headers[0],
            "Subject": headers[1],
            "Date": headers[2],
            "Body": body
            }

            Please consider the 4 fields in the example body above: From, Subject, Date, and Body. Here is a definition of each field:
            "From": contains information about who this email is from
            "Subject": the subject of the email message
            "Date": a timestamp of when the message was sent
            "Body": the email message body, which includes the actual contents of the email message

            You will be tasked to read and summarize various email messages in the format shown above. Do not make up any information that is not explicitly stated in a previous message.
            """)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": system_message
            },
            {
                "role": "user", 
                "content": email_data
            }
        ],
        #TODO: improve the response format
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "email_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "title": "email",
                            "description": "summary of the email",
                            "type": "string"
                        },
                        "additionalProperties": False
                    }
                }
            }
        }
    )
    
    return response.choices[0].message.content
