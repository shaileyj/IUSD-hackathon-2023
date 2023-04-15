import openai
import json

def get_questions(subject):
    openai.api_key = open("openapikey.secret").read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a bot writing multiple choice AP test questions. "
                                              "Format your response as a valid JSON dictionary in the following syntax: "
                                              "call the main dictionary questions, and within each item in it include the string question,"
                                              " a list of the options as a list named options including strings that include the letter of the"
                                              " answer(in uppercase) and the possible answer option. Also include in questions the string answer, which contains the "
                                              "letter of the correct answer(in uppercase), and explanation, which contains a short explanation"
                                              " of why the correct answer is correct."},
                {"role": "user", "content":" Generate questions on " + subject},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return json.loads(result)
