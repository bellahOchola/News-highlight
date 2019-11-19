class News:
    '''
    class that defines the news objects
    '''

    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

class Articles:
    '''
    class that defines the article objects
    '''

    def __init__(self,id,url,author,description,urlToImage,publishedAt):
        self.url = url
        self.id = id
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.urlToImage = urlToImage

