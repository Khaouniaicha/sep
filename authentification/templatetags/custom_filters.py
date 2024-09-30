from django import template

register = template.Library()

@register.filter
def media_url(media):
    if media.image:
        return media.image.url
    elif media.video:
        return media.video.url
    elif media.pdf:
        return media.pdf.url
    elif media.text:
        return media.text.url
    elif media.doc:
        return media.doc.url
    elif media.excel:
        return media.excel.url
    return ''
