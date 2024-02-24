class StudentGroup:
    def __init__(self, group, idGroup):
        self.group = group
        self.idGroup = idGroup


    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getIdGroup(self):
        return self.idGroup

    def setIdGroup(self, idGroup):
        self.idGroup = idGroup

    def __str__(self):
        return "StudentGroup{" + "group=" + str(self.group) + ", idGroup=" + str(self.idGroup) + "}"

    def __iter__(self):
        return iter(self.group)