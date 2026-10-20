# HypergraphViewer

[HypergraphViewer](https://github.com/yuxizhe/HypergraphViewer) is a web app for exploring HIF files visually. It runs entirely in the browser, so there is nothing to install: open the [live app](https://yuxizhe.github.io/HypergraphViewer/), point it at a HIF file, and browse the hypergraph.

**Try it:** [open `lesmis.hif.json` in HypergraphViewer](https://yuxizhe.github.io/HypergraphViewer/?url=https%3A%2F%2Fraw.githubusercontent.com%2FHIF-org%2FHIF-standard%2Fmain%2Ftutorials%2Fdata%2Flesmis.hif.json).

![HypergraphViewer: database panel, hypergraph canvas and subgraph inspector](https://raw.githubusercontent.com/yuxizhe/HypergraphViewer/main/docs/images/screenshot.png)

*The Neurology sample dataset: the left panel holds the data source, dataset statistics and the vertex list; the canvas shows the neighborhood of the selected vertex; the right panel lists the vertices and hyperedges in view. Vertices are colored by `entity_type`.*

## Loading a HIF file

Open <https://yuxizhe.github.io/HypergraphViewer/>. The **Data Source** card on the left offers three options:

- **Remote HIF URL**: paste the URL of a HIF file and click **Load**. The file is fetched by the browser, so the server must allow cross-origin requests; raw GitHub URLs work. For example, the Les Misérables file from this repository:

  ```
  https://raw.githubusercontent.com/HIF-org/HIF-standard/main/tutorials/data/lesmis.hif.json
  ```

  The address bar then holds the file as a `?url=` parameter, so the page can be bookmarked or shared. A link of the form `https://yuxizhe.github.io/HypergraphViewer/?url=<URL-encoded HIF file URL>` opens the file directly.

- **Upload HIF File**: pick a local `.json` file. It is read in the browser and is not uploaded to any server.
- **Sample Datasets**: built-in examples (Game of Thrones, a medical knowledge graph, and others), all stored as HIF.

The other HIF files in [`data/`](data) load the same way, for example [`e-coli.json`](https://yuxizhe.github.io/HypergraphViewer/?url=https%3A%2F%2Fraw.githubusercontent.com%2FHIF-org%2FHIF-standard%2Fmain%2Ftutorials%2Fdata%2Fe-coli.json), [`diseasome.json`](https://yuxizhe.github.io/HypergraphViewer/?url=https%3A%2F%2Fraw.githubusercontent.com%2FHIF-org%2FHIF-standard%2Fmain%2Ftutorials%2Fdata%2Fdiseasome.json) and [`contacts_high_school.hif.json`](https://yuxizhe.github.io/HypergraphViewer/?url=https%3A%2F%2Fraw.githubusercontent.com%2FHIF-org%2FHIF-standard%2Fmain%2Ftutorials%2Fdata%2Fcontacts_high_school.hif.json) (33 MB, 172,035 hyperedges).

## How HIF is displayed

| HIF | In the viewer |
| --- | --- |
| `incidences` | Grouped by `edge` into hyperedges. Hyperedges with 3+ members are drawn as contours around their nodes, 2-member hyperedges as lines. |
| `nodes` | Vertices. Their `attrs` appear when hovering a vertex and in the details panel. A `attrs.entity_type` value colors the vertex and can be used as a filter. Nodes that only appear in `incidences` are added automatically, and isolated nodes are listed too. |
| `edges` | `attrs` of each edge (such as `description`, `keywords` or `type`) are shown for its hyperedge. Edges without incidences are counted but not drawn. |
| `metadata`, `network-type` | `metadata.name` and `network-type` are read; directed hyperedges are drawn without direction. |

Node and edge IDs can be strings or numbers.

## Exploring a hypergraph

Large hypergraphs are explored one neighborhood at a time:

1. Pick a vertex in the **Vertices** list on the left (search by ID, type or description). The canvas shows that vertex together with every hyperedge it belongs to.
2. Hover vertices, lines and contours for their attributes; click a hyperedge to highlight its members.
3. Switch between **Hypergraph** mode (contours) and **Graph** mode (pairwise lines with a force layout) at the top.
4. Use the **Subgraph** panel on the right to hide, show or recolor individual vertices and hyperedges. Hub vertices that belong to at least half of the hyperedges in view are hidden by default to keep the layout readable; click **Show all** to bring them back.

## Tips

- `NaN` and `Infinity`, which Python's `json` module writes by default but which are not valid JSON, are read as `null`.
- To validate a file against the HIF schema before loading it, see [Validate files against HIF standard](../README.md#validate-files-against-hif-standard).
- The rendering is also available as the [`hypergraph-viz`](https://github.com/yuxizhe/HypergraphViewer/tree/main/packages/hypergraph-viz) package for embedding hypergraph views in other web pages.
