class URLBuilder:
    def __init__(self, builder):
        self.protocol = builder.protocol
        self.hostname = builder.hostname
        self.port = builder.port
        self.path_param = builder.path_param
        self.query_param = builder.query_param

    def __str__(self):
        url = f"{self.protocol}://{self.hostname}"
        if self.port:
            url += f":{self.port}"
        if self.path_param:
            url += f"/{self.path_param}"
        if self.query_param:
            url += f"?{self.query_param}"
        return url
    
    class Builder:
        def __init__(self):
            self.protocol = None
            self.hostname = None
            self.port = None
            self.path_param = None
            self.query_param = None

        def set_protocol(self, protocol):
            self.protocol = protocol
            return self
        
        def set_hostname(self, hostname):
            self.hostname = hostname
            return self
        
        def set_port(self, port):
            self.port = port
            return self
        
        def set_query_param(self, query_param):
            self.query_param += query_param
            return self
        
        def set_path_param(self, path_param):
            self.path_param = path_param
            return self
        
        def build(self):
            return URLBuilder(self)
        



# Without builder Pattern
class URL:
    def __init__(self, protocol, domain, port, path, query_param):
        self.protocol = protocol
        self.domain = domain
        self.port = port
        self.path = path
        self.query_param = query_param


    def __str__(self):
        # Construct the URL string based on whether port and query_param are provided
        url = f"{self.protocol}://{self.domain}"
        if self.port:
            url += f":{self.port}"
        if self.path:
            url += f"/{self.path}"
        if self.query_param:
            url += f"?{self.query_param}"
        return url

# Creating a URL without a builder
url = URL(
    protocol="https",
    domain="example.com",
    path="search",
    query_param="key=value",
)

# Example Usage:
if __name__ == "__main__":
    url = (
        URLBuilder.Builder()
        .set_protocol("https")
        .set_hostname("example.com")
        .set_port("8080")  # Optional
        .set_path_param("api/v1/resource")
        .set_query_param("key=value")
        .build()
    )

    print(url)  # Output: https://example.com:8080/api/v1/resource?key=value