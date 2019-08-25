from app import app

@app.route('/')
def index():
    return "<h1>Hello World</h1>"
    
if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True)