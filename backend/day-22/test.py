from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "My Web App"
    user = "Alice"
    return render_template('index.html', title=title, user=user)

@app.route('/about')
def about():
    title = 'About Us'
    content = 'Welcome to our About Us page!'
    return render_template('about.html', title=title, content=content)


if __name__ == "__main__":
    # include to run the server
    app.run()
    
    """ put the html file in a folder called templates """
    # /myapp
    #   /templates
    #     index.html
    #   app.py