# Affective Transition Modulation Layer (ATML) — PR Template

## Summary
Describe the change related to ATML, including:
- transition orchestration
- classifier interrupt handling
- UMV (User Modulation Vector)
- PTS/IML/SAM pipeline

## Related Issues
- #<issue-number> Missing ATML (S2→S0 hard transitions)

## Architecture Impact
- Which components are modified?
- Does this PR introduce new states or transitions?
- Does it modify classifier gating?
- Does it add or update orchestration logic?

## Safety Considerations
- Does the change preserve safety guarantees?
- Does it modify enforcement behavior?
- Does it introduce any new risk vectors?

## Performance Considerations
- Latency impact (<50 ms requirement)
- Memory footprint
- Additional inference steps

## Testing
- Unit tests for state transitions
- Integration tests for classifier → ATML → SAM pipeline
- Regression tests ensuring no S2→S0 direct transitions

## Checklist
- [ ] ATML pipeline implemented
- [ ] No direct S2→S0 transitions
- [ ] Classifier interrupts routed through TO
- [ ] UMV updated per turn
- [ ] Documentation updated
