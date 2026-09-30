# Repo mode: roast the evidence

When the user asks to roast their repo, codebase, PR, spec or pitch deck and you can read it, base the roast on what the files show. A roast citing `src/api/users.ts` is impossible to argue with; a generic one is easy to dismiss.

## Ground rules

- **Read-only.** Don't edit files, install dependencies, run migrations, start servers or commit anything. Reading files and running search / `git` read commands is enough.
- **Never print secret values.** If you find a key, token or password, cite the file and line and show it masked (`sk-...XXXX` → `sk-***`). Tell them to rotate it - once it's committed, deleting it is not enough.
- **Cite paths** (`path/to/file:line`) for every finding. No path, no claim.
- **Budget**: a quick sweep, not an audit. Around 10-20 cheap reads/searches, then write. For a large repo, sample the entry points, routes, auth and config.
- Absence of evidence isn't proof: say "I found no tests" rather than "you have no tests" when you only sampled.

## What to check (pick what fits the stack)

1. **Claims** - README, landing copy, pitch: "production-ready", "scalable", "secure", "enterprise". These set the WTF-meter: compare claims with evidence.
2. **Secrets** - tracked `.env` files (`git ls-files | grep -i env`), hard-coded keys (patterns like `sk-`, `AKIA`, `ghp_`, `xox`, `-----BEGIN`, `service_role`), keys shipped in frontend bundles or `NEXT_PUBLIC_` / `VITE_` variables that shouldn't be public.
3. **Access control** - API routes without auth checks; user IDs taken from the request body instead of the session; Supabase tables without RLS or `service_role` used client-side; Firebase rules like `allow read, write: if true`.
4. **Input handling** - SQL built by string concatenation, missing validation on request bodies, `dangerouslySetInnerHTML` / `v-html` with user content, file uploads without type/size limits.
5. **Money** - payment webhooks without signature verification, prices trusted from the client, no idempotency on charges.
6. **Tests and CI** - count test files vs source files; is there any CI config at all?
7. **Data safety** - migrations present or schema edited by hand? Any backup story? Destructive scripts without guards?
8. **Operability** - error handling that swallows errors, `console.log` as the only logging, no health check, no monitoring.
9. **AI-dump smell** - single files over ~1,000 lines, duplicated near-identical components, dead code, many `TODO` / `FIXME` / `HACK`, dependencies added but never imported.
10. **Git history** (optional) - one giant "init" commit or commits named "fix" x50 suggest nobody understands the code well enough to change it safely.

## Output

Same structure as the normal roast, with two changes:

- The "under the waterline" section becomes **"What your code actually says"**: 5-8 findings, each with a path and why it matters in production. Put anything that can leak data or money first.
- The way out is a **prioritized fix list**: what to fix today (secrets, access control), this week (tests on the core flow, validation), and before real users (monitoring, backups, legal).

If the code is genuinely solid for its stated scope, say so and score low. Roasting good work for sport is how the skill loses credibility.
