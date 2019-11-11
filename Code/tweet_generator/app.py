from flask import Flask, render_template
import random
from word_frequency import open_file, histogram, frequency, total_words
from stochastic import stochastic

app = Flask(__name__)

text_title = "Sherlock Holmes"
histogram = (histogram(open_file()))
total_words = total_words(histogram)

@app.route('/')
def index():
    sentence = ""
    # word = arge.sys.get("word")
    i = 10
    while i > 0:
        sentence += stochastic(histogram, total_words) + " "
        i -= 1
    
    return render_template("base.html", word=sentence, title=text_title)

if __name__ == '__main__':
    app.run(debug=True)