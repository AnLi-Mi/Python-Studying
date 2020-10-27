class JobSite:
    def __init__(self, name, url, *jobs):
        self.name = name
        self.url = url
        self.jobs = jobs

    def __str__(self):
        return f'On {self.name} site are at the moment {len(self.jobs)} suitable job offers'


website1 = JobSite("BULLDOGJOB", "https://bulldogjob.pl/companies/jobs")
print (website1)


class Job:
    def __init__(self, title, company, salary, technology, location):
        self.title = title
        self.company = company
        self. salary = salary
        self.technology = technology
        self.location = location

    def __str__(self):
        return f'Position {self.title!r} at {self.company}\n Salary: {self.salary}\n Technology: {self.technology}\n Location: {self.location}'


job1 = Job ("Backend Developer", "Intel", 10000, "Python", "Gdańsk")
job2 = Job ("Frontend Developer", "Pyszne.pl", 8000, "JavaScript", "Warszawa")
job3 = Job ("Fullstack Developer", "Unit8", 12000, "Ruby, HTML", "Wrocław")

print(job1)
print(job2)
print(job3)
