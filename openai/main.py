import openai

# 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

openai.api_key = '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'

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="What is the Ecole42?",
    max_tokens=50,
    temperature=0.8
)

generated_text = response['choices'][0]['text']
print(generated_text)
