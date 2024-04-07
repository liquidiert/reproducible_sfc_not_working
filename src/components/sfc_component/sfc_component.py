from django_components import component
from django_components import types as t

@component.register("sfc-component")
class SFCComponent(component.Component):
    
    def get_context_data(self)-> component.Dict[str, component.Any]:
        return {}
    
    template: t.django_html = """
        <div class="container bg-green-200 mx-auto">Hi from sfc!</div>
    """