from django import template

register = template.Library()


def format_flag_class(language):
    return {
        'en': 'us',
        'ja': 'jp',
    }.get(language, language)

@register.inclusion_tag('flag.html')
def flag_by_language(language):

    flag_class = format_flag_class(language)

    return {
        'name': language,
        'class': flag_class
    }
