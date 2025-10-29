# EC2 Brute Force Incident - First Hour Checklist
- Confirm the GuardDuty finding and source IP reputation.
- Isolate the EC2 instance from the network (quarantine security group).
- Rotate instance profile credentials if present.
- Capture volatile data; ensure detailed CloudTrail logs are enabled.
