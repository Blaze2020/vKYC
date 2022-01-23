Jinja Template
https://jinja2docs.readthedocs.io/en/stable/

Using template inheritance:
{% extends 'about.html'
{% block content %}
    {% for item in data %}
        <h1>{{ item.Name }}</h1>
        <p>{{ item.Profession }}</p>
        <p>{{ item.Age }}</p>
        <p>{{ item.Aim }}</p>
    {% endfor %}
{% endblock content %}{% extends 'about.html' %}

Injecting it into:parent tempalte (about.html)

Flashing messages
{% with messages = get_flashed_messages() %}
            {% if messages %}

                {% for message in messages %}
                    <p>{{ message }}</p>
                {% endfor %}

            {% endif %}
        {% endwith %},
