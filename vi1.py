import random
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')

def get_ai_choice():
    return random.randint(1, 10)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        user_input = request.form['user_input']

        try:
            user_input = int(user_input)
            if 1 <= user_input <= 10:
                ai = get_ai_choice()
                result = f"AI chose {ai}. "
                
                if user_input == ai:
                    result += "Congratulations! You win!"
                else:
                    result += "Sorry, you didn't win. Try again!"

            else:
                result = "Please enter a number between 1 and 10."
        except ValueError:
            result = "Invalid input. Please enter a valid number."

        return render_template('index.html',result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)


