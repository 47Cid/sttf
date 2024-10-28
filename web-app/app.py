from flask import Flask, request, render_template

app = Flask(__name__)

@app.after_request
def add_csp_header(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "object-src 'none'; "
        "script-src 'none'; "
        "base-uri 'none'; "
        "style-src 'unsafe-inline'; "
        "img-src *;"
    ) 
    return response


@app.route('/')
def home():
    note = request.args.get('note', '')  # Get 'note' parameter from the URL
    # Render the HTML template and pass the 'note' variable
    response = render_template('home.html', note=note)
    # Set Content Security Policy

    return response

if __name__ == '__main__':
    app.run(debug=True)