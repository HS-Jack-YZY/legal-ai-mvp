from google import genai

client = genai.Client()

prompts = "teach me how to use gemini api"

response = client.models.generate_content(model="gemini-2.5-flash", contents=prompts)

print(response.text)
