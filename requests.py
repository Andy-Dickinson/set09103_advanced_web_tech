from flask import Flask, request
app = Flask(__name__)



@app.route("/")
def root():
    return "The default, 'root' route"


# A route will accept Get requests by default, and also supports HEAD automatically when GET present.
# Specify route can accept other requests using 'methods'
# use if..else to execute different code relevant to requests
@app.route("/account/", methods=['GET', 'POST'])
def account():

    # can print out request info on server for debug purposes
    print("request info:", request.method, request.path, request.form)


    # to test GET request, just visit URL/account
    # to test POST: curl -i -X POST <server_URL:port/account>
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        page = '''
        <html>
        <body>
            <form action="" method="post" name="form">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body>
        </html>
        '''
        return "GET'ting /account root"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debut=True)