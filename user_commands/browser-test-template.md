# Browser Test Command Template

This template is used by init commands to generate the `/browser-test` command for frontend projects.

## Generated Command

`.cursor/commands/browser-test.md`

**Content:**
```markdown
# Browser Test

Run browser testing after code changes. This is Phase 4 of the TDD workflow.

## Quick Start

```bash
# Start dev server
npm run dev

# Or production preview
npm run build && npm run start  # Next.js
npm run build && npm run preview  # Vite
```

## Checklist

### Core Checks (Always)
- [ ] Open changed pages in browser
- [ ] Check DevTools Console - no errors/warnings
- [ ] Check DevTools Network - no failed requests
- [ ] Test main user interactions

### Viewport Testing
- [ ] Desktop (1280px+)
- [ ] Tablet (768px-1024px)
- [ ] Mobile (< 640px)

Use DevTools → Toggle Device Toolbar (Ctrl+Shift+M / Cmd+Shift+M)

### Performance Checks
- [ ] Test with slow network (Network → Slow 3G)
- [ ] Check for layout shifts during load
- [ ] Verify loading states appear

### Interaction Testing
- [ ] Click all buttons/links on changed pages
- [ ] Submit forms with valid data
- [ ] Submit forms with invalid data (check error states)
- [ ] Test keyboard navigation (Tab, Enter, Escape)

### Data Flow Testing
- [ ] Data loads correctly
- [ ] Mutations update UI (create, update, delete)
- [ ] Optimistic updates work
- [ ] Error states display correctly
- [ ] Empty states display correctly

## Quick Commands

```bash
# Open browser with DevTools
# Chrome
open -a "Google Chrome" --args --auto-open-devtools-for-tabs http://localhost:3000

# Firefox
firefox --devtools http://localhost:3000
```

## Report Template

After testing, document:
```markdown
## Browser Test Report
- **Pages Tested:** [list]
- **Viewports:** desktop ✅, tablet ✅, mobile ✅
- **Console Errors:** none / [list issues]
- **Network Issues:** none / [list issues]
- **Interactions:** all working / [list issues]
```

## When to Run

**MANDATORY after:**
- Component changes
- Styling changes
- Data fetching changes
- Routing changes
- State management changes
- Form changes
- Animation changes

**SKIP for:**
- Utility function only
- Type definitions only
- Test files only
- Documentation only
```

## Customization by Project Type

### Next.js Projects
Add to checklist:
- [ ] Server Components render correctly (no hydration mismatch)
- [ ] Server Actions execute (check Network for POST to same URL)
- [ ] Streaming/Suspense boundaries work
- [ ] Metadata/SEO tags are correct (View Page Source)

### React SPA Projects
Add to checklist:
- [ ] SWR/React Query cache works (check Network for deduplication)
- [ ] Route transitions are smooth
- [ ] Browser back/forward works
- [ ] Deep links work (refresh on nested route)

### Fullstack Projects
Add to checklist:
- [ ] Database operations complete
- [ ] Authentication flow works
- [ ] Protected routes redirect correctly
- [ ] API responses are correct
