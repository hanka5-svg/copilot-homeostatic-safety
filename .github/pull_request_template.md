# Affective Transition Modulation Layer (ATML) — Pull Request Template

## Summary
Provide a clear summary of the changes introduced in this PR, focusing on:
- transition orchestration updates
- classifier interrupt handling
- User-State Vector (USV) or User Modulation Vector (UMV) updates
- adherence to the ATML pipeline (PTS → IML → SAM)

## Related Issues
- Link to issues related to missing or incorrect ATML behavior.
- Example: #<issue-number> Hard transitions (S2 → S0)

## Architecture Impact
Describe how this PR affects system architecture:
- Are new states or transitions introduced?
- Does this modify classifier gating?
- Does this update orchestration logic?
- Does this affect continuity or modulation behavior?

## Safety Considerations
Explain how the change interacts with safety:
- Does it preserve safety guarantees?
- Does it modify enforcement behavior?
- Does it introduce new risk vectors?

## Performance Considerations
Evaluate performance impact:
- Latency changes (<50 ms requirement)
- Memory footprint
- Additional inference or orchestration steps

## Testing
List tests performed:
- Unit tests for state transitions
- Integration tests for classifier → ATML → SAM pipeline
- Regression tests ensuring no S2 → S0 direct transitions

## Checklist
- [ ] ATML pipeline implemented correctly
- [ ] No direct S2 → S0 transitions
- [ ] Classifier interrupts routed through Transition Orchestrator
- [ ] UMV/USV updated per turn
- [ ] Documentation updated
