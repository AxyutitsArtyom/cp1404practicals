class Band:

    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        members_info = ", ".join([str(member) for member in self.members])
        return f"{self.name} ({members_info})"

    def add(self, member):
        self.members.append(member)

    def play(self):
        return "\n".join([member.play() for member in self.members])
