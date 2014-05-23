from excercise.models import Application

def application(request):
    try:
        return {
            'APP': Application.current(),
        }
    except:
        return {
            'APP': 'CN'
        }
