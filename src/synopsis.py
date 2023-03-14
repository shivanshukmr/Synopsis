from flask import Flask
from flask import request
from libs import summary
from libs.utils import is_json
from libs.audio_process import get_transcript
from flask_cors import CORS, cross_origin
from flask import render_template
from flask import jsonify

app = Flask(__name__)
cors = CORS(app)

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

@app.route("/api/summary", methods=["GET"])
@cross_origin()
def summarize():
    text = request.args.get('text', None)
    print(text)
    url = request.args.get('url', None)
    print(url)
    if text:
        r = summary.get_summary(text)["choices"][0]["text"]
        return jsonify(
        text=r,
    )
    if url:
        ans = get_transcript(url)
        if ans:
            return jsonify(
                text=summary.get_summary(ans)["choices"][0]["text"])
        return None
   


app.get("api/refactor")


def refactor():
    if is_json(request):
        data = request.json
        refactored_code = summary.get_summary(data, prompt="refactor the code: ")
        return refactored_code
    else:
        return "Content type not supported"


app.run(port=8000, debug=True)
