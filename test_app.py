from flask import request

with app.test_request_context('/', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/'
    assert request.method == 'POST'