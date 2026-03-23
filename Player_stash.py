class Item:
    def __init__(self, item_id, name, weight):

        self.item_id = item_id
        self.name = name
        self.weight = weight


    def __repr__(self):
        return f"{self.name}(id = {self.item_id},w = {self.weight})"
 
class Stash:
    def __init__(self, capacity):
        self.capacity = capacity
        self._contents = {}
 
    def add_item(self, item, qty=1):
        new_weight = self.total_weight() + item.weight * qty
        if new_weight > self.capacity:
            raise ValueError("Exceeded capacity")
        if item.item_id in self._contents:
            _, existing_qty = self._contents[item.item_id]
        else:
            existing_qty = 0
            
        self._contents[item.item_id] = (item, existing_qty + qty)
        
    def remove_item(self, item_id, qty=1):
        if item_id not in self._contents:
            raise ValueError("Item not found in stash")

        item_obj, existing_qty = self._contents[item_id]

        if qty > existing_qty:
            raise ValueError("Not enough items")

        new_qty = existing_qty - qty
        if new_qty == 0:
            del self._contents[item_id]
        else:
            self._contents[item_id] = (item_obj, new_qty)


    def total_weight(self):
        return sum(item.weight * qty for item, qty in self._contents.values())
 
    def __repr__(self):
        items_list = []
        for item, qty in self._contents.values():
            items_list.append(f"{item.name} x{qty}")

        content_str = ", ".join(items_list)

        return f"Stash: [{content_str}] ({self.total_weight()}/{self.capacity})"



potion = Item(1, "Health Potion", 0.5)
sword  = Item(2, "Iron Sword", 3.0)


stash = Stash(capacity=10.0)
stash.add_item(potion, 4)
stash.add_item(sword, 2)
print(stash)
stash.remove_item(1, 2)
print("Total weight:", stash.total_weight())
