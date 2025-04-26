from web import create_app

if __name__ == '__main__':
    app = create_app()
    # Use Waitress for Windows compatibility
    from waitress import serve
    serve(app, host='127.0.0.1', port=5000)