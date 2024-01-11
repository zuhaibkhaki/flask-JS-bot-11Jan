from flask import Flask, render_template, request, Blueprint
app = Flask(__name__)

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main_routes.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key} : {value}')
    return render_template('chat.html', bot_name="MediQuery")

@main_routes.route('/chat_interface', methods=['GET'])
def chat_interface():
    return render_template('chat_interface.html')