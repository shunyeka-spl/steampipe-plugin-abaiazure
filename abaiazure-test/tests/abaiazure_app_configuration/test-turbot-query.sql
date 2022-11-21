select name, akas, title
from abaiazure.abaiazure_app_configuration
where name = '{{ resourceName }}' and resource_group = '{{ resourceName }}';
