from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/journal')
def journal():
    # Change the path of the output.txt file to where it is on your system. 
    file_path = os.path.join(app.root_path, '/Users/devpatel/Desktop/MyBuddy/script/output.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        user_entry_content = file.read().replace('\n', '<br>')

    return render_template('journal.html', user_entry_content=user_entry_content)

@app.route('/support')
def support():
    return render_template('/support.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    # Change the path of the gpt-interpreter file to where it is on your system. 
    subprocess.run(['python', 'script/gpt-interpreter.py'])
    return 'Script executed successfully!'

if __name__ == '__main__':
    app.run(debug=True)
