# Bidirectional Relationships Reference

Configure relationships that automatically update both connected posts.

## Basic Bidirectional Setup

When Post A selects Post B, Post B automatically shows Post A in its relationship field.

### Post Type A Field
```json
{
  "key": "field_related_products",
  "label": "Related Products",
  "name": "related_products",
  "type": "relationship",
  "post_type": ["product"],
  "bidirectional": 1,
  "bidirectional_target": ["field_related_posts"]
}
```

### Post Type B Field
```json
{
  "key": "field_related_posts",
  "label": "Related Blog Posts",
  "name": "related_posts",
  "type": "relationship",
  "post_type": ["post"],
  "bidirectional": 1,
  "bidirectional_target": ["field_related_products"]
}
```

## Symmetric Relationships

Same post type, both directions:

```json
{
  "key": "field_related_posts",
  "label": "Related Posts",
  "name": "related_posts",
  "type": "relationship",
  "post_type": ["post"],
  "bidirectional": 1,
  "bidirectional_target": ["field_related_posts"]
}
```

## Multiple Bidirectional Fields

One field can sync with multiple target fields:

```json
{
  "key": "field_team_members",
  "label": "Team Members",
  "name": "team_members",
  "type": "relationship",
  "post_type": ["person"],
  "bidirectional": 1,
  "bidirectional_target": [
    "field_projects",
    "field_departments"
  ]
}
```

## With Post Object Field

Works with single selections too:

```json
{
  "key": "field_featured_in",
  "label": "Featured In",
  "name": "featured_in",
  "type": "post_object",
  "post_type": ["page"],
  "bidirectional": 1,
  "bidirectional_target": ["field_featured_posts"]
}
```

## Common Use Cases

### Products ↔ Posts
```json
// In Product CPT
{
  "key": "field_product_related_posts",
  "name": "related_posts",
  "type": "relationship",
  "post_type": ["post"],
  "bidirectional": 1,
  "bidirectional_target": ["field_post_related_products"]
}

// In Post
{
  "key": "field_post_related_products",
  "name": "related_products",
  "type": "relationship",
  "post_type": ["product"],
  "bidirectional": 1,
  "bidirectional_target": ["field_product_related_posts"]
}
```

### Team Members ↔ Projects
```json
// In Person CPT
{
  "key": "field_person_projects",
  "name": "projects",
  "type": "relationship",
  "post_type": ["project"],
  "bidirectional": 1,
  "bidirectional_target": ["field_project_team"]
}

// In Project CPT
{
  "key": "field_project_team",
  "name": "team_members",
  "type": "relationship",
  "post_type": ["person"],
  "bidirectional": 1,
  "bidirectional_target": ["field_person_projects"]
}
```

### Courses ↔ Prerequisites
```json
{
  "key": "field_course_prerequisites",
  "label": "Prerequisites",
  "name": "prerequisites",
  "type": "relationship",
  "post_type": ["course"],
  "bidirectional": 1,
  "bidirectional_target": ["field_course_unlocks"]
},
{
  "key": "field_course_unlocks",
  "label": "Unlocks Courses",
  "name": "unlocks",
  "type": "relationship",
  "post_type": ["course"],
  "bidirectional": 1,
  "bidirectional_target": ["field_course_prerequisites"]
}
```

## Important Notes

1. **Field Keys**: Use field keys in `bidirectional_target`, not field names
2. **Post Types**: Target field must allow the source post type
3. **Multiple Targets**: Array of field keys for multiple connections
4. **Auto Updates**: Changes sync automatically on save
5. **No Loops**: ACF prevents infinite update loops

## Best Practices

1. Use clear, semantic names for both directions
2. Document the relationship purpose
3. Set appropriate min/max values
4. Consider UI impact (many relationships = slow interface)
5. Use filters to limit selectable posts
6. Add instructions for content editors

## Advanced Pattern: Hub and Spoke

Central hub with multiple connection types:

```json
// In Hub (Project)
{
  "key": "field_project_team",
  "name": "team",
  "type": "relationship",
  "post_type": ["person"],
  "bidirectional": 1,
  "bidirectional_target": ["field_person_projects"]
},
{
  "key": "field_project_resources",
  "name": "resources",
  "type": "relationship",
  "post_type": ["resource"],
  "bidirectional": 1,
  "bidirectional_target": ["field_resource_projects"]
}

// In Person
{
  "key": "field_person_projects",
  "name": "projects",
  "type": "relationship",
  "post_type": ["project"],
  "bidirectional": 1,
  "bidirectional_target": ["field_project_team"]
}

// In Resource
{
  "key": "field_resource_projects",
  "name": "projects",
  "type": "relationship",
  "post_type": ["project"],
  "bidirectional": 1,
  "bidirectional_target": ["field_project_resources"]
}
```