class Good(object):
    def __init__(self, description, img, price):
        self.description = description
        self.img = img
        self.price = price

    def tojson(self):
        json = {}
        json['description'] = self.description
        json['img'] = self.img
        json['price'] = self.price
        return json