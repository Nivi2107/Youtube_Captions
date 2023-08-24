from flask import Flask, render_template, request, send_file

from textextraction import download_youtube_captions, download_file

app = Flask(__name__,static_url_path = "/static")

@app.route("/",methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def input():
    result = download_youtube_captions(request.form['link'])
    return render_template('service.html', result=result)

@app.route("/download")
def download():
    download_file()
    path = "captions.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
        app.run(debug=True)