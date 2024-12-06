import textwrap
from openai import OpenAI

def llm_summarize_JSON(email_data):
    client = OpenAI()

    # System message explicitly describing the expected behavior and output
    system_message = textwrap.dedent("""\
        You are an expert email summarizer that provides structured JSON output. 
        Given a list of emails in JSON format, summarize each email and return an array of objects, where each object has:
        - "date": The date of the email (as provided in the input).
        - "description": A concise, accurate, and helpful summary of the email content.

        The input JSON will have the following structure:
        [
            {"id": "someid", "sender": "somesender", "subject": "somesubject", "date": "somedate", "body": "somebody"}
        ]

        Example input for one email:
        [
            {
                "id": "19399c3eaf00f29a",
                "sender": "Marcus Ingram <marcus-noreply@mail.com>",
                "subject": "Meeting Reminder for proposal;",
                "date": "Fri, 6 Dec 2024 02:19:33 +0000 (UTC)",
                "body": "Just a reminder about our meeting tomorrow at 10 AM. Bring a notepad, pencils etc. I think I should be able to make it on time but Ill let you know otherwise."
            }
        ]

        Example output for one email:
        [
            {
                "id": 19399c3eaf00f29a",
                "date": "2024, 6 December",
                "description": "Marcus reminding you about a proposal meeting and to bring pencils tomorrow at 10 AM."
            }
        ]

        Constraints:
        - Only include the "id", "date", and "description" fields in the output.
        - Do not fabricate information; summarize only the given data.
        - Ensure the output is a valid JSON array.
    """)

    # OpenAI completion request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": email_data}
        ]
    )

    # Extract the content
    content = response.choices[0].message.content

    # Return the content directly as JSON (it should be JSON as per instructions)
    return content
