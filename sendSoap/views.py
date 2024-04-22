import requests
from django.shortcuts import render

def envoyer_xml(request):
    api_url = 'http://dneonline.com/calculator.asmx?WSDL'
    resultat = None

    if request.method == 'POST':
        xml_code = request.POST.get('xml_code')


        import requests

        if request.POST.get('action') == 'envoyer':
            headers = {
                'Content-Type': 'text/xml',
                'Authorization': ''
            }
            response = requests.post(api_url, data=xml_code, headers=headers)

            if response.status_code == 200:
                resultat = response.text
            else:
                resultat = f"La requête a échoué avec le code d'état {response.status_code}"

    return render(request, 'envoyer_xml.html', {'resultat': resultat})
