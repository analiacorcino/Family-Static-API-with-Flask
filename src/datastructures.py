
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22],
        },
        
        
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3],
        },

        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1],
        }  
        
        ]



    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99)

    def add_member(self, member):
        # fill this method and update the return
        if not "id" in member:
            member["id"] = self._generateId()
        self._members.append({
        "id": member["id"],
        "first_name":  member["first_name"],
        "last_name": self.last_name,
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"],
        })
        return True


    def delete_member(self, id):
        # fill this method and update the return
       for item in self._members:
            if item["id"]== id:
                self._members.remove(item)
                return true
    
    def update_member(self, id, member):
       for item in self._members:
            
            if item ["id"] == id:
                
                if "first_name" in member:
                    item["first_name"] = member["first_name"]
                if "last_name" in member:
                    item["last_name"] = member["last_name"]
                if "age" in member:
                    item["age"] = member["age"]
                if "lucky_numbers" in member:
                    item["lucky_numbers"] = member["lucky_numbers"]
                return true


    def get_member(self, id):
       for item in self._members:
            if item["id"]== id:
                return item
                
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
