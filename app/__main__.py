
from app.__init__ import create_app
from app.sum_routes import sum_bp 

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
