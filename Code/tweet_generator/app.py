from flask import Flask, render_template, request, url_for
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
    num = request.args.get('length')
    if num:
        i = 0
        while i < int(num):
            sentence += stochastic(histogram, total_words) + " "
            i += 1

        return render_template("base.html", word=sentence, title=text_title)

    else:
        i = 0
        while i < 10:
            sentence += stochastic(histogram, total_words) + " "
            i += 1

        return render_template("base.html", word=sentence, title=text_title)

    print(sentence)

if __name__ == '__main__':
    app.run(debug=True)