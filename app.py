import nltk

# download these model from nltk
nltk.download('wordnet')
nltk.download('punkt')

from logging import debug
from flask import Flask,render_template,request
from textblob import TextBlob
from textblob import Word


# create a flask app
app = Flask(__name__)

# define an api
@app.route('/')
def home():
    return render_template('index.html') 

@app.route("/check", methods = ["POST"])
def check():
    # get the info:
    word = request.form.get('Word')

    # take the word and get the correct word
    text = TextBlob(word)
    text_1 = text.correct()
  
      
    # check if the word entered on the screen and corrected word is same :
    if text == text_1:
        return render_template('index.html',Explaination = f"Great! Entered word has correct spelling")
    else:
        temp =Word(word)
        correct_spell = temp.spellcheck()
        display_word = [x[0] for x in correct_spell][:3]
        return render_template('index.html',Explaination = f"Entered Word has incorrect spelling. Did you mean : {display_word} ?")


if __name__ == '__main__':
    
    app.run(host="0.0.0.0",port=5000,debug=True)