from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    typed_text_strings = models.CharField(max_length=255, help_text="Comma-separated strings for typed text effect")
    description = models.TextField()
    cv_link = models.URLField(blank=True, null=True)
    
    # Contact Info
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100)
    
    # Social Links
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    
    # Profile Info
    status_label = models.CharField(max_length=50, default="Available for opportunities")
    open_to_work = models.BooleanField(default=True)
    experience_summary = models.CharField(max_length=100)
    education_summary = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AboutCard(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="e.g., fas fa-network-wired")
    icon_color_class = models.CharField(max_length=100, help_text="e.g., text-accent")
    border_color_code = models.CharField(max_length=50, help_text="e.g., #6366f1 or empty for default accent", blank=True, null=True)
    bg_color_class = models.CharField(max_length=100, help_text="e.g., bg-blue-50 dark:bg-blue-950/50")
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Highlight(models.Model):
    text = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text

class Statistic(models.Model):
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    color_class = models.CharField(max_length=100, help_text="e.g., text-accent")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    data_cat = models.CharField(max_length=50, unique=True, help_text="e.g., routing")
    is_active_default = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="e.g., fas fa-microchip")
    icon_color_class = models.CharField(max_length=100, help_text="e.g., text-accent")
    level = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., Advanced")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category__order', 'order']

    def __str__(self):
        return self.name

class ProjectTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="e.g., fas fa-network-wired")
    icon_color_class = models.CharField(max_length=100, help_text="e.g., text-accent/60")
    gradient_from = models.CharField(max_length=100, help_text="e.g., from-blue-50 dark:from-blue-950/40")
    gradient_to = models.CharField(max_length=100, help_text="e.g., to-indigo-50 dark:to-indigo-950/40")
    github_link = models.URLField(blank=True, null=True)
    duration_text = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., 2024 - 2025 · 6 Months")
    tags = models.ManyToManyField(ProjectTag, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class VisitorLog(models.Model):
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self):
        return f"{self.ip_address} - {self.path} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
