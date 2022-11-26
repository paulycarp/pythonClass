# Suppose we want to get the number of tags in a lblog
# Creating custom containers

class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag: str) -> None:
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    
    # Reading Tags
    def __getitem__(self, tag: str) -> int:
        return self.tags.get(tag.lower(), 0)

    # Set Item
    def __setitem__(self, tag: str, count: int) -> None:
        self.tags[tag.lower()] = count

    # Length
    def __len__(self) -> int:
        return len(self.tags)
    
    # Making iterabel
    def __iter__(self) -> object:
        return iter(self.tags)