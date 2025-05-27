from django.shortcuts import render

# Liste de services en dur (tu peux plus tard passer à une base de données)
SERVICES = [
    {"titre": "Systèmes informatiques", "description": "Solutions complètes pour votre infrastructure informatique."},
    {"titre": "Réseau & Télécoms", "description": "Installation et maintenance des réseaux et télécommunications."},
    {"titre": "Sécurité électronique", "description": "Surveillance, contrôle d’accès et vidéosurveillance."},
    {"titre": "Transformation digitale", "description": "Accompagnement vers la digitalisation et l’innovation."},
]

def index(request):
    """
    Page d'accueil, affiche la liste complète des services.
    """
    return render(request, 'vitrine/index.html', {'services': SERVICES})

def search_services(request):
    """
    Recherche simple dans la liste des services.
    """
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        query_lower = query.lower()
        results = [
            service for service in SERVICES
            if query_lower in service['titre'].lower() or query_lower in service['description'].lower()
        ]
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'vitrine/search_results.html', context)

def services(request):
    return render(request, 'vitrine/services.html')

def about(request):
    return render(request, 'vitrine/about.html')

def contact(request):
    return render(request, 'vitrine/contact.html')
