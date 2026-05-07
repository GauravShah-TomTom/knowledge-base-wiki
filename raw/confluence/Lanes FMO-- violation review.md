---
source_url: "https://tomtom.atlassian.net/wiki/spaces/PM/pages/1776190433/Lanes+FMO--+violation+review"
fetched: 2026-05-07 10:44:50
title: "Lanes FMO-- violation review"
---

# Lanes FMO-- violation review

Lanes FMO was run on zone DEU-01 ( Schleswig-Holstein ) , and below analysis

was done to determine the top loggers along with their reasons.

# Top 20 Loggers

**Rule ID**

**Count**

**Rule**

50329

37115

Intermediate Road Element not part of Normal Intersection

51684

19409

Missing Lane Connectivity

51147

6659

Missing Lane Connectivity

51059

5763

DTFR for Lane and Road not in line

51068

3710

Invalid Lane Connectivity

50311

2497

Incorrect Direction of Traffic Flow for Lane for connected lanes

50263

2489

Traffic Flow Conflicting with Driving Side

53161

2065

Invalid Lane Connection

51085

1382

Invalid Direction of Traffic Flow for Lane

51830

1232

Incorrect relationship to Lane Connectivity

52379

572

Incorrect Lane Connectivity Relationship

51083

557

Incorrect Lane Divider Type or incorrect Lane Connectivity

51149

387

Incorrect Lane Divider Type or incorrect Lane Connectivity

52261

335

Carriageways too close based upon number of lanes

53887

303

Lane Connectivity conflicts with Lane Direction Category

52497

281

Curvature at Junction starts and ends at same location of all Linear Assignment Maneuvers on that Junction

51062

265

Incorrect Lane Connection

52124

250

Incorrect Z-Levels for Lane Connectivity

52721

209

Geometry of Composing Part does not match geometry of Composite Feature.

52026

198

Incorrect Lane connection

# Rule ID discussion

We will review each of these rules and identify reasons of occurance.

\`1. **50329 Intermediate Road Element not part of Normal Intersection**

**Reason**: We have ‘skipped’ creating lane information on ‘normal’ roads.

This is due to huge junction areas created in HD and trajectories are present instead of centerlines.

**Txn**: c3a3c801-49ef-4d5e-beed-f31a6d984e0f

**Location** : 54.2898788, 10.4342199

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** 1) Determine main road based on FRC/N2C and check the number of lanes present on them. By default give same number of lanes on the road missing lanes and adjust connectivity. If they have different number of lanes , populate whichever lesser.

OR

2.  Determine parallel ‘trajectories’ to the geometry of the road. Assume them as centerlines matching the road and give same number of lanes on road.
    

OR

Orbis improvement to give us indication what are the number of lanes present on such road elements.

**Avoid this for roundabouts for timebeing.**

* * *

2.  **51684 Missing Lane Connectivity**
    

**Reason:** Unable to create / generate lane connectivity at 3 valent junctions. This will be due to either incorrect due to one of the following reasons

I. Wrong matching of Crosslink data II. HD data itself being incomplete. III. Derivation issue

**Txn:** 2ace5197-acb6-4032-81c0-0055aadeda5f

**Location:** 54.3737787, 9.3199749

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** Ignore connectivity proposed by HD especially in simple 'T' 3 valent junctions. By default populate all possible connections at such junctions.

* * *

3.  **51147 Missing Lane Connectivity**
    

**Reason:** Unable to create / generate lane connectivity at 3 valent junctions. This will be due to either incorrect due to one of the following reasons

I. Wrong matching of Crosslink data II. HD data itself being incomplete. III. Derivation issue

**Txn:** 5ce352da-eb60-482d-9a3e-3e570842f16e

**Location:** 54.7182322, 9.6674309

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

More scenario txns ( no lane populated on side roads)

abb810b3-3352-495b-9949-57fa8cb8377e

041ee72e-c650-4938-a662-5f2d4de866bf

**Proposed solution**: Ignore connectivity proposed by HD especially in simple 'T' 3 valent junctions. By default populate all possible connections at such junctions.

* * *

4.  **51059 DTFR for Lane and Road not in line**
    

Reason: 1) Road elements have traffic restriction captured on them for example they are closed for medium trucks. Lanes on such road elements should have the same restriction on them. However HD does not give such lane level restrictions and shows every lane as open for all vehicles.

2.  Sometimes there is only one lane on roads open in both directions. Populating only one lane in one direction causes violation to fire.
    

Txn: 36a315bc-5e73-4bea-b52c-f9c0511daafb

Location: 53.7017789, 9.6492245

**Transaction edits**

**Database**

**HD centerlines and trajectories**

Case 2:

5aa9db90-abf5-418c-8dba-89237b27b676

**Transaction edits**

**Database**

**HD centerlines and trajectories**

Proposed solution: 1) Modify DTFR of lane as per restriction of road. Along with closing lane for one direction , close the other direction of the lane for opposite direction.

2.  If only one lane is going to populated on side road, create it with no DTFR restriction
    

* * *

5.  **51068 Invalid Lane Connectivity**
    

**Reason:** There are certain restrictions on existing RE (BP, DTFR, Maneuvers, GR etc) which prevent lane connectivity , but we populate it.

**Txn**: bd3826da-9e8f-4cb7-8043-2c666cb0eaf0

**Location:** 54.5051924, 8.9377945

**Transaction edits**

**Database**

**HD centerlines and trajectories**

* * *

6.  **50311 Incorrect Direction of Traffic Flow for Lane for connected lanes (Error, Critical)**
    

**Reason:** Incorrect lane connectivity given by derivation process. ‘From’ lane should have traffic flow towards the junction , while ‘To’ lane

should have traffic flow away from the junction.

**Txn:** 4f94fc28-8f6f-40a3-9c36-fa79ba469be6

**Location:** 53.9280544, 10.3162323

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution**: Check whether lane connectivities are correctly populated correctly

* * *

7.  **50263 Traffic Flow Conflicting with Driving Side (Warning, Critical)**
    

**Reason**: Traffic flow on lane should follow Driving side of the particular country. For example if its a 2 way open road, there should be either 1 lane

in each direction OR one bidirectional lane. This violation can occur due to incorrect lane information from HD.

**Txn:** 457576b0-5969-45c9-bba2-3e68802f23cd

**Location:** 54.0414632, 9.3480155

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution**: This is generally accompanied by 51059. Giving bidirectional lanes where one lanes are present and correct lane connectivity will solve this rule.

* * *

8.  **53161 Invalid Lane Connection (Rare warning, Critical)**
    

**Reason**: Seen to be logging over junctions where there are lane connectivities instead of lane centerlines. Connected Lanes departing from the same Road Elements must not cross

**Txn**: 8f04b539-e635-483c-b142-d020918a8f7e

**Location:** 53.7750315, 9.6616162

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** Improve lane connectivity over junctions. Ensure that lane connectivity departing from same road element do not cross each other.

* * *

9.  **51085 Invalid Direction of Traffic Flow for Lane (Rare Warning , Critical)**
    

**Reason:** Somewhat similar to 51059 , DTFR on lane and road should be similar. Road is open in both directions with some restrictions for vehicles lanes should get similar restriction.

**Txn:** acd28c8a-2b57-4fe5-bbcd-ff9db90beb9f

**Location**: 53.6072871, 9.6370286

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution**: Improve transaction logic which copies traffic flow on road elements, mostly traffic restrictions

* * *

10.  **51830 Incorrect relationship to Lane Connectivity (Error , Critical)**
     

**Reason:** Logging due to incorrect lane connectivity – haphazard lane connectivity.

**Txn**: a9001aef-5dc3-4840-94f9-c701486a03e4

**Location**: 54.7064429, 9.5306095

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution**: Correctly identify the intermediate road element and improve lane connectivity. HD needs to improve such junctions as well.

* * *

11.  **52379 Incorrect Lane Connectivity Relationship (Error, Critical)**
     

Reason: Lane connectivities have been created where those number of lanes do not exist in database.

Txn: 70954547-3a89-4750-93a8-5d0c981eb803

Location: 54.4861910, 9.7097606

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution**: Refinement in lane connectivity logic. Connectivity from only existing lanes should be guaranteed.

* * *

12.  **51083 Incorrect Lane Divider Type or incorrect Lane Connectivity (Warning, Critical)**
     

**Reason**: Turn Lane dividers ideally should not be solid, but this could be the reality.

**Txn:** 751aeacf-a203-490d-99e2-f9057c86b8c1

**Location**: 53.8174655, 10.1738497

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** Ensure correctness of lane dividers being correctly populated as per HD. Occasionally can be false positive of everything is correct.

* * *

13.  **51149 Incorrect Lane Divider Type or incorrect Lane Connectivity**
     

**Reason:** Similar to 51083. Dividers should be populated as per reality.

**Txn:** ae08a947-8235-4a91-a6da-75b86116b70d

**Location:** 53.8126690, 10.3288546

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** Ensure correctness of lane dividers being correctly populated as per HD. Occasionally can be false positive of everything is correct.

* * *

14.  **52261 Carriageways too close based upon number of lanes ( Warning , Normal)**
     

**Reason:** Defined set of rule where carriageways should be widely spaced to accomodate higher number of lanes.

Not dependent on derivation or HD side.

**Txn:** e81b0467-4301-411d-a1cc-44aed72961d6

**Location:** 54.4732102, 9.0546438

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** No action required. Could be a candidate for skipping from our project

* * *

15.  **53887 Lane Connectivity conflicts with Lane Direction Category (Rare warning, Critical)**
     

**Reason:** Lane Direction Category indicates that turn should be taken only as indicated in the database. Example ‘Only Left’ should connect only Left lane,

not straight. Any other connectivity causes this violation to fire.

**Txn:** 751aeacf-a203-490d-99e2-f9057c86b8c1

**Location:** 53.8172101, 10.1735019

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

* * *

16.  **52497 Curvature at Junction starts and ends at same location of all Linear Assignment Maneuvers on that Junction (Error, Critical)**
     

Reason: Logs due to presence of Linear assignment maneuver

Txn: ebc265e4-3549-4d36-8d95-697db765f40f

Location: 54.2728757, 10.0173329

* * *

17.  **51062 Incorrect Lane Connection (Rare Warning Critical)**
     

Reason: Incorrect lane connectivity derivation

Txn: 22c8d4ba-122b-4d4a-a017-420ea2e1819e

Location: 54.3072634, 10.6521663

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

**Proposed solution:** Ensure correct lane connectivity at junctions

* * *

18.  **52124 Incorrect Z-Levels for Lane Connectivity (Error, Critical)**
     

**Reason:** Incorrect ‘sequence’ of composition of the particular lane connectivity. It should follow First RE-- Junction- Intermediate RE - Last RE.

Derivation of lane connectivity needs to be reviewed.

**Txn:** 09211602-5b09-4638-a370-bb91233fe900

**Location:** 54.3321177, 10.1197807

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

* * *

19.  **52721 Geometry of Composing Part does not match geometry of Composite Feature.**
     

Reason: Lane connectivity incorrectly created which led to cascade failure of composing the correct ‘Level 2’ feature lane connectivity.

HD data here is incorrect leading to errors in derivation.

Txn: 68baee5b-1830-4c6a-afb6-a2acedc8c795

Location: 53.7784910, 9.9784629

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

* * *

20.  **52026 Incorrect Lane Connection**
     

Reason: Wrong lane connection between junctions.

Txn: f0590ca1-422a-43aa-9779-24471f450f25

Location: 53.9409179, 10.2571595

**Transaction edits**

**HD areas**

**HD centerlines and trajectories**

* * *

# Summarised action points

**Rule ID**

**Proposed action**

**Feasibility**

**PM opinion required?**

**Trade offs**

**Solution**

50329

If by default roads inside junction get same lanes as main road OR

by default roads inside junction get 2 lanes

OR

Orbis improvement

Y – Proposal to default lanes and own connectivity on intermediate roads in junctions as per own logic overriding HD information

OR

\-Request Orbis to indicate lanes on such roads

1.Correctness of data on is not guaranteed since we are ‘filling’ the information using existing lane info.

2.  Genesis needs to build its own logic
    
3.  If its decided to improve HD then possibility of extension of model
    

51684

Ignore connectivity given by HD, connect every lane in every direction possible – 3 valent junctions with FOW 3 or DC Taper

Y- Whether we should populate default lane connectivity at small junctions

1.  Connectivity may not be always in 100% of cases although 90% we expect it to be good.
    

51147

Ignore connectivity given by HD, connect every lane in every direction possible – 3 valent junctions with FOW 3 or DC Taper

Y- Whether we should populate default lane connectivity at small junctions

1.  Connectivity may not be always in 100% of cases although 90% we expect it to be good.
    

51059

Take into consideration vehicle types on roads

OR create bidirectional lanes OR

Orbis improvement

Y- Whether we should create bidirectional lanes on road open in both directions

1.  Correctness of data whether we should create one bidirectional lane or two lanes --one in each direction
    

51068

Orbis improvement

Y-- Ask whether Orbis takes into consideration maneuvers, DTFR, GR while creating connectivties. If not whether we should ignore the connectivities in such cases.

1.  Need to fetch more attribute information which may slow down the process.
    

50311

Improve derivation

Yes - for the scenario given in the transaction above

4f94fc28-8f6f-40a3-9c36-fa79ba469be6

N

Tx - 4f94fc28-8f6f-40a3-9c36-fa79ba469be6

The roads connect to each other from both sides. From one side via junction and from another side via another road. This was the reason lane connectivity was created via junction iso via road.

50263

Orbis improvement /Improve derivation

53161

Improve lane connectivity logic

51085

Orbis improvement

51830

Improve lane connectivity logic

52379

Needs more investigation

51083

No action defined, as per reality.

51149

No action defined, as per reality.

52261

Proposed to be skipped

53887

Orbis improvement

52497

Needs more investigation

51062

Improve lane connectivity logic

52124

Improve lane connectivity logic

52721

Improve lane connectivity logic

52026

Orbis improvement / Improve lane connectivity logic.
