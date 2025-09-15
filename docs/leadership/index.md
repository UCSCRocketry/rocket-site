# Leadership Team

## Executive Leads

{% for lead in leads.executive %}

<div class="leader-card" onclick="openModal('{{ lead.id }}')">
  <img src="{{ lead.photo }}" alt="{{ lead.name }}">
  <h3>{{ lead.name }}</h3>
  <p class="position">{{ lead.position }}</p>
  <p class="short-bio">{{ lead.short_bio }}</p>
</div>

<div id="{{ lead.id }}" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal('{{ lead.id }}')">&times;</span>
    <img src="{{ lead.photo }}" alt="{{ lead.name }}">
    <h3>{{ lead.name }}</h3>
    <p><strong>{{ lead.position }}</strong></p>
    <p>{{ lead.long_bio }}</p>
    {% if lead.socials %}
    <div class="socials">
      {% for site, url in lead.socials.items() %}
        <a href="{{ url }}" target="_blank">{{ site|capitalize }}</a>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}

## Project Leads

{% for lead in leads.project %}

<div class="leader-card" onclick="openModal('{{ lead.id }}')">
  <img src="{{ lead.photo }}" alt="{{ lead.name }}">
  <h3>{{ lead.name }}</h3>
  <p class="position">{{ lead.position }}</p>
  <p class="short-bio">{{ lead.short_bio }}</p>
</div>

<div id="{{ lead.id }}" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal('{{ lead.id }}')">&times;</span>
    <img src="{{ lead.photo }}" alt="{{ lead.name }}">
    <h3>{{ lead.name }}</h3>
    <p><strong>{{ lead.position }}</strong></p>
    <p>{{ lead.long_bio }}</p>
    {% if lead.socials %}
    <div class="socials">
      {% for site, url in lead.socials.items() %}
        <a href="{{ url }}" target="_blank">{{ site|capitalize }}</a>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}

<script>
function openModal(id) {
    const modal = document.getElementById(id);
    if(modal) modal.style.display = 'block';
}

function closeModal(id) {
    const modal = document.getElementById(id);
    if(modal) modal.style.display = 'none';
}

window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
}
</script>
