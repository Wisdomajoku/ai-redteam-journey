# Capstone Projects + Reading Objectives

Three items prepared in advance of post-subscription work. Capstone briefs deliberately specify outcomes and quality bars, not method. The "how" is for you to figure out — that's the proficiency demonstration.

---

## Capstone 1: Comparative LLM Vulnerability Assessment of Three Groq-Hosted Models

**Type:** Solo engagement-style assessment, fictional client framing.

**Estimated time:** 8-12 hours across 2-3 sessions in Week 3.

**Fictional client framing:** Build the project as if you were engaged by a fictional client (e.g. "FinanceFlow, a fintech evaluating LLMs for their internal compliance chatbot") who needs to decide which of three candidate models has the safest behavior profile. The fictional framing matters because it forces you into the deliverable shape a real client would expect.

### Required outcomes

By the end of this capstone, your repository must contain:

1. **Three Garak scan reports** (HTML + JSONL outputs) against three different Groq-hosted models. The model choice must demonstrate architectural diversity — at minimum one Llama-family large, one Llama-family small, and one non-Llama architecture (Mixtral or similar if available on Groq).

2. **A comparative analysis document** that does more than restate findings. It must answer: which model is most vulnerable to which class of attack, and why does the architectural or training difference plausibly produce that pattern? This is the part that demonstrates senior framing. A surface-level "Model A had 30% failure, Model B had 25%" is not enough; you must propose mechanisms.

3. **A defender's recommendation document** that translates your findings into "if you are deploying for this use case, here is which model to pick and why." This is what your fictional client paid for.

4. **A README at the project root** that orients a hiring manager scanning the repo in 60 seconds. Methodology, models tested, headline findings, link to detailed reports.

### Quality bars

- The probe set must be consistent across all three models (you cannot run different probes on different targets — that invalidates the comparison)
- Generations per prompt must be the same across all three runs
- Random seed must be set for reproducibility
- At least one finding per model must include a manually-verified reproduction in Burp Repeater or PyRIT, not just Garak's auto-report
- The comparative analysis must reference at least one peer-reviewed paper or technical report explaining why architectures behave differently under adversarial prompting

### What "done" looks like

A hiring manager opens your repo, reads the README, clicks through to the comparative analysis, and within five minutes thinks: "this person can run a real engagement and produce a real deliverable."

### What this capstone proves

- Tool fluency under realistic constraints (rate limits, probe selection, consistent methodology)
- Comparative analytical capability (the rarer skill — most testers can run one scan)
- Defender framing (the senior signal — you understand both attacker and defender perspectives)
- Reproducibility discipline (the engineering signal — your work can be replayed)

### Optional stretch

If you have appetite after the required outcomes, add a fourth model from a different provider (Together.ai, Anthropic via Bedrock, OpenAI direct) as an extra-architectural data point. Mention the increased generality this brings.

### What this capstone is NOT

- It is not a deep red team engagement against one target. That is Capstone 2.
- It is not a tutorial about how to use Garak. It is a finding-producing assessment.
- It is not a CTF write-up. It is structured like a client deliverable.

---

## Capstone 2: End-to-End AI Red Team Engagement Simulation

**Type:** Full simulated engagement using the complete toolchain, fictional client framing.

**Estimated time:** 15-20 hours across 3-5 sessions in Week 4 or Week 5.

**Fictional client framing:** Build the project as if you were engaged by a fictional client whose application you also build (or stand up using an open-source LLM application reference architecture). This is the senior-level demonstration — you scope, execute, and report on a complete engagement.

### Required outcomes

Your repository must contain a full engagement simulation, structured as a real client deliverable would be:

1. **A fictional scoping document.** What the client asked for. What you scoped in and out. The threat model. The authorization framing. This is the artifact a client signs before you start.

2. **A reconnaissance artifact.** Burp proxy session capture or annotated screenshots showing how you mapped the target's surface. The endpoint list, request shapes, authentication mechanism, streaming protocol if applicable.

3. **A broad scan report.** Garak output mapped to the targets discovered in recon. Identify the highest failure rate categories.

4. **A deep-dive findings pack.** PyRIT scripts targeting the highest-rate Garak categories. Each working attack documented with reproduction steps, evidence, and severity rating.

5. **An application-layer findings pack.** Burp Repeater workflow outputs showing application-layer issues — authentication, authorization, IDOR, system prompt extraction, tool call manipulation, header injection. Whichever apply to the target you stood up.

6. **A regression suite.** A Promptfoo or PyRIT-based test suite encoding the working attacks, runnable as a single command. This is what a real client would pay extra for.

7. **The complete engagement report.** Using your engagement-report-template. Filled in with the actual findings from this simulation. This is your portfolio-grade deliverable.

8. **A README + project overview** that frames the whole thing for a reader, including which fictional target you used, which OWASP LLM Top 10 categories you covered, and what skills the capstone demonstrates.

### Target selection

The fictional target you build or stand up must include at minimum:

- A chatbot UI or API endpoint (the user-facing surface)
- A system prompt with operational rules (you will try to extract this)
- Some form of authentication (you will test it)
- A conversation ID or session mechanism (you will test for IDOR)

Suggested approach (one of many): use an open-source RAG chatbot reference architecture, point it at Groq's API, deploy it locally on your Kali VM. The complete stack runs on your laptop. The "client" is fictional but the application is real.

### Quality bars

- The engagement report must follow your template, complete with executive summary, scope, methodology, findings, positive findings, remediation roadmap, verification plan, and appendices.
- At least one Critical finding, at least two High findings, at least two Medium findings. If your fictional target does not have enough surface to support that, choose a richer target.
- Each finding must include a reproduction artifact (HTTP request, PyRIT script, or Garak probe invocation) that a reader can independently replay.
- The regression suite must be runnable end-to-end in under 10 minutes.
- All findings mapped to OWASP LLM Top 10 + MITRE ATLAS.

### What "done" looks like

A hiring manager or potential client opens the repo, reads the engagement report cover to cover, and thinks: "I would hire this person to do exactly this work for my company." That is the bar.

### What this capstone proves

- Full engagement scoping capability (not just running tools)
- Multi-tool orchestration (Burp + Garak + PyRIT used in sequence, not in isolation)
- Client communication discipline (the report shape is the deliverable, not just the findings)
- Build-and-break capability (you stood up an application AND broke it; few testers do both)
- Reproducibility at scale (the regression suite proves the work can be productized)

### Optional stretch

Build the same engagement against a second target with a different architecture (e.g. agentic system with tool calls, or multi-modal model accepting image input). Demonstrates breadth across the AI red team domain, not just chatbots.

### What this capstone is NOT

- It is not a teaching artifact. It is a portfolio piece.
- It is not Garak v PyRIT v Burp head-to-head comparison. It is the three working together.
- It is not a CTF. It is a structured client engagement simulation.

---

## Reading Objectives for OWASP GenAI Red Team Guide + Microsoft + Google SAIF + NIST

The combined reading package totals roughly 6-8 hours if read selectively. Read in this order. Spend more time on the first two; skim the last two.

### 1. OWASP GenAI Red Team Guide (primary, ~3 hours)

**URL:** https://genai.owasp.org/resource/genai-red-teaming-guide/

**What to extract:**

- **Engagement scoping language.** What questions does the guide say a red teamer should ask before starting? Mine this for your own scoping conversation script. Compare to what you instinctively wrote in the engagement report template. Where the guide is more thorough, update your template.

- **Methodology structure.** What phases does the guide propose? Compare to the four-phase approach (recon, broad scan, deep dive, verification) you used in your operator docs. Identify any phase you have been missing.

- **Reporting structure.** Pay attention to: severity rubric (compare to your OWASP Risk Rating choice), evidence requirements (what proof goes with each finding), remediation language (how they recommend phrasing fixes).

- **Threat model framework.** The guide proposes layers: model, application, infrastructure, agentic. Note which OWASP LLM Top 10 categories map to which layer. This is the framework you'll use during the recon phase of every engagement.

- **Where the guide is thin.** Read with one eye on gaps. Where the guide is sparse (often: agentic systems, RAG-specific attacks, multi-modal targets, indirect injection real-world vectors), those are the spaces you can publish your own content and stand out.

**Output:** One page at `week3/owasp-genai-redteam-notes.md` with four sections — Key methodology phases I'm adopting (3-5 bullets), Reporting structure I'll incorporate, Gaps I noticed, Citations to mine for client conversations and proposals.

### 2. Microsoft AI Red Team Lessons (primary, ~1.5 hours)

**Source:** "Lessons from Red Teaming 100 Generative AI Products" — Microsoft AI Red Team paper, available via Microsoft Research or arXiv.

**What to extract:**

- **The 8 lessons.** Read each. Compare to your own emerging mental model. Which lessons confirm what you already think? Which ones challenge it?

- **Microsoft's framing of "what doesn't work."** They are unusually honest about red team failures and dead ends. This is more valuable than the success stories. What attacks did they expect to work that did not? What did they expect to fail that surprised them?

- **The "harm" vs "vulnerability" distinction.** Microsoft draws a line between AI safety (harm) and AI security (vulnerability). Your work is primarily the latter. Understand the distinction so you can frame your offerings correctly to clients who confuse the two.

- **Multi-modal red teaming notes.** Most clients in your first year will be text-only chatbots. But the Microsoft paper covers multi-modal extensively. Skim those sections for vocabulary you can drop into a proposal when a multi-modal opportunity comes up.

**Output:** Add a section to the OWASP notes file titled "Microsoft AI Red Team lessons — most useful." 5-8 bullets max.

### 3. Google SAIF (Secure AI Framework) (skim, ~1 hour)

**URL:** https://safety.google/cybersecurity-advancements/saif/ or search "Google SAIF framework"

**What to extract:**

- **The six SAIF elements.** Note them. They map roughly to defender concerns; you should be able to articulate them when a client asks "how does your work fit into SAIF?"

- **The risk categorization vocabulary.** Google uses different phrasing than OWASP. When a Google-ecosystem client (or a client using Google Cloud AI services) reaches out, knowing SAIF vocabulary signals you can speak their language.

- **What SAIF does NOT cover.** Google's framework is defender-focused; offensive testing is implicit. Your work fills the gap. This is positioning material.

**Output:** Add "SAIF vocabulary I should know" as 5-7 bullets in your OWASP notes file.

### 4. NIST AI Risk Management Framework (selective skim, ~1.5 hours)

**URL:** https://www.nist.gov/itl/ai-risk-management-framework

**CRITICAL — do NOT read cover to cover.** The full NIST AI RMF is hundreds of pages. Read only:

- **The MAP function:** how organizations identify and categorize AI risks. This tells you what your government and enterprise clients are asked to do.
- **The MEASURE function:** how organizations evaluate AI risks. Your red team output is one input to this function.
- **The Generative AI Profile (GAI Profile).** This is NIST's specific guidance for generative AI. ~50 pages, more recent than the core RMF. Read this section carefully.

**What to extract:**

- **The risk categories.** NIST uses different categorization than OWASP and MITRE. Government and large-enterprise clients will speak in NIST terms.

- **The "trustworthy AI" attributes** (validity, safety, security, accountability, transparency, fairness, privacy). Memorize these as a vocabulary set. When a regulated-industry client reaches out, framing your work in these terms accelerates the sales conversation.

- **The evidence requirements.** NIST's framework asks organizations to document risk assessments. Your engagement reports become inputs to this documentation. Designing reports that map to NIST evidence requirements is a value-add you can charge for.

**Output:** Add "NIST AI RMF — what regulated clients expect" as a 6-10 bullet section. Save the URL of the GAI Profile for future reference.

### Total expected output

One file at `week3/reading-notes.md` containing:

1. OWASP GenAI Red Team Guide — Key takeaways
2. Microsoft AI Red Team — Most useful lessons
3. Google SAIF — Vocabulary I should know
4. NIST AI RMF — What regulated clients expect
5. Cross-cutting observations — Patterns across all four

Total length: 2-3 pages. Not an essay; a reference document you will skim before client conversations and use to populate proposals.

### Discipline note

Do not read these four sources in the order you encounter them online or in the order I listed them. Read in the order above: OWASP first (most directly useful), Microsoft second (most honest), Google third (positioning), NIST fourth (selective only).

Resist the urge to read NIST cover to cover. The framework is comprehensive and you are not writing a policy document; you are extracting vocabulary and evidence requirements for client conversations.

---

## Suggested execution order across the post-subscription period

**Friday May 22:** OWASP GenAI Red Team Guide reading + notes. Half day.

**Saturday May 23 - Sunday May 24:** Capstone 1 execution. Three Garak scans, comparative analysis, defender recommendations, repo write-up.

**Following week (May 25-31):** Microsoft + Google SAIF + NIST skim and notes. Half day total across two evenings. Capstone 2 scoping and target selection.

**Week of June 1-7:** Capstone 2 execution and write-up.

By June 8, you should have: two capstones in the repo, all four reading notes consolidated, all templates ready for use. That is the body of work you take into paid engagements.

