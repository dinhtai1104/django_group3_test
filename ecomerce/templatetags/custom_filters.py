
#Filter

from django.template.defaulttags import register
@register.filter
def roundValue(value):
   return round(value)

@register.filter
def getLength(value):
   return len(value)

#End Filter