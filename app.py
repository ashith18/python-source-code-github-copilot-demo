from flask import Flask, render_template, request
import os
import openai
app = Flask(__name__, template_folder='templates')

# OpenAI API credentials
openai.api_key = 'sk-o7hL4nCDcjw'

def get_chatbot_response(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = float(request.form['number1'])
    number2 = float(request.form['number2'])
    operation = request.form['operation']
    result = 0

    if operation == 'add':
        result = number1 + number2
    elif operation =='sub':
        result = number1 - number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'divide':
        if number2 != 0:
            result = number1 / number2
        else:
            return 'Cannot divide by Zero!'
        
    

    return render_template('result.html', result=result)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = get_chatbot_response(user_message)
    return response

if __name__=='__main__':
    app.run(debug=True)
            
