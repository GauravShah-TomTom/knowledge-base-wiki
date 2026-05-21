---
type: system
---

# UMM — Uber Map Model

*Source: raw/scans/MEDS Overview.pdf*

UMM is Uber's internal map data model — the canonical representation of road network data used by navigation, routing, and map quality systems such as [[MEDS]].

## Data Entities

| Entity | Description |
|---|---|
| Segments | Directed road links between junctions |
| Junctions | Intersection/connection points between segments |
| Maneuvers | Turn instructions at junctions (direction + connecting segments) |
| Road furniture — Barriers | Physical barriers blocking road access |
| Road furniture — Signs | Road signs |
| Road furniture — Traffic lights | Traffic signal furniture |

## Example Record (JSON)

```json
{
  "uuid": "199559f5-92d8-9c7a-5964-12336f511f1b",
  "geometry": {
    "point": { "latE7": -234799350, "lngE7": -466614120 }
  },
  "data": {
    "maneuver": {
      "type": 1,
      "segments": [
        { "direction": 1, "uuid": "65fd3976-0272-9389-14a9-6b477b93e89d" },
        { "direction": 2, "uuid": "85b20f8e-a03b-43b7-bb5a-94a2bf4d41fb" }
      ]
    }
  },
  "providersData": [
    {
      "provider": "TOMTOM",
      "version": "1106820223 - 1106820716",
      "tags": { "mnrFeatureType": "2103" },
      "providerId": "eabcda62-c757-4eef-818a-8f3b0280b662"
    }
  ],
  "countryCode": "BR"
}
```

Coordinates use E7 encoding (multiply by 1e-7 to get decimal degrees).

## Provider Data

UMM records include a `providersData` field linking to source map providers such as TomTom (mnrFeatureType codes reference TomTom's MNR feature taxonomy).

## Related

- [[MEDS]] — uses UMM as one of its input signals for map error detection
