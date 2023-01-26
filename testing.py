class ResistorCircuit():
    """
    Class representing circuit with resistors.
    Circuit may have only 1 power source.
    """

    def __init__(self, ps_voltage, ps_wires=(1,2)):
        """
        initialize circuit with no resistors
        @param ps_voltage: the voltage of the power source
        @param ps_wires: tuple of the wires the power source is connected to. must be 2 unique wires.
            default --> (1,2), (positive terminal, negative terminal)
        """
        self.ps_voltage = ps_voltage
        self.ps_wires = ps_wires
        self.resistors = []
    def add_resistor(self, resistance, wires):
        """
        add resistor to circuit.
        @param resistance: resistance of resistor
        @param wires: tuple of wires resistor is connected to. must be 2 unique wires.
        """
        r = _Resistor(resistance=resistance, wires=wires)
        self.resistors.append(r)
    def print(self):
        """
        display circuit in human readable format
        """
        print(f"Voltage source {self.ps_voltage} V, connected to wires {self.ps_wires}")
        for r in self.resistors:
            print(f"Resistor {r.resistance} ohms, connected to wires {r.wires}")


class _Resistor():
    """
    Hidden class representing resistor circuit component
    """
    def __init__(self, resistance: float, wires):
        self.resistance = resistance
        self.wires = wires
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

def equivalent_resistor_series(resistors):
    resistances = [r.resistance for r in resistors]
    return Resistor(sum(resistances))

def equivalent_resistor_parallel(resistors):
    inv_resistances = [1/r.resistance for r in resistors]
    return Resistor(1 / sum(inv_resistances))



# driver
if __name__ == "__main__":
    circuit = ResistorCircuit(ps_voltage=120)
    circuit.add_resistor(10, (1,2))
    circuit.add_resistor(20, (2,3))
    circuit.print()
