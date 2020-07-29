from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Users/arifhaque/PycharmProjects/Scraper/Sale Scraper.py')
def my_link():
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)



@app.route("/")
def hello():
    return '''
    <!doctype html>
    <html>
    <h1>Dubizzle Listing Bot</h1>
    <form action="/my-link/">
            <input type="submit" value="Click me" />
        </form
    <body>

    <button> <a href="/Users/arifhaque/PycharmProjects/Scraper/Sale Scraper.py">Click me</a></button>

    
    </body>
    </html>
'''
if __name__ == '__main__':
    app.run(debug=True)