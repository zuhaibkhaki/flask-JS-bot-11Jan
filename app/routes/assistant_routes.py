from flask import Blueprint, render_template, request
from app.langfunc.helper import summary

assistant_routes = Blueprint('assistant_routes', __name__)

@assistant_routes.route('/upload', methods=['POST'])
def upload_pdf():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Save the uploaded file
            uploaded_file.save(uploaded_file.filename)
            # return summary
            report_summary = summary()
            return render_template('chat.html', confirm="PDF Uploaded Succesfully!",
                                   summary=report_summary)
    return "No file selected."

@assistant_routes.route('/process_user_query', methods=['POST'])
def process_query():
    if request.method == 'POST':
        # call query handling logic
        response = 'Answer for the query goes here!'
        return render_template('chat.html', response = response)
    
@assistant_routes.route('/process_user_chat', methods=['POST'])
def process_chat():
    if request.method == 'POST':
        # call query handling logic
        query = request.form.get('userInput', '')
        response = f'Answer to your query: {query}'
    return render_template('chat_interface.html', response = response)