from django.shortcuts import render


def index(request, chart_data, html_file, active_name):
    content = {
        "chart_data": chart_data,
        "active_name": active_name
    }

    return render(request, html_file, content)
