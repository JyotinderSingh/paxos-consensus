from collections import namedtuple

# data types
Proposal = namedtuple("Proposal", ["caller", "client_id", "input"])
Ballot = namedtuple("Ballot", ["n", "leader"])

# message types
Accepted = namedtuple("Accepted", ["slot", "ballot_num"])
Accept = namedtuple("Accept", ["slot", "ballot_num", "proposal"])
Decision = namedtuple("Decision", ["slot", "proposal"])
Invoked = namedtuple("Invoked", ["client_id", "output"])
Invoke = namedtuple("Invoke", ["caller", "client_id", "input_value"])
Join = namedtuple("Join", [])
Active = namedtuple("Active", [])
Prepare = namedtuple("Prepare", ["ballot_num"])
Promise = namedtuple("Promise", ["ballot_num", "accepted_propoals"])
Propose = namedtuple("Propose", ["slot", "proposal"])
Welcome = namedtuple("Welcome", ["state", "slot", "decisions"])
Decided = namedtuple("Decided", ["slot"])
Preempted = namedtuple("Preempted", ["slot", "preempted_by"])
Adopted = namedtuple("Adopted", ["ballot_num", "accepted_proposal"])
Accepting = namedtuple("Accepting", ["leader"])

# constants - would be preferable to have them in terms of average round-trip time
JOIN_RETRANSMIT = 0.7
CATCHUP_INTERVAL = 0.6
ACCEPT_RETRANSMIT = 1.0
PREPARE_RETRANSMIT = 1.0
INVOKE_RETRANSMIT = 0.5
LEADER_TIMEOUT = 1.0
# sorts before all real ballots
NULL_BALLOT = Ballot(-1, -1)
# no-op to fill otherwise empty slots
NOOP_PROPOSAL = Proposal(None, None, None)
