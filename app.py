from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# Set your OpenAI API key
OpenAI.api_key = "YOUR_API_KEY"

# Negotiation logic for price offers
INITIAL_PRICE = 100
MINIMUM_PRICE = 80

def negotiate_price(user_offer):
    if user_offer >= INITIAL_PRICE:
        return "Great! The price is acceptable."
    elif user_offer >= MINIMUM_PRICE:
        counter_offer = user_offer + 5  # Bot proposes a counteroffer slightly above user offer
        return f"I can give you a discount, how about {counter_offer}?"
    else:
        return "Sorry, that price is too low."

@app.route('/negotiate', methods=['POST'])
def negotiate():
    # Get user input from the request (price offer)
    user_input = request.json['user_input']
    user_offer = int(user_input)

    # Generate bot's response
    bot_response = negotiate_price(user_offer)

    return jsonify({"bot_response": bot_response})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
