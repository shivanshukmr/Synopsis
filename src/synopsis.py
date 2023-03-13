from flask import Flask
from flask import request
from libs import summary
from libs.utils import is_json
from libs.audio_process import get_transcript

app = Flask(__name__)


@app.route("/api/summary", methods=["GET"])
def summarize():
    if is_json(request):
        data = request.json
        url = data.get("url", None)
        text = data.get("text", None)
        if text:
            r = summary.get_summary(text)["choices"][0]["text"]
            print(type(r))
            return r
        if url:
            ans = get_transcript(url)
            return summary.get_summary(ans)["choices"][0]["text"]
    else:
        return "Content type not supported"


app.get("api/refactor")


def refactor():
    if is_json(request):
        data = request.json
        refactored_code = summary.get_summary(data, prompt="refactor the code: ")
        return refactored_code
    else:
        return "Content type not supported"


app.run(port=8000, debug=True)
