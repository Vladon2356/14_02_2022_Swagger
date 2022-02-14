from app.app import create_app
DEBUG = True
app = create_app()

if __name__ == "__main__":
    app.config.from_object(__name__)
    app.run(debug=True)
