
---
name: acf-local-json
description: Generate Advanced Custom Fields (ACF) Local JSON configurations for WordPress from visual designs or HTML structures. Use when creating ACF field groups, converting designs to ACF schemas, building WordPress custom fields from mockups, or when working with ACF Pro Local JSON format. Supports flexible content, repeaters, clone fields, and all ACF field types.
metadata:
  author: josecortezz25
  version: "1.0"
  source: https://airbnb.com
---

# ACF Local JSON Builder

Generate complete ACF (Advanced Custom Fields) Local JSON configurations from images, designs, or HTML structures for WordPress development.

## Core Workflow

1. **Analyze Input**: Examine the provided image, design, or HTML structure
2. **Identify Components**: Detect repeating patterns, content sections, and field relationships
3. **Map Field Types**: Determine appropriate ACF field types for each component
4. **Generate JSON**: Create the complete Local JSON configuration
5. **Validate Structure**: Ensure proper nesting, keys, and field relationships

## Field Type Detection Guidelines

### From Visual Analysis

- **Text inputs/headings** → `text`, `textarea`, or `wysiwyg`
- **Images** → `image` (consider `gallery` for multiple)
- **Repeating cards/sections** → `repeater` or `flexible_content`
- **Toggle states** → `true_false` or `button_group`
- **Dropdowns/select boxes** → `select` or `radio`
- **Date displays** → `date_picker` or `date_time_picker`
- **Links/buttons** → `link` or `url`
- **Color variations** → `color_picker`
- **File downloads** → `file`
- **Numbered lists** → `number` or `range`
- **Tab interfaces** → `tab` field type
- **Accordions** → `flexible_content` with layouts

### From HTML Structure

```html
<!-- Text Field -->
<h1>, <h2>, <p> → text/textarea/wysiwyg

<!-- Image Field -->
<img> → image field
<picture>, <source> → image with return format 'array'

<!-- Repeater Pattern -->
<div class="card"> (múltiples) → repeater
<ul><li> (dinámicos) → repeater

<!-- Flexible Content Pattern -->
Secciones variadas (hero, features, cta) → flexible_content

<!-- Link Field -->
<a href=""> → link field

<!-- True/False -->
<input type="checkbox"> → true_false
```

## JSON Structure Template

Every ACF Local JSON file follows this structure:

```json
{
  "key": "group_unique_identifier",
  "title": "Field Group Name",
  "fields": [...],
  "location": [...],
  "menu_order": 0,
  "position": "normal",
  "style": "default",
  "label_placement": "top",
  "instruction_placement": "label",
  "hide_on_screen": "",
  "active": true,
  "description": ""
}
```

## Field Structure Patterns

### Basic Field
```json
{
  "key": "field_unique_key",
  "label": "Field Label",
  "name": "field_name",
  "type": "text",
  "instructions": "",
  "required": 0,
  "conditional_logic": 0,
  "wrapper": {
    "width": "",
    "class": "",
    "id": ""
  },
  "default_value": "",
  "placeholder": "",
  "prepend": "",
  "append": "",
  "maxlength": ""
}
```

### Repeater Field
```json
{
  "key": "field_repeater_key",
  "label": "Items",
  "name": "items",
  "type": "repeater",
  "instructions": "",
  "required": 0,
  "layout": "block",
  "button_label": "Add Item",
  "min": 0,
  "max": 0,
  "sub_fields": [
    {
      "key": "field_subfield_key",
      "label": "Title",
      "name": "title",
      "type": "text",
      "parent": "field_repeater_key"
    }
  ]
}
```

### Flexible Content
```json
{
  "key": "field_flexible_key",
  "label": "Page Builder",
  "name": "page_builder",
  "type": "flexible_content",
  "instructions": "",
  "button_label": "Add Section",
  "min": "",
  "max": "",
  "layouts": {
    "layout_hero": {
      "key": "layout_hero_key",
      "name": "hero",
      "label": "Hero Section",
      "display": "block",
      "sub_fields": [...]
    },
    "layout_features": {
      "key": "layout_features_key",
      "name": "features",
      "label": "Features Section",
      "display": "block",
      "sub_fields": [...]
    }
  }
}
```

### Image Field
```json
{
  "key": "field_image_key",
  "label": "Image",
  "name": "image",
  "type": "image",
  "return_format": "array",
  "preview_size": "medium",
  "library": "all",
  "min_width": "",
  "min_height": "",
  "min_size": "",
  "max_width": "",
  "max_height": "",
  "max_size": "",
  "mime_types": ""
}
```

## Key Generation Rules

1. **Group Keys**: `group_` + descriptive_snake_case + random_hash
   - Example: `group_homepage_hero_5f8a2b`

2. **Field Keys**: `field_` + descriptive_snake_case + random_hash
   - Example: `field_hero_title_9c3d1e`

3. **Layout Keys**: `layout_` + layout_name + random_hash
   - Example: `layout_hero_section_4b7e9a`

4. **Uniqueness**: Every key must be globally unique across all ACF installations

## Location Rules

Common location patterns:

```json
"location": [
  [
    {
      "param": "post_type",
      "operator": "==",
      "value": "page"
    }
  ]
]
```

```json
"location": [
  [
    {
      "param": "page_template",
      "operator": "==",
      "value": "template-homepage.php"
    }
  ]
]
```

```json
"location": [
  [
    {
      "param": "post_type",
      "operator": "==",
      "value": "post"
    },
    {
      "param": "post_category",
      "operator": "==",
      "value": "category:news"
    }
  ]
]
```

## Best Practices

1. **Semantic Naming**: Use clear, descriptive names that reflect content purpose
2. **Proper Nesting**: Maintain correct parent-child relationships in repeaters/flex
3. **Return Formats**: Choose appropriate return formats (ID, array, url for images)
4. **Instructions**: Add helpful instructions for content editors
5. **Defaults**: Set sensible default values where appropriate
6. **Validation**: Include min/max constraints where relevant
7. **Layout Types**: Use `block`, `table`, or `row` layouts appropriately
8. **Clone Fields**: Reference the clone fields documentation for reusable field sets

## Output Format

Generate the complete JSON file ready to save as:
```
acf-json/group_[name].json
```

The file should be valid JSON and immediately usable in WordPress ACF Pro's Local JSON feature.

## Advanced Features

For complex patterns like:
- **Clone fields**: See `references/clone-fields.md`
- **Bidirectional relationships**: See `references/relationships.md`
- **Custom field types**: See `references/custom-types.md`
- **Conditional logic**: See `references/conditional-logic.md`

## Example Workflow

**User provides**: Screenshot of a hero section with title, subtitle, CTA button, and background image

**Analysis**:
1. Hero section = Field Group
2. Title = text field
3. Subtitle = textarea field
4. CTA = link field (text + URL)
5. Background = image field

**Output**: Complete JSON with all fields properly structured and nested
