# Test upload fixtures

These files are for local testing of the `/upload` UI. They're gitignored.

| File | Will land at | Notes |
| --- | --- | --- |
| `hello-note.md` | `raw/notes/hello-note.md` | Plain note |
| `sprint-retro.vtt` | `raw/transcripts/<YYYY-MM-DD> sprint-retro.vtt` | Date prefix auto-applied |
| `tech-design-review-IDIndex-improvement.md` | `raw/notes/tech-design-review-IDIndex-improvement.md` | Summary note |
| `tech-design-review-IDIndex-improvement.vtt` | `raw/transcripts/<YYYY-MM-DD> tech-design-review-IDIndex-improvement.vtt` | Real transcript |

Drag any of these onto http://localhost:3000/upload to verify the flow.
