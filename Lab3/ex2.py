class Patient:
    """
    Represents a patient in a hospital.
    
    This class manages patient information including personal details,
    medical diagnosis, and admission status.
    
    Attributes:
        name (str): The patient's full name.
        dob (str): The patient's date of birth in format 'YYYY-MM-DD'.
        id (int): The unique patient identifier.
        diagnosis (str): The patient's medical diagnosis.
        admitted (bool): Whether the patient is currently admitted. Defaults to False.

    Outsource:
    - docstrings 
    """
    
    def __init__(self, name: str, dob: str, id: int, diagnosis: str, admitted: bool = False):
        """
        Initialize a new Patient instance.
        
        Args:
            name (str): The patient's full name.
            dob (str): The patient's date of birth (format: 'YYYY-MM-DD').
            id (int): The unique patient identifier.
            diagnosis (str): The patient's medical diagnosis.
            admitted (bool, optional): Whether the patient is admitted. Defaults to False.
        
        Outsource:
        - docstrings
        """
        self.name = name
        self.dob = dob
        self.id = id
        self.diagnosis = diagnosis
        self.admitted = admitted 

    def admit(self):
        """
        Admit the patient to the hospital.
        
        Sets the patient's admission status to True, indicating they are
        currently admitted to the hospital.

        Outsource:
        - docstrings
        """
        self.admitted = True

    def discharge(self):
        """
        Discharge the patient from the hospital.
        
        Sets the patient's admission status to False, indicating they are
        no longer admitted to the hospital.

        Outsource:
        - docstrings
        """
        self.admitted = False

    def __str__(self):
        """
        Return a string representation of the patient.
        
        Returns:
            str: A formatted string containing the patient's ID, name, date of birth,
                 diagnosis, and admission status.
        Outsource:
        - docstrings
        """
        status = "Admitted" if self.admitted else "Not Admitted"
        return f"Patient ID: {self.id}\nName: {self.name}\nDate of Birth: {self.dob}\nDiagnosis: {self.diagnosis}\nStatus: {status}"
    


