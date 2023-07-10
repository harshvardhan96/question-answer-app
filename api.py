from flask import Flask, request, jsonify, render_template
import redis

# Connect to Redis
redis_host = 'localhost'  # Update with the actual Redis host
redis_port = 6379  # Update with the actual Redis port
redis_db = 0  # Update with the actual Redis database number
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

app = Flask(__name__)

def insert_data():
    # Store the information using Hashes
    redis_client.hset("pan_card", "about_pan_card",
                      "The PAN card is a unique ten-digit alphanumeric identification number...")
    redis_client.hset("pan_card", "who_needs_pan_card",
                      "All individuals/non-individuals (including foreign citizens/entities) earning taxable income in India must have a PAN card.")
    redis_client.hset("pan_card", "types_of_pan_cards",
                      "In India, two types of PAN cards are available: e-PAN card and physical PAN card...")
    redis_client.hset("pan_card", "nris_and_pan_card",
                      "NRIs don’t need to have a PAN Card. However, a PAN Card is necessary for NRIs if they wish to do any of the following in India...")
    redis_client.hset("pan_card", "importance_for_nri_accounts",
                      "NRI Accounts comprise of NRE, NRO, and FCNR Accounts. A basic overview to understand the importance of PAN Card with respect to these three accounts...")
    redis_client.hset("pan_card", "pan_card_application_process",
                      "New Pan Card: How can NRI apply for a new PAN card...")
    redis_client.hset("pan_card", "documents_required",
                      "If you have Aadhaar card: No other document is required. You can get your pan card through your Aadhaar card in 10 minutes. If you don’t have an Aadhaar card: Passport (Any Country) / OCI Card, Passport Size Photograph, Overseas address proof with zip code...")
    redis_client.hset("pan_card", "cost_of_new_pan_card",
                      "The PAN CARD Application through ABC costs Rs 2500 for E-PAN, and if you want it to be couriered, it will cost Rs 1200 extra for physical delivery to your address...")
    redis_client.hset("pan_card", "time_required_to_issue_pan_card",
                      "If you have Aadhaar card: You can get a Pan Card instantly (in under 10 minutes), if you have an Aadhaar card. You can apply through ABC. If you don’t have an Aadhaar card: Once the payment is made to ABC, we will contact you and initiate the process. Pan card will be issued in 3 weeks...")
    redis_client.hset("pan_card", "updation_correction_in_pan_card",
                      "Information that can be updated in the PAN Card: Your name, Father’s name, Date of Birth, Citizenship, Photograph, Signature, Gender, Address, Contact details")

    keys = redis_client.keys("*")
    print("Data Added:",keys)

def retrieve_data():
    # Retrieve the data for each section efficiently
    about_pan_card = redis_client.hget("pan_card", "about_pan_card").decode()
    who_needs_pan_card = redis_client.hget("pan_card", "who_needs_pan_card").decode()
    types_of_pan_cards = redis_client.hget("pan_card", "types_of_pan_cards").decode()
    nris_and_pan_card = redis_client.hget("pan_card", "nris_and_pan_card").decode()
    importance_for_nri_accounts = redis_client.hget("pan_card", "importance_for_nri_accounts").decode()
    pan_card_application_process = redis_client.hget("pan_card", "pan_card_application_process").decode()
    documents_required = redis_client.hget("pan_card", "documents_required").decode()
    cost_of_new_pan_card = redis_client.hget("pan_card", "cost_of_new_pan_card").decode()
    time_required_to_issue_pan_card = redis_client.hget("pan_card", "time_required_to_issue_pan_card").decode()
    updation_correction_in_pan_card = redis_client.hget("pan_card", "updation_correction_in_pan_card").decode()

    # Print the retrieved data for each section
    print("About Pan Card:\n", about_pan_card)
    print("\nWho Needs a Pan Card:\n", who_needs_pan_card)
    print("\nTypes of PAN Cards:\n", types_of_pan_cards)
    print("\nNRIs and Pan Card:\n", nris_and_pan_card)
    print("\nImportance for NRI Accounts:\n", importance_for_nri_accounts)
    print("\nPAN Card Application Process:\n", pan_card_application_process)
    print("\nDocuments Required for a New PAN Card:\n", documents_required)
    print("\nCost of New PAN Card:\n", cost_of_new_pan_card)
    print("\nTime Required to Issue PAN Card:\n", time_required_to_issue_pan_card)
    print("\nUpdation/Correction in the PAN Card:\n", updation_correction_in_pan_card)

# Function to retrieve answer from Redis
def get_answer_from_redis(question):
    # Retrieve the answer from Redis based on the user input question
    answer = redis_client.hget("pan_card", question)
    return answer

@app.route('/', methods=['GET'])
def welcome():
    # print("Welcome to the home page of question answering tool!")
    insert_data()
    return "Welcome to the home page of question answering tool!"

@app.route('/question', methods=['POST'])
def answer_question():

    print("Enter your question:")

    # Get the question from the request
    data = request.get_json()
    question = data['question']

    # Check if answer is available in Redis
    answer = get_answer_from_redis(question)

    # Prepare the response
    response = {'question': question, 'answer': answer.decode() if answer else 'Answer not found'}

    # print(response['answer'])

    # Render the response in an HTML template
    return response['answer']

    # return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
