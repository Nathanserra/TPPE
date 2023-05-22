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

    
    