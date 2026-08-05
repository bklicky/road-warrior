# Road Warrior Stationary Test Protocol

## Objective

Verify that the Road Warrior ChatGPT Project can support the minimum Prototype 1 loop before any moving-drive test. This protocol tests the skeleton of the experience, not polished behavior.

Run the complete sequence in Environment A first. If no blocking issue prevents further testing, open a new dated test chat and repeat the sequence in Environment B.

## Test Environments

### Environment A — Desk / Phone

Used to verify conversational behavior before involving the car.

### Environment B — Parked Kia

Used to verify:

- Android Auto navigation remains visible.
- Bruce's voice reaches Road Warrior through the active audio path.
- Road Warrior replies through the car speakers.
- The Voice session survives normal screen and app-state changes.
- No phone interaction is required once the test begins.

## Equipment and Configuration Record

| Field | Value |
| --- | --- |
| Test date | |
| Tester | |
| Phone model | |
| Android version | |
| ChatGPT app version | |
| ChatGPT plan | |
| Voice option used | |
| Background conversations enabled: Yes/No | |
| Project name | |
| Project-only memory enabled: Yes/No | |
| Kia model/year | |
| Android Auto mode: wired/wireless | |
| Navigation app | |
| Phone battery optimization state | |
| Cellular or Wi-Fi connection | |
| Other relevant configuration notes | |

## Preconditions

- [ ] Road Warrior Prototype 1 Project exists.
- [ ] Project Instructions are saved and verified.
- [ ] Required project documents are attached.
- [ ] A new dated test chat is open.
- [ ] Voice is started manually.
- [ ] For the Kia test, the vehicle is parked safely.
- [ ] Android Auto navigation is active for the Kia test.
- [ ] Bruce will not handle the phone while the test is running.

## Test Sequence

| Run field | Value |
| --- | --- |
| Environment: Desk / Phone or Parked Kia | |
| Test chat | |
| Start time | |

| Step | Bruce says or does | Expected Road Warrior behavior | Actual behavior | Pass/Fail | Notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | Start with the active Voice session in standby. | Remains available without beginning substantive engagement. | | | |
| 2 | Say a casual greeting without “Hey Road Warrior.” | Does not begin a substantive conversation while in standby. | | | |
| 3 | Say “Hey Road Warrior.” | Acknowledges briefly and becomes conversationally active. | | | |
| 4 | Have a short natural conversation. | Responds naturally and maintains the thread. | | | |
| 5 | Say “Capture that.” | Briefly acknowledges and preserves the relevant item. | | | |
| 6 | Continue the original conversation. | Continues without unnecessary recap or derailment. | | | |
| 7 | Say “I’ve got feedback.” | Briefly acknowledges feedback mode without losing the prior thread. | | | |
| 8 | Provide one feedback observation. | Captures the observation with enough context for later review. | | | |
| 9 | Ask or allow Road Warrior to resume. | Returns to the prior conversation at the correct point. | | | |
| 10 | Say “Road Warrior, stand by.” | Briefly acknowledges and stops substantive engagement. | | | |
| 11 | Allow at least 30 seconds of silence. | Remains in standby. | | | |
| 12 | Play radio, music, or ambient speech. | Does not treat ambient audio as an invitation to converse. | | | |
| 13 | Observe the session while ambient audio continues. | Does not begin a substantive conversation while in standby. | | | |
| 14 | Say “Hey Road Warrior.” | Recognizes the conversational activation phrase. | | | |
| 15 | Continue briefly. | Confirms reactivation through an appropriate response. | | | |
| 16 | Trigger or simulate one interruption: navigation prompt, screen lock, app backgrounding, or an incoming call if safe and practical. | Handles the interruption without unsafe interaction. | | | Interruption tested: |
| 17 | After the interruption, resume speaking to Road Warrior. | Session survives and resumes, or the failure is clearly observable and documented. | | | |
| 18 | State that Bruce is parked and ending the test. | Recognizes the transition to the closing review. | | | |
| 19 | Complete the brief end-of-drive reflection. | Conducts a short conversational reflection and preserves the responses. | | | |
| 20 | Ask Road Warrior to generate the full structured session package. | Generates the package from the conversation without asking Bruce to perform the summarization or categorization. | | | |
| 21 | Review the package against the required section checklist below. | Every required section is present; empty sections are explicitly marked rather than omitted. | | | |
| 22 | End the Voice session. | Voice ends deliberately and safely. | | | |
| 23 | Open or inspect the dated chat. | The session transcript is available in the chat. | | | |

Required package sections:

- [ ] Summary
- [ ] Key discoveries
- [ ] Decisions
- [ ] Action items
- [ ] Open questions
- [ ] Horizon ideas
- [ ] Open loops
- [ ] Contextual items
- [ ] Field feedback
- [ ] End-of-Drive Reflection
- [ ] Prototype audit
- [ ] Known transcript or continuity gaps

## Pass Criteria

The stationary test passes only if:

- Activation and standby phrases function as conversational conventions.
- Natural conversation works.
- Capture is preserved.
- Field feedback is preserved.
- The previous thread resumes after feedback.
- Standby does not produce unwanted substantive engagement.
- The session can survive at least one tested interruption or the failure is clearly documented.
- The full package is generated.
- The transcript is available.
- In the Kia, audio works both directions and Android Auto navigation remains usable.
- No phone handling is required while the test is active.

## Failure Conditions

- Car microphone does not reach Road Warrior.
- Road Warrior audio does not play through car speakers.
- Android Auto navigation becomes unusable.
- Voice terminates unexpectedly.
- Reactivation requires unsafe phone handling.
- Capture or feedback is lost.
- Thread resumption fails materially.
- Package sections are missing.
- Transcript is unavailable.
- Standby falsely engages repeatedly with ambient audio.

## Evidence to Record

- Screenshots where safe and practical.
- Exact failure messages.
- Approximate timing of failures.
- Whether the issue was reproducible.
- Whether recovery required touching the phone.
- Copy of the generated session package.
- Link or location of the test chat.
- Final pass/fail decision.

## Test Result

| Field | Result |
| --- | --- |
| Overall result: PASS / CONDITIONAL PASS / FAIL | |
| Blocking issues | |
| Non-blocking issues | |
| Recommended next action | |
| Approved for 10-minute drive test: Yes/No | |
