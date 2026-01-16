# Add Web Design Guidelines Skill

Add Vercel's Web Interface Guidelines skill to a project. This skill enables AI-powered UI auditing for 100+ web design best practices.

## When to Use

Use this command when:
- Setting up a frontend project that needs UI quality checks
- Adding accessibility, performance, and UX auditing
- Reviewing existing UI code against best practices

## What It Adds

Creates a skill that can audit UI code for compliance with Web Interface Guidelines covering:

- **Accessibility** - aria-labels, semantic HTML, keyboard handlers
- **Focus States** - visible focus, focus-visible patterns
- **Forms** - autocomplete, validation, error handling
- **Animation** - prefers-reduced-motion, compositor-friendly transforms
- **Typography** - curly quotes, ellipsis, tabular-nums
- **Images** - dimensions, lazy loading, alt text
- **Performance** - virtualization, layout thrashing, preconnect
- **Navigation & State** - URL reflects state, deep-linking
- **Dark Mode & Theming** - color-scheme, theme-color meta
- **Touch & Interaction** - touch-action, tap-highlight
- **Locale & i18n** - Intl.DateTimeFormat, Intl.NumberFormat

## Generate

Create the following files:

### Skill File
`.cursor/skills/045-web-design-guidelines/SKILL.md` AND `.cursor/rules/045-web-design-guidelines.mdc`

**Frontmatter:**
```yaml
---
name: "045-web-design-guidelines"
description: "Web Interface Guidelines - 100+ UI best practices for accessibility, performance, and UX"
alwaysApply: true
---
```

**Content:**
```markdown
# Web Interface Guidelines

Reference for reviewing UI code against web best practices. Based on Vercel's Web Interface Guidelines.

## Quick Reference by Category

### Accessibility

- [ ] All interactive elements have accessible names (aria-label, aria-labelledby, or visible text)
- [ ] Images have alt text (decorative images use alt="")
- [ ] Form inputs have associated labels
- [ ] Focus order is logical (no tabindex > 0)
- [ ] Color alone doesn't convey meaning
- [ ] Sufficient color contrast (4.5:1 for text, 3:1 for large text)
- [ ] Interactive elements are keyboard accessible
- [ ] ARIA roles are used correctly (don't override native semantics)

### Focus States

- [ ] All focusable elements have visible focus indicators
- [ ] Use `:focus-visible` for keyboard-only focus (not mouse clicks)
- [ ] Focus trap is implemented for modals/dialogs
- [ ] Focus is restored when modal closes

```css
/* Focus visible pattern */
button:focus-visible {
  outline: 2px solid var(--focus-color);
  outline-offset: 2px;
}
```

### Forms

- [ ] Use appropriate input types (email, tel, url, number)
- [ ] Enable autocomplete with correct attributes
- [ ] Validation errors are announced to screen readers
- [ ] Required fields are marked and announced
- [ ] Error messages are specific and actionable

```html
<input
  type="email"
  autocomplete="email"
  required
  aria-describedby="email-error"
/>
<p id="email-error" role="alert">Please enter a valid email</p>
```

### Animation

- [ ] Respect `prefers-reduced-motion`
- [ ] Use compositor-friendly transforms (transform, opacity)
- [ ] Avoid animating layout properties (width, height, margin)
- [ ] Animation duration is appropriate (150-500ms for UI)

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

/* Compositor-friendly animation */
.animate {
  transform: translateX(0);
  transition: transform 200ms ease-out;
}
.animate.active {
  transform: translateX(100px);
}
```

### Typography

- [ ] Use curly quotes (" " ' ') not straight quotes
- [ ] Use proper ellipsis (…) not three dots (...)
- [ ] Use tabular-nums for aligned numbers
- [ ] Line height is readable (1.4-1.6 for body text)
- [ ] Maximum line length is controlled (65-75 characters)

```css
.numbers {
  font-variant-numeric: tabular-nums;
}

.prose {
  max-width: 65ch;
  line-height: 1.6;
}
```

### Images

- [ ] All images have explicit width and height (prevents CLS)
- [ ] Use lazy loading for below-the-fold images
- [ ] Use srcset for responsive images
- [ ] Use WebP/AVIF with fallbacks
- [ ] Decorative images use aria-hidden="true"

```tsx
<Image
  src="/hero.jpg"
  alt="Hero image description"
  width={1200}
  height={600}
  loading="lazy" // or priority for above-fold
  sizes="(max-width: 768px) 100vw, 50vw"
/>
```

### Performance

- [ ] Use virtualization for long lists (>100 items)
- [ ] Avoid layout thrashing (batch DOM reads and writes)
- [ ] Use preconnect for third-party origins
- [ ] Critical CSS is inlined
- [ ] JavaScript is deferred or lazy loaded

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://cdn.example.com" crossorigin />
```

### Navigation & State

- [ ] URL reflects current state (shareable links)
- [ ] Browser back/forward works correctly
- [ ] Deep linking is supported
- [ ] Loading states are shown for navigation
- [ ] 404 pages are helpful

### Dark Mode & Theming

- [ ] color-scheme meta tag is set
- [ ] theme-color meta tag updates with theme
- [ ] System preference is detected
- [ ] User preference is persisted
- [ ] No flash of wrong theme on load

```html
<meta name="color-scheme" content="light dark" />
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0a0a0a" />
```

### Touch & Interaction

- [ ] Touch targets are at least 44x44px
- [ ] touch-action is set appropriately
- [ ] No tap delay (touch-action: manipulation)
- [ ] Pull-to-refresh is handled if needed

```css
button, a, [role="button"] {
  min-width: 44px;
  min-height: 44px;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
```

### Locale & i18n

- [ ] Use Intl.DateTimeFormat for dates
- [ ] Use Intl.NumberFormat for numbers/currency
- [ ] Language is declared in HTML
- [ ] RTL layouts are supported if needed
- [ ] Pluralization is handled correctly

```tsx
const formatter = new Intl.DateTimeFormat('en-US', {
  dateStyle: 'medium',
  timeStyle: 'short'
})

const currencyFormatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD'
})
```

## Review Command

To run a full UI review, use the `/review-ui` command which will:
1. Fetch the latest guidelines
2. Read specified files
3. Check against all rules
4. Output findings in `file:line` format

## Reference

For the complete guidelines, fetch:
```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```
```

### Review UI Command
`.cursor/commands/review-ui.md`

**Content:**
```markdown
# Review UI

Review UI code for Web Interface Guidelines compliance.

## Usage

Provide files or patterns to review:
- Single file: `src/components/Button.tsx`
- Pattern: `src/components/**/*.tsx`
- Current file: (no argument)

## Process

1. Fetch latest guidelines from:
   ```
   https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
   ```

2. Read the specified files

3. Check against all rules in the fetched guidelines

4. Output findings in format:
   ```
   file:line - [Category] Issue description
   ```

## Categories

- Accessibility
- Focus States
- Forms
- Animation
- Typography
- Images
- Performance
- Navigation & State
- Dark Mode & Theming
- Touch & Interaction
- Locale & i18n

## Example Output

```
src/components/Button.tsx:15 - [Accessibility] Button missing accessible name
src/components/Input.tsx:23 - [Forms] Missing autocomplete attribute
src/components/Modal.tsx:45 - [Focus States] Missing focus trap
```

## Severity Levels

- 🔴 **Critical** - Accessibility violations, broken functionality
- 🟠 **High** - UX issues, performance problems
- 🟡 **Medium** - Best practice violations
- 🟢 **Low** - Nice to have improvements
```

## Integration

This skill integrates with:
- `080-code-review` - UI-specific review points
- `check-performance.md` - Performance validation
- Framework-specific patterns (React, Next.js)

Start by asking: "Add Web Design Guidelines to this project? (yes/no)"
