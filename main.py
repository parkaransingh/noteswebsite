from website import create_app

app = create_app()

# only if we run this file, we want to execute this line, not when we just import it
if __name__ == '__main__':
    app.run(debug =True) # run the flask application with webserver, debug = true means everytime we make a change, it automatically reruns the flask server

# verizon phone number 7709576407 