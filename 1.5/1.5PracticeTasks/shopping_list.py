class ShoppingList():
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} has been added to {self.list_name}")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} has been removed from {self.list_name}")
        else:
            print(f"{item} is not in list {self.list_name}")
    
    def view_list(self):
        print(f"{self.list_name} list includes: ")
        for item in self.shopping_list:
            print(item)

    def merge_lists(self, obj):
        merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)
        merged_lists_obj = ShoppingList(merged_lists_name)
        merged_lists_obj.shopping_list = self.shopping_list.copy()
        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)
        return merged_lists_obj
            


pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.add_item('bone')
pet_store_list.add_item('dog food')
pet_store_list.add_item('treats')
pet_store_list.add_item('ball')
pet_store_list.add_item('collar')

pet_store_list.remove_item('collar')

pet_store_list.view_list()