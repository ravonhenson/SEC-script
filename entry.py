class Entry:
    def __init__(self, accession_number, entity, form, is_material, summary,
                 dollar_amt, record_count, customers_affected) -> None:
        self._accession_number = accession_number
        self._entity = entity
        self._form = form
        self._is_material = is_material
        self._summary = summary
        self._dollar_amt = dollar_amt
        self._record_count = record_count
        self._customers_affected = customers_affected

    def to_string(self):
        return ",".join(map(str, vars(self).values())) #???
    
    def return_list(self):
        return list(vars(self).values())
    
    # Getter and Setter for accession_number
    @property
    def accession_number(self):
        return self._accession_number

    @accession_number.setter
    def accession_number(self, accession_number):
        self._accession_number = accession_number

    # Getter and Setter for entity
    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, entity):
        self._entity = entity

    # Getter and Setter for form
    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, form):
        self._form = form

    # Getter and Setter for summary
    @property
    def summary(self):
        return self._summary
    
    @summary.setter
    def summary(self, summary):
        self._summary = summary

    # Getter and Setter for is_material
    @property
    def is_material(self):
        return self._is_material

    @is_material.setter
    def is_material(self, is_material):
        self._is_material = is_material

    # Getter and Setter for dollar_amt
    @property
    def dollar_amt(self):
        return self._dollar_amt

    @dollar_amt.setter
    def dollar_amt(self, dollar_amt):
        self._dollar_amt = dollar_amt

    # Getter and Setter for record_count
    @property
    def record_count(self):
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        self._record_count = record_count

    # Getter and Setter for customers_affected
    @property
    def customers_affected(self):
        return self._customers_affected

    @customers_affected.setter
    def customers_affected(self, customers_affected):
        self._customers_affected = customers_affected
