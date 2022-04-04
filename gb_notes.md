
## My Notes

1. All items will have the three attributes as follows:
    1. `name` – Name of the item.
    2. `sell_in` – The number of days within which the item should be sold off.
    3. `quality` – The quality of the item; 
        ***take note***
        1. Can never be negative
        2. can never be more than 50 
2. Every day, the method `update_quality()` is executed, which lowers the values for `sell_in` and `quality` each. 
3. Once the `sell_in` date has passed, the value for `quality` degrades twice faster.
4. There are also rules for each of the items that are currently present which are as follows.
    1. *AgedBrie* increases its `quality` with a decrease in `sell_in` value. 
    2. *BackstagePasses* has the following two rules:
        1. When `sell_in` value is more than **10**, `quality` increases by **1**.
        2. When `sell_in` value is **between 6 and 10**, `quality` increases by **2**.
        3. When `sell_in` value is **between 1 and 5**, `quality` increases by **3**.
        4. When `sell_in` value is **0**, `quality` is set to **0**.
    3. Sulfuras is legendary, so `quality` is always **80** and `sell_in` value never decreases.
    4. A new item – *Conjured* is to be added with the following rule:
        1. *Conjured* items degrade `quality` twice as fast as normal items.



## Questions

1. As per the requirement the quality of sulfuras should always be 80. So if a quality of a sulfuras item in the input is specified as say 5, should the quality be changed to 80 ?? as of now it will remain unchanged.
2. as per rule 3 the quality of a item degraded twice faster after sell in date. that doesnt mean the quality of aged brie increases twice faster after sell in date (which is the case now). Seems to me that this is a wrong assumption. 
