class Identifier:
    def __init__(self, lattes, orcid):
        self.lattes = lattes
        self.orcid = orcid

class Author:
    def __init__(self, nationality, birthCountry, birthCity, birthState, lattes, orcid):
        self.identifier = Identifier(lattes, orcid)
        self.nacionality = nationality
        self.birthCountry = birthCountry
        self.birthCity = birthCity
        self.birthState = birthState

class Article:
    def __init__(self, title, publicationDate, language):
        self.title = title
        self.publicationDate = publicationDate
        self.language = language
        self.authors = []

    def addAuthor(self, author):
        self.authors.append(author)

    
    