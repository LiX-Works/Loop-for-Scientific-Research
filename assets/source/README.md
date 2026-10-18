# Figure and logo sources

These editable sources back up the repository's SVG artwork. Each builder uses only the Python standard library and writes a complete SVG; no graphics application or network access is required. The three workflow illustrations and the logo can be rebuilt independently.

| SVG asset | Editable source |
| --- | --- |
| [overview.svg](../overview.svg) | [build_overview.py](build_overview.py) |
| [research-cycle.svg](../research-cycle.svg) | [build_research_cycle.py](build_research_cycle.py) |
| [modules.svg](../modules.svg) | [build_modules.py](build_modules.py) |
| [brand/logo.svg](../brand/logo.svg) | [logo/build_logo.py](logo/build_logo.py) and [logo/geometry.json](logo/geometry.json) |

From the repository root, run:

```bash
python assets/source/build_overview.py
python assets/source/build_research_cycle.py
python assets/source/build_modules.py
python assets/source/logo/build_logo.py
```

Every builder also accepts `--output PATH` to write a separate copy while retaining the checked-in asset. Default destinations are resolved relative to each source file.

The provisional logo is **G3 + B3**, with an ink-green frame and initials, a bronze return arrow, and strengthened Monotype Corsiva **SR**. Its letter outlines are stored as vector geometry, rather than embedded font files. The JSON backup preserves the shapes and style settings, so regeneration needs neither the original installed typeface nor any private candidate folder or machine-specific path. Keep the geometry and generator together when copying this source backup.
