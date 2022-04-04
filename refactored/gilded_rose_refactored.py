# -*- coding: utf-8 -*-

def validate_quality(quality):
    if quality < 0:
        quality = 0
    if quality >50:
        quality = 50
    return quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                # sulfuras remain untouched. proceed to the next item
                continue
            if item.name == "Aged Brie":
                if item.sell_in > 0:
                    # quality of aged brie increases every day
                    item.quality += 1
                else:
                    # but after sell in date it doubles
                    item.quality += 2
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # BackstagePasses has the following rules:
                # When sell_in value is more than 10, quality increases by 1.
                # When sell_in value is between 6 and 10, quality increases by 2.
                # When sell_in value is between 1 and 5, quality increases by 3.
                # When sell_in value is 0, quality is set to 0.
                if item.sell_in > 10:
                    item.quality += 1
                elif 6 <= item.sell_in <= 10:
                    item.quality += 2
                elif 1 <= item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in < 1:
                    item.quality = 0
            elif item.name == "Conjured Mana Cake":
                # conjured items decreases twice as fast
                item.quality -= 2
            else:
                if item.sell_in < 1:
                    item.quality -= 2
                else:
                    item.quality -= 1

            # ensure that quality is within bounds
            item.quality = validate_quality(item.quality)
            # at the end of the days run reduce the sell in by 1. there are no business rules for that.
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)