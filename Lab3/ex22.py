from ex2 import Patient 

class Hospital:
    """
    A class to represent a hospital and manage patient records.
    
    Attributes:
        name (str): The name of the hospital.
        patients (list): A list of Patient objects currently in the hospital.

    Outsource:
    - docstrings
    """
    
    def __init__(self, name: str):
        """
        Initialize a Hospital object.
        
        Args:
            name (str): The name of the hospital. Must not be empty or None.
        
        Raises:
            ValueError: If the hospital name is empty or None.
        
        Outsource:
        - docstrings
        """
        if not name:
            raise ValueError(" Name must be written.")
        self.name = name
        self.patients = []

    def add_patient(self, patient_id:int):
        """
        Add a patient to the hospital.
        
        Args:
            patient_id (Patient): A Patient object to be added to the hospital.
        
        Raises:
            ValueError: If the patient_id is None or invalid.
        
        Outsource:
        - docstrings
        """
        if not patient_id:
            raise ValueError("Invalid patient.")
        self.patients.append(patient_id)

    def discharge_patient(self, patient_id: int):
        """
        Discharge a patient from the hospital by their ID.
        
        Args:
            patient_id (int): The ID of the patient to be discharged.
        
        Returns:
            str: A message indicating whether the patient was successfully discharged
                 or if the patient was not found.
        
        Outsource:
        - docstrings
        """
        for patient in self.patients:
            if patient.id == patient_id:
                self.patients.remove(patient)
                return f"Patient {patient_id} is discharged."
        return f"Patient {patient_id} not found."

    def get_patient_list(self):
        """
        Get a list of all admitted patients in the hospital.
        
        Returns:
            list: A list of Patient objects that are currently admitted 
                  (patient.admitted == True).
        Outsource:
        - docstrings
        """
        admitted_patients = []
        for patient in self.patients:
            if patient.admitted:
                admitted_patients.append(patient)
        return admitted_patients
    

    
