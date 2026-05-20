# STATUS.md

Tool version tracking for the operator's guides in this repository. Updated when material drift is identified between the docs and current upstream releases.

This file is the canonical record of "what's drifted." The individual tool docs in `week2/tools/` reflect the state at the time they were written; this file tracks where they stand against current versions and what changed.

---

## Last review: May 20, 2026

### Garak (`week2/tools/garak-operators-guide.md`)

**Doc version reference:** Garak v0.14.1 (April 3, 2026)

**Current upstream:** Garak v0.15.0 (released May 1, 2026 on PyPI)

**Drift impact:** Minor. Existing commands and patterns in the doc still work. v0.15.0 added probes and a detector that aren't reflected in the doc's tier taxonomy.

**What v0.15.0 added:**

- **New probe modules:**
  - `goat` — multi-turn GOAT (Generative Offensive Agent Tester) probe. Closes part of the gap the doc describes between Garak and PyRIT for multi-turn coverage.
  - `agent_breaker` — probes for agentic systems
  - `system_prompt_extraction` — dedicated module (previously used goodside / promptinject patterns)
- **Probe expansion:** homoglyph obfuscation added to existing `smuggling` module
- **New detector:** `ModernBERT` refusal detector
- **New generator:** `NeMoGuardrails` server support
- **Internal:** DAN probes refactored using metaclass pattern (no command change for users)

**Action when re-engaging the doc:**

1. Add `goat`, `agent_breaker`, `system_prompt_extraction` to the Tier 2 or Tier 3 table.
2. Note in the "Where Garak ends and PyRIT begins" section that v0.15+ has improved multi-turn coverage via `goat`, narrowing (but not closing) the gap.
3. If using ModernBERT detector, note that `--extended_detectors` may surface different results than older runs.

**Source of truth:** https://pypi.org/project/garak/ and https://github.com/NVIDIA/garak/releases

---

### PyRIT (`week2/tools/pyrit-operators-guide.md`)

**Doc version reference:** PyRIT v0.12.0 (April 2026)

**Current upstream:** PyRIT v0.13.0 (released April 17, 2026 on PyPI)

**Drift impact:** Minor. The three engagement scenarios in the doc still execute correctly. v0.13.0 introduced new abstractions for richer target modeling and attack composition that the doc's Custom Target section does not show.

**What v0.13.0 added:**

- **`TargetConfiguration` redesign** with message pieces redesign for richer target modeling (#1573, #1588). Affects how new custom targets are written.
- **`TargetRequirements`** — new abstraction for declaring target-level capability requirements (#1582). Not breaking but enables better composability of attacks and targets.
- **`AttackTechniqueRegistry`** — discoverable, composable attacks (#1611).
- **AWS Bedrock partner integration tests** for OpenAI-compatible Mantle endpoints (#1575).
- **Removed (deprecated):** `FoundryScenario` alias, `piece.role` in conversation analytics. Neither is referenced in the doc, so no impact on doc accuracy.
- **Stricter validation** of explicit empty field overrides in the attack executor (#1507). Scripts that worked silently before may now error.

**Action when re-engaging the doc:**

1. Update version reference from v0.12.0 to v0.13.0 when next revising.
2. When writing a fresh custom target, follow the v0.13.0 `TargetConfiguration` pattern; the example in the doc still works but is not the canonical new approach.
3. If a script that previously ran starts erroring on empty field overrides, that's the v0.13.0 validation tightening, not a bug.

**Source of truth:** https://pypi.org/project/pyrit/ and https://github.com/microsoft/PyRIT/releases

---

### Burp Suite (`week2/tools/burp-llm-operators-guide.md`)

**Doc version reference:** Burp Suite 2026.4.3 (May 13, 2026)

**Current upstream:** Burp Suite 2026.4.3 (May 13, 2026)

**Drift impact:** None. Doc is current as of the most recent stable release. Confirmed against PortSwigger release notes May 20, 2026.

**Watch list for future drift:**

- Burp Suite Pro pricing — currently $499/year as of January 2026 price adjustment. Verify before quoting clients.
- Burp AI in Repeater feature set is evolving release-over-release; the 10,000 free credits figure is current but may change.
- LLM Injector extension (third-party, by Anmol K Sachan) is on v4 as of March 2026; the maintainer updates it actively, and v5 features may appear.

**Source of truth:** https://portswigger.net/burp/releases and https://portswigger.net/burp/ai

---

## Review cadence

This file should be updated:

- Before any significant client engagement that depends on the doc being current
- When a tool ships a major version bump (v0.X → v0.Y is major; v0.X.A → v0.X.B is minor)
- At the start of each new engagement phase (e.g. beginning of Capstone 1, beginning of Capstone 2)
- At minimum every 6 weeks, since the tools in this stack release approximately monthly to quarterly

The discipline is not "rewrite the doc every time." The discipline is "know what's drifted and decide whether the drift matters for what I'm about to do." Most drift is additive (new probes, new attacks) and doesn't break existing patterns.

## How to verify drift yourself

For Garak:
```bash
python -m pip install garak==0.15.0  # or whatever the current version is
python -m garak --list_probes | wc -l   # count probes, compare to doc
```

For PyRIT:
```bash
python -c "import pyrit; print(pyrit.__version__)"
```

For Burp:
- Help menu → About → version number
- Compare to https://portswigger.net/burp/releases

