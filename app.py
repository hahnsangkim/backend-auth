from routes import create_routes
from config import create_app

app = create_app()
create_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')	