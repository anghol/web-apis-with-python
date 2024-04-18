from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    # Render the index.html template and return it
    return render_template('index.html')

@app.get("/search")
def search():
    args = request.args.get("q")
    action = request.args.get("action")
    if action == 'search':
        return redirect(f'https://google.com/search?q={args}')
    elif action == 'lucky':
        return redirect('https://google.com/search?q=chipi+chipi+chapa+chapa')

if __name__ == "__main__":
    app.run()