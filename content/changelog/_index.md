# Changelog

Main user-facing changes are listed here. For a full list of changes, see the GitHub release notes of the [frontend](https://github.com/manulera/OpenCloning_frontend/blob/master/apps/opencloning/CHANGELOG.md) and [backend](https://github.com/manulera/OpenCloning_backend/releases) repositories.

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