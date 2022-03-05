import logging
from pytube import YouTube
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/download_video", methods=["GET", "POST"])
def download_video():
    try:
        youtube_url = request.form["URL"]

        download_path = YouTube(youtube_url).streams.get_highest_resolution().download()
        fname = download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception("Failed download")
        return "Video download failed!"


if __name__ == "__main__":
    app.run(debug=True)

