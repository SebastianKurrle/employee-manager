from .models import Employee


class EmployeeFilter:
    def __init__(self, filter_set, company):
        self.filter_set = filter_set
        self.company = company
        self.result = {}

    # filters the employees
    def filter(self):
        self.result = Employee.objects.filter(company=self.company)

        if 'first_name' in self.filter_set:
            self.result = self.result.filter(first_name__startswith=self.filter_set['first_name'])

        if 'last_name' in self.filter_set:
            self.result = self.result.filter(last_name__startswith=self.filter_set['last_name'])

        if 'salary_per_hour' in self.filter_set:
            self.result = self.result.filter(salary_per_hour=self.filter_set['salary_per_hour'])

        if 'hours_per_week' in self.filter_set:
            self.result = self.result.filter(hours_per_week=self.filter_set['hours_per_week'])

        if 'department' in self.filter_set:
            self.result = self.result.filter(department__startswith=self.filter_set['department'])

        return self.result

