from flask import Flask

app = Flask(__name__)

html_content = """
<h1> Hello World! </h1>
<p> This is a paragraph. </p>
<p> This is another paragraph. </p>
<p> This website is made by using Flask! </p>
<p> Flask is a python web framework used for creating websites!</p>
"""

@app.route("/")
def hello_world():
    return html_content

app.run(debug=True)