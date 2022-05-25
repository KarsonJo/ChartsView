"""ChartsView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .myviews.chart_view import index

# (display_name, html_content, route_path)
chart_datas_bag = [
    ('Q1 1', 'map_zone.html', 'map_zone'),
    ('Q1 2', 'pie_zone.html', 'pie_zone'),
    ('Q3', 'pie_device.html', 'pie_device'),
    ('Q4', 'pie_function.html', 'pie_function'),
    ('Q6 Q7', 'line_time_concentration.html', 'line_time_concentration'),
    ('Q8 Q2', 'line_grade_accompany.html', 'line_grade_accompany'),
    ('Q9', 'pie_class.html', 'pie_class'),
    ('Q10', 'pie_content.html', 'pie_content'),
    ('Q11', 'pie_solution.html', 'pie_solution'),
    ('Q12 Q7', 'line_interact_concentration.html', 'line_interact_concentration'),
    ('Q13', 'pie_problem.html', 'pie_problem'),
    ('Q14', 'pie_action.html', 'pie_action'),
    ('Q15', 'pie_ability.html', 'pie_ability'),
    ('Q16', 'bar_satisfaction.html', 'bar_satisfaction'),
    ('Q17', 'bar_advantage.html', 'bar_advantage'),
    ('Q18', 'bar_disadvantage.html', 'bar_disadvantage'),
    ('Q19', 'pie_expectation.html', 'pie_expectation'),
    ('Q20 Q2 1', 'bar_grade_interest.html', 'bar_grade_interest'),
    ('Q20 Q2 2', 'line_grade_interest.html', 'line_grade_interest')]


def index_with_data(datas, item_index):
    datas_filtered = [(data[0], data[2]) for data in datas]
    return lambda x: index(x, datas_filtered, datas[item_index][1], datas[item_index][0])


urlpatterns = []
for i in range(0, len(chart_datas_bag)):
    urlpatterns.append(
        path(f'{chart_datas_bag[i][2]}/',
             index_with_data(chart_datas_bag, i),
             name=f'{chart_datas_bag[i][2]}'))

urlpatterns.append(path('',
                        lambda x: index(x,
                                        [(data[0], data[2]) for data in chart_datas_bag],
                                        'index.html',
                                        ''),
                        name='index'))
