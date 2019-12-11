from flask import Flask, render_template, request, url_for
import random
from histogram import open_file, histogram, frequency, total_words
from stochastic import stochastic

from markov_chain_nth_order import Markov

app = Flask(__name__)

text_title = "EDGAR ALLAN POE"
# histogram = (histogram(open_file('test.txt')))
# total_words = total_words(histogram)

file_content = open_file("test.txt")
markov_chain = Markov(file_content, 2)

@app.route('/')
def index():
    # sentence = ""
    # # word = arge.sys.get("word")
    num = request.args.get('length')
    # if num:
    #     i = 0
    #     while i < int(num):
    #         sentence += stochastic(histogram, total_words) + " "
    #         i += 1

    #     return render_template("base.html", word=sentence, title=text_title)

    # else:
    #     i = 0
    #     while i < 10:
    #         sentence += stochastic(histogram, total_words) + " "
    #         i += 1

    #     return render_template("base.html", word=sentence, title=text_title)

    # print(sentence)


    if num:
        sentence = markov_chain.get_sentence(int(num))
        return render_template("base.html", word=sentence, title=text_title)
    else:
        sentence = markov_chain.get_sentence(10)
        return render_template("base.html", word=sentence, title=text_title)


if __name__ == '__main__':
    app.run(debug=True)