class People:
    """
    This class is the representation of a Person.
    """

    def __init__(self, name: str):
        """
        Constructor of the class People.py

        Parameters
        ----------
        name : str
            Name of the person.
        """
        self.name = name  # the name of the People

    @property
    def getName(self):
        """
        Return the name of the People.py.
        """
        return self.name
