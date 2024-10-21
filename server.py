""" This is the server.py file. Executing this function initiates the application
    emotion detector to be executed over the Flask channel and deployed
    on localhost:5000
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """ This code is the emotion detector code 
    """
    text_to_analyze = str(request.args.get('textToAnalyze'))
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!<b>"

    response_str = ", ".join(f"'{key}': {value}" for key, value in response.items())
    response_arr = response_str.split(", 'dominant_emotion':")
    response_str = "For the given statement, the system response is " + response_arr[0]
    response_str += ". The dominant emotion is <b>" + response_arr[1]+"<b>."
    return response_str

@app.route("/")
def render_index_page():
    """ This is the index route rendering the index.html
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
