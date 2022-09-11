class HttpPackage:
    def __init__(self, address, method, user_data=None, port=443):
        self.address = address
        self.port = port
        self.method = method
        self.data = user_data


class HttpClient:
    @staticmethod
    def send(package):
        print(f"Sending request with {package}")


class HTTPServer:
    @classmethod
    def get(cls, package):
        print(f"Sending GET to {package.address}")

    @classmethod
    def post(cls, package):
        print(f"Sending POST to {package.address}")
        print(f"Data is {package.data}")

    @classmethod
    def handle_user_request(cls, package: HttpPackage):
        if package.method == "get":
            cls.get(package)
        if package.method == "post":
            cls.post(package)


package = HttpPackage(address="google.com", method="get", user_data={"username": "dima", "password": "admin"})
HttpClient.send(package)