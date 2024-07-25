"""Task
You will be given a list of objects. Each object has type, material, and possibly secondMaterial. The existing materials are: paper, glass, organic, and plastic.

Your job is to sort these objects across the 4 recycling bins according to their material (and secondMaterial if it's present), by listing the type's of objects that should go into those bins.

Notes
The bins should come in the same order as the materials listed above
All bins should be listed in the output, even if some of them are empty
If an object is made of two materials, its type should be listed in both of the respective bins
The order of the type's in each bin should be the same as the order of their respective objects was in the input list
Contrary to the example below, the output in Python should be a tuple of 4 lists instead of a 2-dimensional list
Example
input = [
  {"type": "rotten apples", "material": "organic"},
  {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
  {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
  {"type": "amazon box", "material": "paper"},
  {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
]

output = [
  ["wine bottle", "amazon box", "beer bottle"],
  ["wine bottle", "beer bottle"],
  ["rotten apples", "out of date yogurt"],
  ["out of date yogurt"]
]"""

class Garbage:
    def __init__(self, type, material, secondMaterial = None):
        self.type = type
        self.material = material
        self.secondMaterial = secondMaterial

class Bin:
    def __init__(self):
        self.paper_bin = []
        self.glass_bin = []
        self.organic_bin = []
        self.plastic_bin = []

    def sort_by_first_material(self, garbage):
        if garbage.material == "paper":
            self.paper_bin.append(garbage.type)
        elif garbage.material == "glass":
            self.glass_bin.append(garbage.type)
        elif garbage.material == "organic":
            self.organic_bin.append(garbage.type)
        elif garbage.material == "plastic":
            self.plastic_bin.append(garbage.type)

    def sort_by_second_material(self, garbage):
        if garbage.secondMaterial is not None:
            if garbage.secondMaterial == "paper":
                self.paper_bin.append(garbage.type)
            elif garbage.secondMaterial == "glass":
                self.glass_bin.append(garbage.type)
            elif garbage.secondMaterial == "organic":
                self.organic_bin.append(garbage.type)
            elif garbage.secondMaterial == "plastic":
                self.plastic_bin.append(garbage.type)

def recycle(a):
    bin = Bin()
    for g in a:
        garbage = Garbage(**g)
        bin.sort_by_first_material(garbage)
        bin.sort_by_second_material(garbage)
    return (bin.paper_bin, bin.glass_bin, bin.organic_bin, bin.plastic_bin)

