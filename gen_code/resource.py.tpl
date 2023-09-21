# -*- coding: utf-8 -*-
{{ "" }}
{%- for resource in resource_list %}
from .srv.{{ resource.module_name }} import {{ resource.class_name }}
{%- endfor %}