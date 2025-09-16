# Alumni

{% for lead in leads.unc %}

<div class="lead-card">
  <img src="../../assets/team/{{ lead.id }}.webp" alt="{{ lead.name }}">
  <div class="lead-info">
    <h3>{{ lead.name }}</h3>
    <p class="position">{{ lead.position }}</p>
    <p class="short-bio">{{ lead.short_bio }}</p>

    {% if lead.socials %}
    <div class="socials">
      {% if lead.socials.linkedin %}
        <a href="{{ lead.socials.linkedin }}" target="_blank">

<span style="width:24px; height:24px; display:inline-block; vertical-align:middle;">
  <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="linkedin"
       class="svg-inline--fa fa-linkedin fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 448 512" style="width:100%; height:100%;">
    <path fill="currentColor"
      d="M100.28 448H7.4V148.9h92.88zm-46.44-340.6C24 107.4 0 83.35 0 54.2 0 25 24 0 53.84 0 83.64 0 107 25 107 54.2c0 29.1-23.36 53.2-53.16 53.2zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.2-79.2-48.3 0-55.7 37.7-55.7 76.7V448h-92.68V148.9h88.98v40.8h1.3c12.4-23.5 42.68-48.2 87.86-48.2 94 0 111.4 61.9 111.4 142.3V448z">
    </path>
  </svg>
</span>

      </a>
    {% endif %}
    {% if lead.socials.github %}
      <a href="{{ lead.socials.github }}" target="_blank">

<span style="width:24px; height:24px; display:inline-block; vertical-align:middle;">
  <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="github"
       class="svg-inline--fa fa-github fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 496 512" style="width:100%; height:100%;">
    <path fill="currentColor"
      d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-2.9 0-5.2-1.6-5.2-3.6
         0-2 2.3-3.6 5.2-3.6 2.9 0 5.2 1.6 5.2 3.6zm-33.2-9.4c-.7
         1.6 1 3.4 3.8 4.1 2.7.7 5.5-.1 6.2-1.7.7-1.6-1-3.4-3.8-4.1
         -2.8-.7-5.5.1-6.2 1.7zm44.8-1.7c-2.9.8-4.9 2.6-4.7 4.1.3
         1.5 2.8 2 5.7 1.2 2.9-.8 4.9-2.6 4.7-4.1-.3-1.5-2.8-2-5.7-1.2zm55
         23.6c-2.8.9-4.6 2.8-4 4.1.6 1.3 3.3 1.6 6.1.7 2.8-.9 4.6-2.8
         4-4.1-.6-1.3-3.3-1.6-6.1-.7zM248 8C111 8 0 119 0 256c0
         110.3 71.3 204.1 170.2 237.2 12.4 2.3 16.9-5.4 16.9-12v-44c-69.2
         15-83.9-33.5-83.9-33.5-11.3-28.7-27.6-36.3-27.6-36.3-22.5-15.4
         1.7-15.1 1.7-15.1 24.9 1.7 38 25.6 38 25.6 22.1 37.8 58 26.9
         72.2 20.5 2.2-15.9 8.7-26.9 15.8-33.1-55.3-6.3-113.4-27.6-113.4-122.9
         0-27.2 9.7-49.5 25.6-66.9-2.6-6.3-11.1-31.7 2.4-66.2 0 0 20.9-6.7
         68.5 25.5 19.9-5.5 41.2-8.2 62.4-8.3 21.2.1 42.5 2.8 62.4 8.3
         47.6-32.2 68.5-25.5 68.5-25.5 13.5 34.5 5 59.9 2.4 66.2 15.9
         17.4 25.6 39.7 25.6 66.9 0 95.5-58.2 116.5-113.6 122.7 8.9
         7.7 16.9 22.9 16.9 46.2v68.5c0 6.6 4.4 14.3 17 12C424.7
         460.1 496 366.3 496 256 496 119 385 8 248 8z">
    </path>
  </svg>
</span>

      </a>
    {% endif %}
    {% if lead.socials.website %}
      <a href="{{ lead.socials.website }}" target="_blank">

<span style="width:24px; height:24px; display:inline-block; vertical-align:middle;">
  <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="globe"
       class="svg-inline--fa fa-globe fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 496 512" style="width:100%; height:100%;">
    <path fill="currentColor"
      d="M248 8C111 8 0 119 0 256s111 248 248 248
         248-111 248-248S385 8 248 8zm149.6 187.7c-6.8
         15.3-32.5 46.7-64.5 78.5-9.8 10-19.9 19.4-29.9
         28.1-27.2 23.4-53.3 41.7-63.7 46.8-10.5 5.2-14.1
         5.1-24.6 0-10.5-5.2-36.5-23.4-63.7-46.8-10-8.7-20.1-18.1-29.9-28.1-32-31.8-57.7-63.2-64.5-78.5-6.8-15.3-5.1-25.8 4.8-25.8h283.7c9.8 0 11.6 10.5 4.8 25.8z">
    </path>
  </svg>
</span>

        </a>
      {% endif %}
    </div>
    {% endif %}

</div>
</div>

{% endfor %}
