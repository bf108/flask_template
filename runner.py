from src import create_app

app = create_app()

if __name__ == '__main__':
    port = app.config.get('PORT',5002)
    app.run(host='localhost',port=port)