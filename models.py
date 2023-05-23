import json

class Identifier:
    def __init__(self, lattes, orcid):
        self.lattes = lattes
        self.orcid = orcid

    def completeness(self):
        if (not self.lattes and self.orcid) or (self.lattes and not self.orcid):
            return 1
        else:
            return 0


class Author:
    def __init__(self, nationality, birthCountry, birthCity, birthState, lattes, orcid):
        self.identifier = Identifier(lattes, orcid)
        self.nacionality = nationality
        self.birthCountry = birthCountry
        self.birthCity = birthCity
        self.birthState = birthState

    def completeness(self):
        completeness = 0
        if self.nacionality:
            completeness += 0.125
        if self.birthCountry:
            completeness += 0.125
        if self.birthCity:
            completeness += 0.125
        if self.birthState:
            completeness += 0.125
        
        completeness += self.identifier.completeness() / 2

        return completeness
        

class Article:
    def __init__(self, title, publicationDate, language):
        self.title = title
        self.publicationDate = publicationDate
        self.language = language
        self.authors = []

    def addAuthor(self, author):
        self.authors.append(author)
    
    def completeness(self):
        completeness = 0

        if self.title:
            completeness += 0.25
        if self.publicationDate:
            completeness += 0.25
        if self.language:
            completeness += 0.25

        if self.authors:
            completeness += self.authors[0].completeness() / 4
        
        return completeness

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data
    
    def get_articles(self):
        data = self.read_json()
        list_articles = []

        for article in data:
            artcl = Article(article['title'], article['language'], article['publicationDate'])

            for author in article['authors']:
                nationality = author.get("nacionality", None)
                birthCountry = author.get("birthCountry", None)
                birthCity = author.get("birthCity", None)
                birthState = author.get("birthState", None)
                lattes = author.get("identifier.lattes", None)
                orcid = author.get("identifier.orcid", None)
                artcl.addAuthor(Author(nationality, birthCountry, birthCity, birthState, lattes, orcid))

            list_articles.append(artcl)

        return list_articles
    