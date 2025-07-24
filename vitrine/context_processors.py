from .models import JobOffer

def job_offers_context(request):
    has_active_job_offers = JobOffer.objects.filter(is_active=True).exists()
    return {'has_active_job_offers': has_active_job_offers}
