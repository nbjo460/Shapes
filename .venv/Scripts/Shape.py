from abc import ABC, abstractmethod

class Shape (ABC):
    def init(self):
        self.name = "VIRTUAL SHAPE"
    @abstractmethod
    def get_area (self):
        pass
    def __str__(self):
        return "This shape is: " + self.name
