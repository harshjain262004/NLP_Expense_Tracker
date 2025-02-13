from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv
from SqlBot import *
from genAns import *
from db import *

app = Flask(__name__)

# Define a route to handle incoming requests
@app.route('/whatsapp', methods=['POST'])
def chatgpt():
    query = request.values.get('Body', '').lower()
    SQL = generate_PgSql(query)
    Data = ExecuteSQL(SQL)
    answer = GenerateNaturalAnswer(Data,query,SQL)
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(answer)
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)

