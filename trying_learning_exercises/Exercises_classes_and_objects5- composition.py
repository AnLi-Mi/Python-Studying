class JobSite:
    def __init__(self, name, url, *jobs):
        self.name = name
        self.url = url
        self.jobs = jobs

    def __str__(self):
        return f'On {self.name} site are at the moment {len(self.jobs)} suitable job offers'

    def harvest_job_elements(self):
        pass

# bulldogsite is an object because there is not many bulldogsites to create a child class of it

class Job:
    def __init__(self):
        pass

    def add_details(self, title, company, salary, technology, location):
        self.title = title
        self.company = company
        self. salary = salary
        self.technology = technology
        self.location = location
    
    def __str__(self): # it doesn't work if add_detials wasn't executed
        return f'Position {self.title!r} at {self.company}\n Salary: {self.salary}\n Technology: {self.technology}\n Location: {self.location}'


job1 = Job()
job2 = Job()
job3 = Job()

job1.add_details("Backend Developer", "Intel", 10000, "Python", "Gdańsk")
job2.add_details("Frontend Developer", "Pyszne.pl", 8000, "JavaScript", "Warszawa")
job3.add_details("Fullstack Developer", "Unit8", 12000, "Ruby, HTML", "Wrocław")

print(job1)
print(job2)
print(job3)

website1 = JobSite("BULLDOGJOB", "https://bulldogjob.pl/companies/jobs", job1, job2, job3)
print (website1)

for job in website1.jobs:
    print (job)

