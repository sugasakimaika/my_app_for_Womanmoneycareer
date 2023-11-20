from flask import Flask, request, render_template

womanmoneycareer = Flask(__name__)

@womanmoneycareer.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # ここにロジックを実装
        return render_template('index.html', result=user_input)
    return render_template('index.html')

if __name__ == '__main__':
    womanmoneycareer.run(debug=True)

