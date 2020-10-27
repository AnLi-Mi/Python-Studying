class JobSite:
    def __init__(self, name, url, *jobs):
        self.name = name
        self.url = url
        self.jobs = jobs

    def __str__(self):
        return f'On {self.name} site are at the moment {len(self.jobs)} suitable job offers'


website1 = JobSite("BULLDOGJOB", "https://bulldogjob.pl/companies/jobs")
print (website1)
