class Solution:
    """Represent a chemical solution.

    Attributes: 
    name : str
        The name of the solute (e.g. "NaCl").
    concentration : float
        Concentration in mg/mL (must be > 0).
    volume : float
        Volume in mL (must be > 0).

    Methods: 
    add(other)
        Mix another Solution of the same `name` into this one (updates in-place).
    dilute(factor)
        Reduce concentration by `factor` (updates in-place).
    """

    def __init__(self, name, concentration, volume):
        """Initialize a Solution.

        Parameters: 
        name : str
            Name of the solute.
        concentration : float
            Concentration in mg/mL; must be greater than 0.
        volume : float
            Volume in mL; must be greater than 0.

        Raises: 
        - ValueError: If `concentration` or `volume` is not greater than 0.
        """
        if concentration <= 0:
            raise ValueError("Concentration must be greater than 0")
        if volume <= 0:
            raise ValueError("Volume must be greater than 0")

        self.name = name
        self.concentration = concentration
        self.volume = volume

    def __str__(self):
        """Return a human-readable representation of the solution."""
        return f"Solution: {self.name}, {self.concentration:.2f} mg/mL, {self.volume:.2f} mL"

    def add(self, other):
        """Mix another Solution into this one.

        The method updates this Solution in-place by computing the total
        solute mass from both solutions and dividing by the new total volume.

        Parameters: 
        other : Solution
            Another Solution instance with the same `name`.

        Raises: 
        - ValueError: If `other.name` is different from `self.name`.
        """
        if self.name != other.name:
            raise ValueError("Cannot mix different substances!")

        total_mass_self = self.concentration * self.volume
        total_mass_other = other.concentration * other.volume

        new_volume = self.volume + other.volume
        new_concentration = (total_mass_self + total_mass_other) / new_volume

        self.concentration = new_concentration
        self.volume = new_volume

    def dilute(self, factor):
        """Dilute the solution by the given factor (in-place).

        Parameters: 
        factor : float
            The dilution factor; must be greater than 0. For example,
            factor=2 halves the concentration.

        Raises: 
        - ValueError: If `factor` is not greater than 0.
        """
        if factor <= 0:
            raise ValueError("Dilution factor must be greater than 0")
        self.concentration /= factor

    def __eq__(self, other):
        """Equality: same solute `name` and same `concentration`.

        Note: `volume` is intentionally ignored for equality checks.
        """
        return (self.name == other.name) and (self.concentration == other.concentration)

if __name__ == "__main__":
    s1 = Solution("NaCl", 5.0, 20.0)
    s2 = Solution("NaCl", 1.0, 15.0)
    print(s1)
    s1.add(s2)
    print("After mixing:", s1)
    s1.dilute(2)
    print("After diluting by 2:", s1)
    s3 = Solution("NaCl", s1.concentration, s1.volume)
    print("s1 == s3:", s1 == s3)
