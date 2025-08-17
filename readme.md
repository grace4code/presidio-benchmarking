📖 Definitions
1. True Positive (TP)

Presidio detected an entity, and it was actually correct.

Example: Presidio flagged john.doe@gmail.com as EMAIL_ADDRESS and it really is an email.

👉 TPs are good detections.

2. False Positive (FP)

Presidio detected an entity, but it was wrong.

Example: Presidio flagged hello_world as EMAIL_ADDRESS, but it’s not a valid email.

👉 FPs are false alarms.

3. False Negative (FN)

An entity was present in the data, but Presidio missed it.

Example: The text had +91-9876543210 (a phone number), but Presidio didn’t detect it.

👉 FNs are missed detections.

4. Precision

Of all the entities Presidio said were found, how many were actually correct.

Think of it as “trustworthiness” of detections.

5. Recall

Of all the entities that really existed, how many Presidio actually caught.

Think of it as “coverage” of detections.

6. F1 Score

A single score that balances both Precision and Recall.

Think of it as “overall performance” when you don’t want to just look at precision or recall alone.

7. Support (Count of Records)

Number of test samples (records) you used for that entity type.

Example: If you generated 50 fake phone numbers, then Support = 50.