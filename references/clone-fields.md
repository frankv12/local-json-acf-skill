# Clone Fields Reference

Clone fields allow you to reuse field configurations across multiple field groups, reducing duplication and maintaining consistency.

## Basic Clone Field

```json
{
  "key": "field_clone_key",
  "label": "Common Fields",
  "name": "common_fields",
  "type": "clone",
  "clone": [
    "group_shared_fields_key"
  ],
  "display": "seamless",
  "layout": "block",
  "prefix_label": 0,
  "prefix_name": 0
}
```

## Display Options

### Seamless
Fields appear as if they belong directly to the parent group:
```json
"display": "seamless"
```

### Group
Fields appear grouped under a label:
```json
"display": "group"
```

### Block
Each field appears in its own block:
```json
"display": "block"
```

## Prefix Options

Control whether cloned field names/labels inherit prefixes:

```json
"prefix_label": 0,  // Don't prefix labels
"prefix_name": 0    // Don't prefix field names
```

```json
"prefix_label": 1,  // Prefix labels with clone field label
"prefix_name": 1    // Prefix names with clone field name
```

## Common Use Cases

### Shared SEO Fields
```json
{
  "key": "field_seo_clone",
  "label": "SEO",
  "name": "seo",
  "type": "clone",
  "clone": ["group_seo_fields"],
  "display": "group",
  "prefix_label": 0,
  "prefix_name": 0
}
```

### Reusable CTA Section
```json
{
  "key": "field_cta_clone",
  "label": "Call to Action",
  "name": "cta",
  "type": "clone",
  "clone": ["group_cta_fields"],
  "display": "seamless"
}
```

### Multiple Field Groups
```json
{
  "key": "field_combined_clone",
  "type": "clone",
  "clone": [
    "group_seo_fields",
    "group_social_fields",
    "group_analytics_fields"
  ],
  "display": "seamless"
}
```

## Best Practices

1. Create a dedicated field group for commonly cloned fields
2. Use `seamless` display for invisible integration
3. Set `prefix_name: 0` to maintain consistent field names
4. Clone entire groups rather than individual fields when possible
5. Document which groups are meant to be cloned