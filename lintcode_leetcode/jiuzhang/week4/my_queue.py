class my_queue:
    def __init__(self):
        self.elemets = []
        self.pointer = 0

    def add(self, e):
        self.elemets.append(e)

    def poll(self):
        if not self.elemets:
            return None
        self.pointer += 1
        return self.elemets[self.pointer - 1]

    def size(self):
        return len(self.elemets)

    def is_empty(self):
        return self.size() == 0