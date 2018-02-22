from django.shortcuts import render


def main(request, tag_slug=None):
    return render(request, 'try.html')

