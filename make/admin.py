from django.contrib import admin
from .models import Make

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)







# Hi, I’m a seasoned Ruby on Rails developer with 8 years of hands-on experience building robust, secure, and scalable web applications. My journey began with simple CRUD apps and evolved into architecting complex SaaS platforms, RESTful APIs, background job systems, and highly optimized admin dashboards. From startups to enterprise environments, I’ve delivered value across the board—writing clean code, improving system performance, and mentoring junior developers along the way.

# My skillset extends well beyond Rails. I’m equally comfortable with PostgreSQL, Sidekiq, Redis, RSpec, and integrating third-party services like Stripe, AWS S3, and SendGrid. I follow SOLID principles, use service objects and form objects to keep code modular, and always think two steps ahead in terms of maintainability.

# I’ve worked in Agile teams, collaborated with product managers, designers, and QA testers, and even led sprints when needed. Whether building APIs for a React frontend, optimizing ActiveRecord queries, or setting up CI/CD pipelines with Docker and GitHub Actions, I take pride in doing the work that just works—and scales.

# Some highlights of my work include:

# Building a multi-tenant architecture SaaS tool that served 50,000+ users

# Migrating legacy Rails 4 code to Rails 7 with zero downtime

# Reducing background job latency by 70% by rearchitecting Sidekiq queues

# Mentoring 5+ junior developers who now independently own features

# What sets me apart is my focus on product thinking—I don’t just write code, I care about the why. I understand how code decisions impact the business and the user, and I always aim for solutions that are elegant under the hood and delightful on the surface.

# Now, I’m exploring new challenges, ideally at a company that values craftsmanship, clean architecture, and a collaborative engineering culture. If you're looking for someone who can hit the ground running and elevate your Rails stack with confidence and care—I’d love to connect.    