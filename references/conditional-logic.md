# Conditional Logic Reference

Conditional logic allows fields to appear or hide based on the values of other fields.

## Basic Conditional Logic

```json
{
  "key": "field_website_url",
  "label": "Website URL",
  "name": "website_url",
  "type": "url",
  "conditional_logic": [
    [
      {
        "field": "field_has_website",
        "operator": "==",
        "value": "1"
      }
    ]
  ]
}
```

This field only appears when `field_has_website` is checked (true).

## Operators

### Equality Operators
- `==` - Equal to
- `!=` - Not equal to

### Comparison Operators
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal
- `<=` - Less than or equal

### Pattern Matching
- `contains` - Contains substring
- `!contains` - Does not contain

### Existence
- `empty` - Field is empty
- `!empty` - Field has value

## AND Logic (Multiple Conditions)

All conditions in the same array must be true:

```json
"conditional_logic": [
  [
    {
      "field": "field_type",
      "operator": "==",
      "value": "premium"
    },
    {
      "field": "field_status",
      "operator": "==",
      "value": "active"
    }
  ]
]
```

## OR Logic (Alternative Conditions)

Any group can be true (separate arrays):

```json
"conditional_logic": [
  [
    {
      "field": "field_type",
      "operator": "==",
      "value": "premium"
    }
  ],
  [
    {
      "field": "field_type",
      "operator": "==",
      "value": "enterprise"
    }
  ]
]
```

## Complex Example

Show field if:
- (Type is premium AND status is active) OR
- (Type is trial AND days < 30)

```json
"conditional_logic": [
  [
    {
      "field": "field_type",
      "operator": "==",
      "value": "premium"
    },
    {
      "field": "field_status",
      "operator": "==",
      "value": "active"
    }
  ],
  [
    {
      "field": "field_type",
      "operator": "==",
      "value": "trial"
    },
    {
      "field": "field_trial_days",
      "operator": "<",
      "value": "30"
    }
  ]
]
```

## Common Patterns

### Show/Hide Based on Checkbox
```json
"conditional_logic": [
  [
    {
      "field": "field_enable_feature",
      "operator": "==",
      "value": "1"
    }
  ]
]
```

### Show Based on Select Value
```json
"conditional_logic": [
  [
    {
      "field": "field_layout_type",
      "operator": "==",
      "value": "custom"
    }
  ]
]
```

### Show if Field Has Value
```json
"conditional_logic": [
  [
    {
      "field": "field_title",
      "operator": "!empty"
    }
  ]
]
```

### Show if Multiple Checkboxes
```json
"conditional_logic": [
  [
    {
      "field": "field_option_a",
      "operator": "==",
      "value": "1"
    },
    {
      "field": "field_option_b",
      "operator": "==",
      "value": "1"
    }
  ]
]
```

## In Flexible Content Layouts

Conditional logic works within flexible content sub-fields:

```json
{
  "key": "layout_hero",
  "name": "hero",
  "label": "Hero Section",
  "sub_fields": [
    {
      "key": "field_style",
      "label": "Style",
      "name": "style",
      "type": "select",
      "choices": {
        "default": "Default",
        "video": "Video Background"
      }
    },
    {
      "key": "field_video_url",
      "label": "Video URL",
      "name": "video_url",
      "type": "url",
      "conditional_logic": [
        [
          {
            "field": "field_style",
            "operator": "==",
            "value": "video"
          }
        ]
      ]
    }
  ]
}
```

## Best Practices

1. Keep conditions simple and readable
2. Reference fields by their unique `key`, not `name`
3. Test edge cases (what happens when condition field is empty)
4. Document complex conditional logic
5. Avoid circular dependencies
6. Use select/radio fields for clearer logic than checkboxes