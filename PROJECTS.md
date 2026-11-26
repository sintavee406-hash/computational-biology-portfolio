# Research and Software Index

All descriptions below distinguish computational analysis from experimental validation. Except for the featured thesis, other projects are intentionally described at the workflow level without unpublished results.

## Featured thesis: cyclic hexapeptides and JAK kinases

**Computational Prioritization of Cyclic Hexapeptides for JAK1, JAK2, and JAK3 Using Molecular Docking, Machine Learning, and Molecular Dynamics**

- **Question:** How can cyclic-peptide candidates be prioritized across three related kinase domains using complementary computational evidence?
- **Workflow:** CX4C library generation → receptor/ligand preparation → GPU docking and quality control → cross-target profile analysis → sequence-based ML validation → structural inspection → selected MD follow-up.
- **Skills shown:** high-throughput virtual screening, peptide modeling, Python/R analysis, ML evaluation, visualization, Linux/WSL and GPU workflows, research communication.
- **Public examples:** selected docking-score distributions, ML validation plot, JAK1–CPYWWC binding-site views, and peptide RMSD from the earlier completed three-peptide panel.
- **Status:** Graduate thesis in progress. The earlier three-peptide MD panel is complete; the expanded five-peptide panel is separate and ongoing.

[Detailed research note](jak_project_summary.md) · [Portfolio page](docs/index.html#thesis)

## Topaz formulation and network pharmacology

- **Question:** Explore potential molecular and network-level associations relevant to benign prostatic hyperplasia (BPH) and erectile dysfunction (ED).
- **Workflow:** curate annotated compounds, retrieve and prepare structures, dock against SRD5A2 (PDB 7BW1) and PDE5 (PDB 1UDU) with GOLD/ChemPLP, map compound–target and disease associations, construct Cytoscape/STRING networks, and assess GO/KEGG enrichment.
- **Analysis design:** keep compound identity, structure source, docking target, and network annotation traceable so molecular poses and pathway-level hypotheses can be interpreted separately. Docking scores are not experimental target inhibition.
- **Natural-compound work:** includes preparation or screening of examples such as chrysin, daidzein, brucine, and 18β-glycyrrhetinic acid.
- **Skills shown:** cheminformatics, molecular docking, source tracing, network pharmacology, functional enrichment, data integration.
- **Disclosure:** workflow only; unpublished findings and rankings are not shown.

## Tyrosinase cyclic-peptide screening

- **Question:** Analyze a large cyclic-peptide sequence and docking dataset for tyrosinase-focused prioritization.
- **Workflow:** sequence-library quality control, docking-output organization, SQL/data integration, feature analysis, and ML evaluation with attention to label provenance and dataset coverage.
- **Analysis design:** connect peptide sequences to their docking records, inspect missing or duplicate entries, and keep model evaluation tied to the origin of its labels rather than treating predicted scores as measured activity.
- **Skills shown:** large-scale scientific data processing, Python, SQL, ML, reproducibility checks.
- **Disclosure:** no unpublished rankings or results.

## Acetylcholinesterase (AChE)

- **Question:** Examine pyridoquinoxaline compounds as potential AChE binders.
- **Workflow:** structure-based preparation and docking with PDB 7E3H; use donepezil as a reference; inspect pose and binding-site interactions.
- **Interpretation:** use the reference compound to contextualize pose placement and contacts, without equating similar docking patterns with comparable biological potency.
- **Skills shown:** receptor/ligand preparation, reference-based docking, structural interpretation.

## Pancreatic lipase

- **Question:** Screen potential pancreatic-lipase inhibitors in the catalytic site.
- **Workflow:** prepare the enzyme and candidate ligands, dock with orlistat as a reference, inspect the catalytic triad and surrounding contacts.
- **Interpretation:** assess predicted placement against the catalytic-site geometry and the reference pose; a docking pose alone does not demonstrate enzyme inhibition.
- **Skills shown:** enzyme active-site analysis, docking, reference-compound comparison.

## Alpha-amylase

- **Question:** Explore candidate binding near the alpha-amylase catalytic site.
- **Workflow:** structure-based docking with PDB 1B2Y and catalytic-residue interpretation.
- **Interpretation:** relate predicted ligand contacts to the catalytic region while keeping structural plausibility separate from measured activity.
- **Skills shown:** protein structure handling, docking, interaction analysis.

## Alpha-glucosidase (MGAM)

- **Question:** Explore candidate inhibitors of maltase-glucoamylase.
- **Workflow:** prepare MGAM structure (PDB 2QMJ), dock candidates, and inspect active-site geometry.
- **Interpretation:** compare candidate placement within the same target-defined pocket; avoid cross-target score comparisons without context.
- **Skills shown:** target preparation, molecular docking, binding-site assessment.

## Leishmania CYP51

- **Question:** Assess a parasite sterol-biosynthesis target for inhibitor discovery.
- **Workflow:** inspect CYP51 structure, binding-site and heme environment, and evaluate candidate poses.
- **Interpretation:** account for the cofactor-containing pocket when reading poses; structural proximity to heme is a hypothesis, not evidence of mechanism.
- **Skills shown:** structural bioinformatics, heme-protein interpretation, docking analysis.

## Ligand Fetcher

- **Purpose:** support retrieval and preparation of chemical structures for molecular modeling.
- **Workflow:** resolve compound identifiers, fetch 3D structures where available, apply fallback conformer generation and basic structure/format checks.
- **Skills shown:** Python software development, chemical-data APIs, RDKit-based preparation, validation, fault handling.
- **Disclosure:** project description only; no private collections or licensed assets.

## Cyclic-Peptide Library Generator

- **Purpose:** generate cyclic-hexapeptide structures at screening scale.
- **Workflow:** enumerate sequence space, construct peptide structures, perform cyclization and output checks, organize parallel generation for downstream docking.
- **Skills shown:** Python, peptide modeling, Biopython/PeptideBuilder, parallel processing, workflow design.
- **Disclosure:** project description only; full unpublished screening library is not bundled.
