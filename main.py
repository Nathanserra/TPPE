from models import JsonReader

if __name__ == '__main__':

    reader = JsonReader('extratoFioCruz.json')
    list = reader.get_articles()

        
    for article in list:
        print("O artigo: " + article.title)
        print("Prossui " + str(article.completeness() * 100) + " de completude")
        print()
