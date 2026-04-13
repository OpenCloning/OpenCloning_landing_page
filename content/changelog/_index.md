# Changelog

Main user-facing changes are listed here. For a full list of changes, see the GitHub release notes of the [frontend](https://github.com/manulera/OpenCloning_frontend/blob/master/apps/opencloning/CHANGELOG.md) and [backend](https://github.com/manulera/OpenCloning_backend/releases) repositories.

## Snapgene history parsing

OpenCloning now parses the history of SnapGene files! You can just drag-and-drop a single .dna file into OpenCloning, and it will parse its history. You can see it in action in [this LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7449368101571366912/). If you want to use this in scripts, check out [this function](https://pydna.readthedocs.io/latest/reference/pydna.html#pydna.snapgene_history_parser.parse_snapgene_history).

## Phage recombinases

OpenCloning now supports custom phage recombinases. You can simulate site-specific recombination defining your own recognition sites (e.g. custom attB/attP/attL/attR sequences). Check out the [documentation](https://docs.opencloning.org/methods/phage_recombinases/).

## Assembler

The OpenCloning Assembler is a tool that allows you to clone with MoClo and Golden Gate kits. Designed to demistify Golden Gate assembly for newbies and to save time for experts, it makes combinatorial assembly using MoClo kits blazing fast. The best way to get a feeling of what it can do is to try it with one of the Syntaxes that are already available. Check out this [demo video](https://www.youtube.com/watch?v=ecd9WUIz6O8) or the [documentation](https://docs.opencloning.org/assembler/).

<img src="/images/changelog/changelog_assembler.png" style="width: 100%; height: auto;" caption="OpenCloning Assembler" alt="OpenCloning Assembler" title="OpenCloning Assembler" />

## Manual annotation

👉 Check out the [documentation](https://docs.opencloning.org/annotating_sequences/#manual-annotation).

You can now manually annotate sequences (create features) and create primers directly in the editor. You can also delete and modify existing annotation.

<img src="/images/changelog/manual_annotation.png" style="width: 100%; height: auto;" caption="Manual annotation" alt="Manual annotation" title="Manual annotation" />

## Simplified python scripting for easier automation

You can now write python scripts to automate cloning directly using the python library [pydna](https://github.com/pydna-group/pydna), which is integrated with the OpenCloning data model.

👉 Check out the [documentation](https://github.com/pydna-group/pydna/blob/master/docs/notebooks/history.ipynb) for how to get started with automating your cloning design!

## Import sequences from Open DNA Collections

[Open DNA Collections](https://github.com/Reclone-org/Open-DNA-Collections) are distributed by the [Reclone](https://reclone.org/) project. You can now import sequences from these collections directly into your design.

<div class="row justify-content-center">
    <img src="/images/changelog/open_dna_collections.png" style="width: 30%; height: auto;" caption="Open DNA Collections" alt="Open DNA Collections" title="Open DNA Collections" />
</div>