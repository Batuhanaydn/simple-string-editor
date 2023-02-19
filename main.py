from flask import Flask, request, render_template
from letter_counter import Letter
from sentence_counter import Sentence
from word_counter import Word
from most_frequent_character import Frequent
from scan_letter import ScanLetter
from scan_word import ScanWord
from scan_sentence import ScanSentence
from remove_letter import RemoveLetter
from remove_word import RemoveWord
from remove_sentence import RemoveSentence
from remove_space import RemoveSpace
from remove_newline import RemoveNewLine


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
        result = Letter.letter_counter(string)
        return render_template('result.html', result=result)

@app.route('/word')
def word():
    if request.method == 'GET':
        return render_template('word.html')
    if request.method == 'POST':
        string = request.form.get('string')
        result = Word.word_counter(string)
        return render_template('result.html', result=result)

@app.route('/sentence')
def sentence():
    if request.method == 'GET':
        return render_template('sentence.html')
    if request.method == 'POST':
        string = request.form.get('string')
        result = Sentence.sentence_counter(string)
        return render_template('result.html', result=result)

@app.route('/most-word-numbers')
def most_word():
    if request.method == 'GET':
        return render_template('most-word.html')

    if request.method == 'POST':
        string = request.form.get('string')
        result = Frequent.most_frequent_character(string)
        return render_template('result.html', result=result)

# Find the number of a specific letter
@app.route('/scan-letter')
def scan_letter():
    if request.method == 'GET':
        return render_template('scan-letter.html')
    
    if request.method == 'POST':
        string = request.form.get('string')
        letter = request.form.get('scan-letter')
        result = ScanLetter.scan_letter(string, letter)
        return render_template('result.html', result=result)

@app.route('/scan-word')
def scan_word():
    if request.method == 'GET':
        return render_template('scan-word.html')

    if request.method == 'POST':
        string = request.form.get('string')
        word = request.form.get('scan-word')
        result = ScanWord.scan_word(string, word)
        return render_template('result.html', result=result)
        
@app.route('/scan-sentence')
def scan_sentence():
    if request.method == 'GET':
        return render_template('scan-sentence.html')

    if request.method == 'POST':
        string = request.form.get('string')
        sentence = request.form.get('scan-sentence')
        result = ScanSentence.scan_sentence(string, sentence)
        return render_template('result.html', result=result)

@app.route('/remove-letter')
def remove_letter():
    if request.method == 'GET':
        return render_template('remove-letter.html')

    if request.method == 'POST':
        string = request.form.get('string')
        letter = request.form.get('remove-letter')
        result = RemoveLetter.remove_letter(string, letter)
        return render_template('result.html', result=result)

@app.route('/remove-word')
def remove_word():
    if request.method == 'GET':
        return render_template('remove-word.html')
    
    if request.method == 'POST':
        string = request.form.get('string')
        word = request.form.get('remove-word')
        result = RemoveWord.remove_word(string, word)
        return render_template('result.html', result=result)

@app.route('/remove-sentence')
def remove_sentence():
    if request.method == 'GET':
        return render_template('remove-sentence.html')

    if request.method == 'POST':
        string = request.form.get('string')
        sentence = request.form.get('remove-sentence')
        result = RemoveSentence.remove_sentence(string, sentence)
        return render_template('result.html', result=result)

@app.route('/remove-space')
def remove_space():
    if request.method == 'GET':
        return render_template('remove-space.html')

    if request.method == 'POST':
        string = request.form.get('string')
        result = RemoveSpace.remove_space(string)
        return render_template('result.html', result=result)

@app.route('/remove-newline')
def remove_newline():
    if request.method == 'GET':
        return render_template('remove-newline.html')

    if request.method == 'POST':
        string = request.form.get('string')
        result = RemoveNewLine.remove_new_line(string)
        return render_template('result.html', result=result)


# Batuhan Aydın
if __name__ == '__main__':
    app.run(debug=True)