# Custom Field Types Reference

Reference for specialized and advanced ACF field types.

## Link Field

Stores URL with optional title and target:

```json
{
  "key": "field_cta_link",
  "label": "CTA Link",
  "name": "cta_link",
  "type": "link",
  "return_format": "array"
}
```

Returns:
```php
array(
  'title' => 'Click Here',
  'url' => 'https://example.com',
  'target' => '_blank'
)
```

## Gallery Field

Multiple images with order:

```json
{
  "key": "field_gallery",
  "label": "Image Gallery",
  "name": "gallery",
  "type": "gallery",
  "return_format": "array",
  "insert": "append",
  "library": "all",
  "min": 0,
  "max": 12,
  "preview_size": "medium"
}
```

## Google Map Field

Location picker with coordinates:

```json
{
  "key": "field_location",
  "label": "Location",
  "name": "location",
  "type": "google_map",
  "center_lat": "40.7128",
  "center_lng": "-74.0060",
  "zoom": 14
}
```

Returns:
```php
array(
  'address' => 'New York, NY',
  'lat' => 40.7128,
  'lng' => -74.0060
)
```

## oEmbed Field

Embed videos/content from URLs:

```json
{
  "key": "field_video",
  "label": "Video",
  "name": "video",
  "type": "oembed",
  "width": "",
  "height": ""
}
```

Supports: YouTube, Vimeo, Twitter, etc.

## Color Picker

```json
{
  "key": "field_brand_color",
  "label": "Brand Color",
  "name": "brand_color",
  "type": "color_picker",
  "default_value": "#0073aa",
  "enable_opacity": 1,
  "return_format": "string"
}
```

## Button Group

Multiple choice as buttons:

```json
{
  "key": "field_alignment",
  "label": "Text Alignment",
  "name": "alignment",
  "type": "button_group",
  "choices": {
    "left": "Left",
    "center": "Center",
    "right": "Right"
  },
  "default_value": "left",
  "layout": "horizontal",
  "return_format": "value"
}
```

## Range Slider

Numeric value with visual slider:

```json
{
  "key": "field_opacity",
  "label": "Opacity",
  "name": "opacity",
  "type": "range",
  "default_value": 100,
  "min": 0,
  "max": 100,
  "step": 5,
  "prepend": "",
  "append": "%"
}
```

## Accordion Field

Organize fields visually (no data stored):

```json
{
  "key": "field_accordion_content",
  "label": "Content Settings",
  "name": "",
  "type": "accordion",
  "open": 1,
  "multi_expand": 0,
  "endpoint": 0
}
```

End accordion with:
```json
{
  "key": "field_accordion_end",
  "label": "Accordion End",
  "name": "",
  "type": "accordion",
  "endpoint": 1
}
```

## Tab Field

Create tabbed interface (no data stored):

```json
{
  "key": "field_tab_content",
  "label": "Content",
  "name": "",
  "type": "tab",
  "placement": "top"
}
```

## Message Field

Display instructions/info (no data):

```json
{
  "key": "field_instructions",
  "label": "Instructions",
  "name": "",
  "type": "message",
  "message": "Fill in the hero section content below",
  "new_lines": "wpautop",
  "esc_html": 0
}
```

## Post Object

Select WordPress posts:

```json
{
  "key": "field_related_post",
  "label": "Related Post",
  "name": "related_post",
  "type": "post_object",
  "post_type": ["post"],
  "taxonomy": [],
  "allow_null": 1,
  "multiple": 0,
  "return_format": "object",
  "ui": 1
}
```

## Relationship Field

Select multiple posts with search:

```json
{
  "key": "field_featured_posts",
  "label": "Featured Posts",
  "name": "featured_posts",
  "type": "relationship",
  "post_type": ["post"],
  "filters": ["search", "post_type", "taxonomy"],
  "elements": ["featured_image"],
  "min": 0,
  "max": 6,
  "return_format": "object"
}
```

## Taxonomy Field

Select taxonomy terms:

```json
{
  "key": "field_categories",
  "label": "Categories",
  "name": "categories",
  "type": "taxonomy",
  "taxonomy": "category",
  "field_type": "checkbox",
  "add_term": 1,
  "save_terms": 0,
  "load_terms": 0,
  "return_format": "id",
  "multiple": 0
}
```

## User Field

Select WordPress users:

```json
{
  "key": "field_author",
  "label": "Author",
  "name": "author",
  "type": "user",
  "role": ["author", "editor"],
  "allow_null": 0,
  "multiple": 0,
  "return_format": "array"
}
```

## Best Practices

1. Use appropriate field types for better UX
2. Set `return_format` consistently across project
3. Use Link field instead of separate URL + text fields
4. Use Button Group for 2-5 options (better than select)
5. Use Accordion/Tab to organize long forms
6. Add Message fields for complex sections
7. Consider relationship fields for content connections