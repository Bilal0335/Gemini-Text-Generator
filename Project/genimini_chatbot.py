import google.generativeai as genai
API_KEY = "AIzaSyBbHkLAjGRRhY73L99nQ9siY__8oPgVzRs"
genai.configure(api_key=API_KEY)

# ! Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

user_input = input("Enter Your Prompt = ")
output = getResponseFromModel(user_input)
print(output)
