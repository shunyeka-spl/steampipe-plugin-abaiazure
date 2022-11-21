select name, id, type, region
from abaiazure.abaiazure_app_configuration
where name = 'dummy-test{{ resourceName }}' and resource_group = '{{ resourceName }}';
