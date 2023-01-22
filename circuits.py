class Resistor():
    """
    Class representing resistor circuit component
    """

    def __init__(self, resistance: float):
        self.resistance = resistance
    def __repr__(self):
        return f"Resistor: {self.resistance} Ohms"
    def __sub__(self, other):
        """
        - symbolizes resistors in series
        e.g. Req_series = R1 - R2
        """
        return equivalent_resistor_series([self, other])
    def __floordiv__(self, other):
        """
        // symbolizes resistors in parallel
        e.g. Req_parallel = R1 // R2
        """
        return equivalent_resistor_parallel([self, other])

class ResistorArray():
    """
    Class representing a collection of resistors
    """
    def __init__(self, resistances):
        self.resistors = [Resistor(r) for r in resistances]
    def __getitem__(self, key):
        return self.resistors[key - 1]
    def equivalent_series(self):
        return equivalent_resistor_series(self.resistors)
    def equivalent_parallel(self):
        return equivalent_resistor_parallel(self.resistors)

def equivalent_resistor_series(resistors):
    resistances = [r.resistance for r in resistors]
    return Resistor(sum(resistances))

def equivalent_resistor_parallel(resistors):
    inv_resistances = [1/r.resistance for r in resistors]
    return Resistor(1 / sum(inv_resistances))



# driver
if __name__ == "__main__":
    R = ResistorArray([5, 3, 4, 1, 2])
    Req = ((R[3] - R[4]) // R[2]) - R[1] - R[5]
    print(Req)
    
