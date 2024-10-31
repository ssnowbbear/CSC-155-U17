# create a class for big cats

class BigCat():
    def __init__(self, weight=0, common_name = [], genus = "", species = "", coat_pattern = ""):
        self.weight = weight
        self.common_name = common_name
        self.genus = genus
        self.species = species
        self.coat_pattern = coat_pattern
    def __repr__(self):
        return f"{self.common_name}"
    def __lt__(self, other): #defines < behvior (make '.sort()' work), sorting by 'str',
        # will sort alphabetically
        if self.weight < other.weight:
            return True
        else:
            return False
    def __mul__(self, other): #define * behavior
        if self.common_name == "lion" and other.common_name == "tiger":
            return "liger"
        elif self.common_name == "tiger" and other.common_name == "lion":
            return "tigon"
        else:
            return "I don't know"
        

bigcat1 = BigCat(300, "lion", "panthera", "leo", "solid")
bigcat2 = BigCat(450, "tiger", "panthera", "tigris", "striped")
bigcat3 = BigCat(100, "puma", "felis", "concolor", "solid")
catlist = [bigcat1, bigcat2, bigcat3]

print(catlist)
catlist.sort()
print(catlist)


class Movie:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year =  year
    def __repr__(self):
        return f"{self.title} {self.year}"
    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False
        


movielist = [Movie "", 1970...] # make example later

