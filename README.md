# cfl-py

An incomplete python implementation of the [CFL's public API](https://api.cfl.ca/docs).

## Current state of implementation

CFL API Version: 1.38

Endpoints:

- ✅ Games
- ✅ Players
- ⬜ Leaders
- ⬜ Team Leaders (v1.1)
- ⬜ Standings
- ⬜ Teams
- ⬜ Play-By-Play
- ⬜ Season
- ⬜ Transactions

## Versioning

This project uses a semantic versioning which includes the version of the CFL's API which it is attempting to implement.

For example:

```
1.0.1+cfl1.38
```

This is version 1.0.1 of this library (first major release, no minor releases yet, 1 patch), and it is implementing version 1.38 of the CFL API.

A future version of this library might be something like:

```
2.3.0+cfl.138
```

This would represent the second major version of this library (a major update including changes incompatible with v1), the 3rd backward compatible release within that version, with no patches to that minor version, and still implementing 1.38. This would represent something like a re-write of the library.

Currently this library is in beta and is at version 0. Attempts will be made to avoid breaking changes between version 0 and version 1, but no guarantees.
