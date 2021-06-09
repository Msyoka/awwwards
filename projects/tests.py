from django.test import TestCase
from .models import Projects, Profile, Votes
from django.contrib.auth.models import User

# Create your tests here
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'mumo' ,email = 'daviemumo37@gmail.com', password = 'col12')
        self.profile = Profile(image = '', user = self.user, bio ='Doc code',)
        
        
    def test_save_profile(self):
        self.user.save()
        self.profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()


class ProjectsTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    # Set up method
    def setUp(self):
        self.user = User(username = 'mumo' ,email = 'daviemumo37@gmail.com', password = 'col12')
        self.user.save()

        self.profile = Profile(image = '/path/jefflogo.svg' ,user = self.user, bio = "Doc code")
        self.profile.save()

        self.project = Projects(name = 'gram37', image = '', description = 'insta clone', link = '')
        self.project.save()

        # Creating a new project
        self.project.profile.user.add(self.profile)
    
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()
        

class VotesTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'mumo', email = 'daviemumo37@gmail.com', password = 'col12')
        self.user.save()

        self.profile = Profile(image = '' ,user = self.user, bio = "")
        self.profile.save()

        self.project = Projects(name = 'Testing', image = '/path/jefflogo.svg', description = 'Project one', link = '/path/jefflogo.svg')
        self.project.save()

        self.vote = Votes(design = '7', usability = '7', content = '6', user=self.user, project = 'Testing')
        self.vote.save_vote()from django.test import TestCase
from .models import Projects, Profile, Votes
from django.contrib.auth.models import User

# Create your tests here
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'mumo' ,email = 'daviemumo37@gmail.com', password = 'col12')
        self.profile = Profile(image = '', user = self.user, bio ='doctor',)
        
        
    def test_save_profile(self):
        self.user.save()
        self.profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()


class ProjectsTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    # Set up method
    def setUp(self):
        self.user = User(username = 'mumo' ,email = 'daviemumo37@gmail.com', password = 'col12')
        self.user.save()

        self.profile = Profile(image = '' ,user = self.user, bio = "I love coding")
        self.profile.save()

        self.project = Projects(name = 'gram37', image = '', description = 'insta clone', link = '')
        self.project.save()

        # Creating a new project
        self.project.profile.user.add(self.profile)
    
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()
        

class VotesTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'mumo', email = 'daviemumo37@gmail.com', password = 'col12')
        self.user.save()

        self.profile = Profile(image = '' ,user = self.user, bio = "")
        self.profile.save()

        self.project = Projects(name = 'gram37', image = '', description = 'Project one', link = '')
        self.project.save()

        self.vote = Votes(design = '7', usability = '7', content = '6', user=self.user, project = 'Testing')
        self.vote.save_vote()