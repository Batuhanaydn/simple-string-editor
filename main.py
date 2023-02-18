from flask import Flask, request, render_template
from letter_counter import Letter
from sentence_counter import Sentence
from word_counter import Word


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/letter', methods=['GET', 'POST'])
def letter():
    if request.method == 'GET':
        return render_template('letter.html')
    if request.method == 'POST':
        string = request.form.get('string')
        return render_template('result.html', string=string)

@app.route('/word')
def word():
    if request.method == 'GET':
        return render_template('word.html')
    if request.method == 'POST':
        string = request.form.get('string')
        return render_template('result.html', string=string)

@app.route('/sentence')
def sentence():
    if request.method == 'GET':
        return render_template('sentence.html')
    if request.method == 'POST':
        string = request.form.get('string')
        return render_template('result.html', string=string)

@app.route('/most-word-numbers')
def most_word():
    if request.method == 'GET':
        return render_template('most-word.html')

    if request.method == 'POST':
        string = request.form.get('string')
        return render_template('result.html', string=string)

# Find the number of a specific letter
@app.route('/scan-letter')
def scan_letter():
    if request.method == 'GET':
        return render_template('scan-letter.html')
    
    if request.method == 'POST':
        string = request.form.get('string')
        letter = request.form.get('scan-letter')

        return render_template('result.html')

@app.route('/scan-word')
def scan_word():
    if request.method == 'GET':
        return render_template('scan-word.html')

    if request.method == 'POST':
        string = request.form.get('string')
        word = request.form.get('scan-word')

        return render_template('result.html')
        
@app.route('/scan-sentence')
def scan_sentence():
    if request.method == 'GET':
        return render_template('scan-sentence.html')

    if request.method == 'POST':
        string = request.form.get('string')
        sentence = request.form.get('scan-sentence')

        return render_template('result.html')

@app.route('/remove-letter')
def remove_letter():
    if request.method == 'GET':
        return render_template('remove-letter.html')

    if request.method == 'POST':
        string = request.form.get('string')
        letter = request.form.get('remove-letter')

        return render_template('result.html')

@app.route('/remove-word')
def remove_word():
    if request.method == 'GET':
        return render_template('remove-word.html')
    
    if request.method == 'POST':
        string = request.form.get('string')
        word = request.form.get('remove-word')

        return render_template('result.html')

@app.route('/remove-sentence')
def remove_sentence():
    if request.method == 'GET':
        return render_template('remove-sentence.html')

    if request.method == 'POST':
        string = request.form.get('string')
        sentence = request.form.get('remove-sentence')

        return render_template('result.html')

@app.route('/remove-space')
def remove_space():
    if request.method == 'GET':
        return render_template('remove-space.html')

    if request.method == 'POST':
        string = request.form.get('string')

        return render_template('result.html')

@app.route('/remove-newline')
def remove_newline():
    if request.method == 'GET':
        return render_template('remove-newline.html')

    if request.method == 'POST':
        string = request.form.get('string')

        return render_template('result.html')


# Batuhan Aydın
if __name__ == '__main__':
    app.run(debug=True)