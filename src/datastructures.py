
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

        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["lastname"] = self.last_name
        if "id" not in member : member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]['id'] == id:
                aux = self._members[i]
                del self._members[i]
                return aux
        return {"msg" : "done"}

    def get_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]['id'] == id:
                return self._members[i]
        return {"msg" : "Id not found"}

    def get_all_members(self):
        return self._members