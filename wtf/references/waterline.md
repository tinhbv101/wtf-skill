# What's under the waterline

The work nobody films for the "built it in an hour" clip. Choose 5-8 items that fit **the exact product the user named**: start with its archetype section, fill gaps from the cross-cutting lists, and restate each item in concrete terms in the user's language instead of copying these lines.

## Contents
- By archetype: social / messaging, marketplace / ride-hailing / delivery, e-commerce, fintech / payments, B2B SaaS, accounting / ERP, AI apps, "replace the team with AI"
- Cross-cutting: engineering, security and safety, business and operations
- Legal by target market

## By archetype

### Social network / messaging
- **Feed ranking** - not `ORDER BY created_at`. ML ranking, A/B tests, years of behavioral data
- **Fan-out** - a celebrity posts once and that post has to appear in millions of feeds almost instantly
- **Real-time** - websockets, presence, reconnects, message ordering, delivery receipts, offline queues
- **Moderation** - fraud, gore, child sexual abuse material, fake news; you are legally on the hook for what stays up
- **Bots** - the sign-up form goes live and bot farms find it within days
- **Media** - upload, compression, video transcoding, storage and bandwidth bills
- **Cold start** - a social network without your friends in it is an empty database
- **End-to-end encryption** (messaging) - key exchange, multi-device, backups - cryptography you cannot vibe-code safely

### Marketplace / ride-hailing / delivery
- **Chicken-and-egg** - no sellers/drivers, no buyers/riders, and vice versa. Supply is recruited by hand, city by city
- **Real-time dispatch** - matching, ETAs, live location, re-assignment when a driver cancels
- **Dynamic pricing** - surge, promotions, driver incentives, and the abuse each one invites
- **Driver / seller KYC** - identity, licenses, vehicle checks, background checks
- **Money flows** - split payments, payouts, cash on delivery reconciliation, refunds, chargebacks
- **Safety incidents** - accidents, harassment, lost items, insurance; someone must answer the phone at 2 a.m.
- **Fraud** - fake trips, GPS spoofing, promo abuse, collusion between drivers and riders

### E-commerce
- **Flash sales** - millions of concurrent requests for the same item; overselling the last unit
- **Inventory consistency** - two people buying the last item, stock across warehouses
- **Logistics** - shipping partners, tracking, failed deliveries, returns, COD
- **Counterfeits and seller fraud** - fake reviews, fake products, trademark complaints
- **Tax invoices** - e-invoices per order in markets that require them
- **Search and recommendations** - language-specific search (diacritics, CJK tokenization), typos, ranking

### Fintech / payments / e-wallet
- **Licensing** - holding customer money or moving it usually needs a license; without one, the product is illegal, not "MVP"
- **KYC / AML** - identity verification, sanctions screening, suspicious transaction reporting
- **Ledger correctness** - double-entry, idempotency, reconciliation to the cent; a rounding bug is someone's money
- **Security** - PCI DSS for card data, fraud detection, account takeover
- **Bank integrations** - every partner bank has its own API, cut-off times and failure modes

### B2B SaaS
- **Multi-tenancy** - tenant A must never see tenant B's data; one missing `WHERE tenant_id = ?` is a breach
- **Billing** - plans, proration, trials, dunning, taxes, invoices, refunds
- **Roles and permissions** - admins, members, guests, per-object sharing
- **Enterprise asks** - SSO/SAML, audit logs, data export, SLA, security questionnaires, SOC 2 / ISO 27001
- **Integrations** - every customer wants Slack, Google, their ERP, a webhook, an API with rate limits
- **Migrations** - customers' data must survive every schema change

### Accounting / ERP / invoicing
- **Regulation is the product** - charts of accounts, accounting regimes, tax filing formats defined by the government, changing year to year
- **E-invoices** - formats, digital signatures, transmission to the tax authority, cancellation/adjustment rules
- **Correctness** - books must balance; errors become penalties for the customer
- **Data retention** - accounting records must be kept for years; losing them is not an option
- **Support** - accountants call at the filing deadline, every quarter, all at once
- **Integrations** - banks, e-invoice providers, tax portals, payroll, social insurance

### AI apps / "clone ChatGPT"
- **The model is not yours** - the "clone" calls someone else's API; your margin is their price minus your costs, and they can ship your feature next month
- **Inference cost** - every message costs money; a free tier with heavy users can burn more than revenue
- **Training your own model** - frontier models take billions of dollars of compute, massive datasets and research teams; not a weekend
- **Rate limits and outages** - provider limits, latency spikes, model deprecations that change behavior overnight
- **Hallucinations and liability** - wrong medical, legal or financial answers with your name on them
- **Evals** - without a test set you can't tell whether a prompt change made things better or worse
- **Prompt injection and abuse** - users jailbreaking it, leaking the system prompt, using it for spam; content filters
- **Privacy** - user data sent to a third-party model provider, data retention, enterprise customers asking where it goes

### "Replace the whole dev team with AI"
- **Someone still decides** what to build, reviews what AI wrote and owns it when it breaks
- **Code you don't understand** can't be debugged at 3 a.m. and can't be defended in a security review
- **AI-generated security holes** - leaked keys, missing access checks, outdated dependencies - look fine until exploited
- **Accountability** - customers, regulators and investors want a human who answers for the system

## Cross-cutting

### Engineering
- **Scale** - one tester on localhost tells you nothing about a million people at once: caching, queues, sharding, CDNs
- **Data consistency** - double charges, lost orders, race conditions
- **Mobile** - iOS + Android, store review, old versions in the wild, push notifications
- **Monitoring** - without logs, metrics and alerts, users find the outage before you do
- **Backups you've actually restored** - one lost database and nobody trusts you with data again

### Security and safety
- **Accounts** - sign-in, reset flows, 2FA, social login, session expiry, rate-limiting password guesses
- **Classic holes** - injection, XSS, secrets pasted into generated code, and the favourite: changing an ID in the URL shows someone else's data
- **Abuse of money flows** - fake orders, review farms, coupon farming, chargebacks

### Business and operations
- **Distribution** - shipping is the cheap part; getting strangers to show up is the expensive part
- **Support** - a customer's payment vanished at midnight; whose phone rings?
- **On-call** - prod falls over at 3 a.m. and the coding assistant is not on the rota
- **Maintenance** - tech debt compounds, especially in code nobody on the team understands
- **Cloud bill** - unoptimised generated code plus auto-scaling can cost more than the product earns
- **Offline operations** - drivers, warehouses, couriers, sellers, accountants: real humans, not promptable
- **IP** - copy a famous brand's name, logo or screens and expect a cease-and-desist
- **Fundraising** - early investors fund teams and traction, not demos

## Legal by target market

Choose by **where the product will run**, not by the language of the message. Treat these as prompts to go check, not as legal advice.

### Vietnam
- **Personal data**: Law on Personal Data Protection No. 91/2025/QH15, in force since 1 Jan 2026 (guided by Decree 356/2025, which replaced Decree 13/2023). Fines up to 5% of prior-year revenue for cross-border transfer violations, up to 10x the proceeds for trading personal data; 72-hour breach reporting. Collecting emails on a landing page already counts
- **Social networks**: Decree 147/2024 (effective 25 Dec 2024) - accounts must be verified by Vietnamese phone number before they can post, comment or livestream; social networks also need a license
- **E-wallets and payment intermediaries**: Decree 52/2024 (effective 1 Jul 2024) - an SBV license and at least VND 50 billion charter capital; e-wallets must hold a payment-assurance balance covering all wallet balances. No license means partner with a licensed provider, not "launch and see"
- **E-invoices**: mandatory for all businesses since 1 Jul 2022 (Law on Tax Administration 38/2019, Decree 123/2020, amended by Decree 70/2025 from 1 Jun 2025 - household businesses with revenue of VND 1 billion or more need cash-register e-invoices connected to the tax authority)
- **Accounting regimes**: Circular 99/2025/TT-BTC replaced Circular 200/2014 for fiscal years from 1 Jan 2026; SMEs still commonly use Circular 133/2016. Household businesses lost lump-sum ("khoán") tax from 1 Jan 2026 (Resolution 198/2025) and now self-declare tax on actual revenue - the rules an accounting app must encode change almost every year
- **Transport / delivery**: ride-hailing and delivery fall under transport business rules - vehicles and drivers are regulated
- Source (checked Sep 2026): PDPL 91/2025 and its fines - Ministry of Public Security (bocongan.gov.vn), VnEconomy; Decree 356/2025 replacing Decree 13/2023 - vanban.chinhphu.vn, EY Vietnam legal alert Mar 2026, LuatVietnam; Decree 147/2024 - LuatVietnam; Decree 52/2024 capital figures - LuatVietnam (English); e-invoices mandatory from 1 Jul 2022 - chinhphu.vn; Decree 70/2025 and Resolution 198/2025 - ThuVienPhapLuat *(medium confidence: quote the rule, keep thresholds approximate)*; Circular 99/2025 replacing Circular 200 - Bac Ninh Department of Finance

### EU / EEA
- **Personal data**: GDPR - lawful basis, consent, data subject rights, breach notification
- **Platforms**: the Digital Services Act - handling illegal-content reports, transparency reporting
- **AI**: the EU AI Act adds obligations by risk level, including transparency for chatbots and generated content
- **Payments**: PSD2 licensing and strong customer authentication

### United States
- **Personal data**: a patchwork of state laws such as California's CCPA/CPRA; COPPA whenever under-13s might sign up
- **Payments**: money transmitter licenses are state by state
- **Health / finance data**: HIPAA, GLBA and sector rules if they apply

### Japan
- **Personal data**: the APPI governs how user data is collected, used and shared
- **Messaging**: chat-style services may have to notify the regulator under the Telecommunications Business Act
- **Payments**: Payment Services Act for prepaid instruments and funds transfer

### Anywhere else
- Most countries now have a data-protection law; say so in general terms rather than naming one you're unsure of
- Transport, finance, healthcare and food delivery need sector licenses in almost every market
