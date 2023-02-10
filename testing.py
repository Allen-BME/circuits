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
        self.resistors = dict()
    def add_resistor(self, resistance, wires):
        """
        add resistor to circuit.
        @param resistance: resistance of resistor
        @param wires: tuple of wires resistor is connected to. must be 2 unique wires.
        """
        wires = frozenset(wires)
        r = _Resistor(resistance=resistance, wires=wires)
        if wires not in self.resistors.keys():
            self.resistors[wires] = []
        self.resistors[wires].append(r)
    def print(self):
        """
        display circuit in human readable format
        """
        print(f"Voltage source {self.ps_voltage} V, connected to wires {self.ps_wires}")
        for wire_set in self.resistors:
            for r in self.resistors[wire_set]:
                print(r)
    def combine_all_parallel_resistors(self):
        """
        combine every resistor with the same wire set (parallel resistors)
        """
        for wire_set in self.resistors:
            if len(self.resistors[wire_set]) > 1:
                req = equivalent_resistor_parallel([r for r in self.resistors[wire_set]], wire_set)
                self.resistors[wire_set] = [req]
    def find_equivalent_resistor(self):
        """
        combine all resistors in the circuit into 1 equivalent resistor
        """


class _Resistor():
    """
    Hidden class representing resistor circuit component
    """
    def __init__(self, resistance: float, wires):
        self.resistance = resistance
        if (type(wires) != set) and (len(wires) != 2):
            raise Exception("Resistor wires must be 2 element set")
        self.wires = wires
    def __repr__(self):
        return f"Resistor: {self.resistance:.2f} Ohms connected to wires {self.wires}"
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

def equivalent_resistor_series(resistors, wires):
    resistances = [r.resistance for r in resistors]
    return _Resistor(sum(resistances), wires)

def equivalent_resistor_parallel(resistors, wires):
    inv_resistances = [1/r.resistance for r in resistors]
    return _Resistor(1 / sum(inv_resistances), wires)



# driver
if __name__ == "__main__":
    circuit = ResistorCircuit(ps_voltage=120)
    circuit.add_resistor(10, {1,2})
    circuit.add_resistor(20, {1,2})
    circuit.add_resistor(30, {1,3})
    circuit.add_resistor(30, {1,3})
    circuit.add_resistor(40, {2,1})
    circuit.add_resistor(50, {2,3})
    circuit.print()

    circuit.combine_all_parallel_resistors()
    circuit.print()
