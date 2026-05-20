# Upwork Proposal Templates

Three proposal variants for the most common AI red team opportunities on Upwork. Each is pre-written to a quality bar appropriate for an Upwork buyer skimming 30 proposals in 5 minutes; the buyer should be able to read the first three lines and decide to read the rest.

## How to use this file

For every Upwork job you apply to:

1. Read the job post twice. Identify what the client actually wants (often different from what they typed).
2. Match the job to one of the three variants below.
3. Copy the variant, replace `{{PLACEHOLDERS}}`, and trim anything that does not fit the specific opportunity.
4. Submit. Do not send the proposal as-is; personalization in the first sentence drives reply rates.

**Critical Upwork formatting rule:** Upwork strips most markdown but keeps line breaks and bullet points (`-` rendered as bullet). Keep formatting plain. No headings, no bold, no code blocks. Use line breaks and indentation only.

**Time budget for sending a proposal:** 8 to 12 minutes per opportunity, including reading the post carefully. If you cannot personalize in that time, the opportunity is not a fit; move on. Quality over volume.

**Pricing anchor:** Use the rates below as starting points. Adjust based on client budget signals in the job post and your current bookings.

| Variant | Engagement size | Day rate equivalent | Project fee range |
|---|---|---|---|
| A — Pre-deployment red team | 3-7 days | $400-700 | $1,500-5,000 |
| B — Targeted finding investigation | 1-2 days | $500-800 | $500-1,500 |
| C — Ongoing regression | 1-2 days quarterly | $400-600 | $1,500/quarter |

You do not need to disclose the day rate. Quote the project fee.

**On rate negotiation:** Upwork buyers will lowball. Hold your floor. If they say "our budget is $300 total" for a real AI red team engagement, the right answer is "I understand. That budget doesn't match the depth this needs. If you'd like a single-finding investigation instead, that fits — happy to discuss." Walking away from a lowball opportunity is itself a positioning move.

---

## VARIANT A: Pre-deployment Red Team

**When to use:** Job post mentions launching a chatbot, AI feature, RAG system, or LLM product; client wants assessment before going live. Look for phrases like "we're launching," "pre-launch," "before we go to production," "going to production next month," "security review of our AI."

**Project fee range:** $1,500 - $5,000

**Indicators it's a good fit:**

- Client describes the application's purpose, not just "test our AI"
- Mentions OWASP, MITRE ATLAS, or specific risks like "prompt injection"
- Budget signal in the post is above $1,500 (or "negotiable" with substantial scope)
- Timeline is 1-3 weeks (not "today")
- Reasonable detail in the job post (signals a non-amateur buyer)

**Indicators it's a bad fit (skip):**

- Budget under $500 with substantial scope expected
- "Quick check" or "should take an hour"
- Vague scope with no application details
- Client wants only automated scanning with no manual depth

---

### THE PROPOSAL

Hi {{CLIENT_NAME if visible, else "there"}},

{{ONE LINE that proves you read the post — reference the specific application, framework, or risk they mentioned. e.g. "Saw your post about the customer support chatbot you're launching next month — the LangChain + RAG setup is exactly the architecture where I focus my red team work."}}

I'm an AI red team specialist with three years of traditional pentest and SOC background, now focused on LLM application security. For your engagement, I'd recommend a structured pre-deployment assessment that covers both model-layer attacks (prompt injection, jailbreaks, content policy bypass) and the application-layer issues that most LLM security reviews miss — authentication on chatbot APIs, conversation ID authorization, RAG cross-tenant exposure, tool call manipulation in agentic flows.

How I'd approach this engagement:

- Phase 1: Reconnaissance and surface mapping using Burp Suite — identify your application's endpoint shape, request structure, auth, and any application-layer issues incidentally surfaced ({{2-4}} hours)
- Phase 2: Broad-coverage vulnerability scanning using NVIDIA's Garak — runs {{N}} probe modules covering OWASP LLM Top 10 categories, produces structured findings with reproducible evidence ({{2-3}} hours)
- Phase 3: Targeted deep-dive using Microsoft's PyRIT — multi-turn adversarial scripts, custom scorers for your specific threat model (e.g. {{THREAT_FROM_JOB_POST}}) ({{4-8}} hours)
- Phase 4: Verification, reproduction, and client-ready report

Deliverable: a structured engagement report with executive summary, full finding details (severity, reproduction steps, evidence, remediation), positive findings, and a verification plan. Findings are mapped to OWASP LLM Top 10 and MITRE ATLAS v5.4.0 for clean integration with whatever security framework your team already uses.

You can see the structure of my reports here: github.com/Wisdomajoku/ai-redteam-journey/blob/main/templates/example-engagement-report.md (this is a fictional engagement on a healthcare chatbot, illustrating the deliverable shape).

Proposed timeline: {{N}} business days from kickoff to final report.

Proposed fee: ${{X,XXX}}, fixed-price. Includes one round of follow-up questions on findings within 30 days of delivery.

Happy to discuss scope, threat model, or any specifics about your target before we engage. I'm based in Lagos (WAT), which works well for clients in Europe, US East Coast (with morning overlap), and APAC.

— Wisdom Ajoku
github.com/Wisdomajoku/ai-redteam-journey
linkedin.com/in/{{YOUR_HANDLE}}

---

## VARIANT B: Targeted Finding Investigation

**When to use:** Client reports they noticed something specific and want one issue investigated. Could be a leaked system prompt, a suspicious chatbot response, an internal finding from their dev team they want validated. Look for phrases like "we noticed," "we found," "we suspect," "can you check whether," "can you confirm if."

**Project fee range:** $500 - $1,500

**Indicators it's a good fit:**

- Specific issue named, not vague concern
- Client has working access to the affected system
- Reasonable timeline (1-7 days)
- Budget signal aligns with a 1-2 day engagement

**Indicators it's a bad fit:**

- "We think we got hacked, can you do incident response" — this is IR, not red team. Refer if you have a contact, otherwise pass.
- Issue is on a system the client does not own or authorize you to test
- Budget under $300

---

### THE PROPOSAL

Hi {{CLIENT_NAME}},

{{ONE LINE referencing the specific issue they raised. e.g. "Read your post about the chatbot returning what looks like part of the system prompt — that's a pattern I see often, and it's worth understanding the full exposure before you decide on a fix."}}

I'm an AI red team specialist focused on LLM application security. For a single-finding investigation like this, I run a focused 1-2 day deep-dive that answers three questions clearly:

- What exactly is happening? (Mechanism, reproducibility, attack vector)
- How exploitable is it in practice? (Realistic threat model — who can do this, with what skill, against what data)
- What's the right fix and what's the right priority? (Specific remediation with effort estimate)

How I'd approach this specific issue:

- Reproduce the finding from your description, confirming exact conditions ({{1-2}} hours)
- Characterize the exposure: range of variations that trigger it, what data leaks, who can access it ({{2-4}} hours)
- Map to OWASP LLM Top 10 + MITRE ATLAS for context with your existing security work
- Produce a focused finding report with reproduction steps, severity rating using OWASP Risk Rating, and prioritized remediation

Deliverable: a 4-8 page focused finding report (not a full engagement report — appropriate to scope). Covers the specific issue thoroughly with evidence and remediation. Includes a 30-minute video walkthrough of the reproduction if helpful for your dev team.

Proposed timeline: {{N}} business days from access being provided.

Proposed fee: ${{X,XXX}}, fixed-price. Includes follow-up questions on the finding within 30 days.

Two things I'll need to start: (1) the access credentials or test account to reproduce, (2) confirmation of authorization scope (which endpoints/conversations are in-bounds). Standard responsible-disclosure terms.

— Wisdom Ajoku
github.com/Wisdomajoku/ai-redteam-journey
linkedin.com/in/{{YOUR_HANDLE}}

---

## VARIANT C: Ongoing Regression Testing

**When to use:** Client mentions they've done a previous security assessment, want recurring testing, or want to verify fixes from a prior engagement. Could be follow-up to a previous engagement of yours, or new business from a client whose previous tester has moved on. Phrases: "quarterly testing," "ongoing red team," "regression suite," "we patched these findings and want verification."

**Project fee range:** $1,500/quarter recurring (or larger if they want a Promptfoo-based automated suite built one-time)

**Indicators it's a good fit:**

- Client has an existing finding list, prior report, or specific change to verify
- Mentions ongoing testing as an explicit need
- Mature enough engineering org that they care about regression discipline
- Budget signal suggests recurring monthly or quarterly engagement

**Indicators it's a bad fit:**

- One-off engagement disguised as "ongoing" (be explicit before signing)
- Client wants "fully automated, no human work needed" — this is wishful; explain the limit

---

### THE PROPOSAL

Hi {{CLIENT_NAME}},

{{ONE LINE referencing their context. e.g. "Saw your post about wanting quarterly red team verification on your AI chatbot — this is exactly the structure I recommend most of my clients move toward after their first engagement, and I'd be glad to be the recurring resource."}}

I'm an AI red team specialist focused on LLM application security. For ongoing regression testing, I structure engagements as one of two patterns depending on your maturity:

Pattern 1: Quarterly assessment ({{1-2}} days each quarter, $1,500 fixed per quarter). I rerun your prior finding tests, plus a baseline scan against current OWASP LLM Top 10 categories, plus targeted deep-dives on anything new in your application since the last quarter. Comparative report against the previous quarter's baseline. Best when your application changes meaningfully every quarter.

Pattern 2: Continuous regression suite (one-time setup $2,500 - $4,000, then $750/quarter for review). I build a Promptfoo or PyRIT-based regression suite encoding all known finding patterns, which your team can run on every deploy. I review the run quarterly and update the suite as your application evolves. Best when you have CI/CD discipline and want continuous coverage rather than point-in-time assessments.

Both patterns deliver:

- A clear pass/fail status on each known finding from prior work
- Detection of new issues introduced by your last quarter's changes
- Mapped to OWASP LLM Top 10 + MITRE ATLAS v5.4.0
- A short executive summary suitable for forwarding to your CTO or board, plus full technical details for your engineering team

For both patterns, the first engagement includes a 30-minute discovery call to understand: your existing finding history, current application changes, and what "good" looks like for your team's reporting needs.

Sample of the report shape I deliver: github.com/Wisdomajoku/ai-redteam-journey/blob/main/templates/example-engagement-report.md

Proposed start: {{TIMING}}. Quarterly cycles run {{TIMING_OFFER}}.

Happy to discuss which pattern fits, or to suggest a hybrid based on your specifics.

— Wisdom Ajoku
github.com/Wisdomajoku/ai-redteam-journey
linkedin.com/in/{{YOUR_HANDLE}}

---

## Cross-cutting tips for all three variants

**On the first line of every proposal.** This is the single highest-leverage element. Upwork's interface shows the buyer the first 100-150 characters before they click through. If your first line is generic ("I am a cybersecurity professional with X years of experience"), the buyer never opens the proposal. If your first line references their specific situation, they read on. Always personalize the first line. If you cannot personalize, do not send.

**On rate justification.** Buyers will ask "why $X." The answer is never "because that's my rate." The answer is some version of: "This engagement requires Y days of skilled work. The deliverable is a client-ready report your engineering team can act on directly. The fee covers the work plus 30 days of follow-up support. Lower fees on platforms typically mean automated scanning only, which would catch maybe 30% of what a manual review surfaces in an LLM application." You don't need to memorize this verbatim; the structure is: time + deliverable + value comparison.

**On clients who want to negotiate down to half your rate.** Two responses depending on signal:

If they seem like a legitimate client with a real budget constraint: "I can do a scoped-down engagement at $X. That covers Phase 1 and Phase 2 of the standard approach, which is sufficient if you want a baseline assessment but won't include the multi-turn deep dive. Let me know if that fits."

If they seem like they're shopping for the cheapest: "I appreciate the interest, but the rate I quoted is the floor for this scope. There are other testers on Upwork at lower rates; whether that delivers the depth you need depends on the engagement. Happy to refer you to other resources if budget is the primary constraint."

The second response loses the engagement but protects your positioning. Doing $300 engagements once trains the market to expect them from you.

**On scope creep mid-engagement.** Clients will ask for "just one more thing." Two responses: yes, no charge, if it's under 30 minutes; or "happy to add that — it'll add $X to the scope and Y days to the timeline." Never agree to scope additions for free beyond the 30-minute floor; clients respect this once they see the boundary.

**On red flags during the initial conversation.** Walk away from any client who:

- Cannot or will not sign a written authorization
- Wants you to test a system they don't appear to own
- Pressures you to skip the scoping conversation and "just start testing today"
- Suggests payment outside Upwork (until you have an established relationship and you've agreed to migrate off-platform mutually)
- Asks you to test "production data" or use real user accounts other than the one they provide

**On the portfolio link in your proposals.** Every proposal references your repo. This works because:

- It's instant proof you do this work, not just claim to
- It shows your judgment (the docs, the writeups, the example engagement)
- It differentiates you from 95% of Upwork proposers who have no portfolio

When the repo gets your first capstone, link to that specifically. Capstone-level proof beats generic repo link.

**On Upwork's algorithmic boost for fast replies.** Apply to jobs within the first 30 minutes of posting if possible. The platform shows new jobs to bidders in waves; early proposals get more visibility. After 4 hours, your proposal is one of 40+ and visibility drops.

**On the Upwork rating game.** Your first 5-10 engagements are worth taking at slightly below your target rate if it lets you secure 5-star reviews. After 10 reviews, you can hold the line at full rate because the social proof carries you. Do not undercut indefinitely; do undercut strategically for the first few.

