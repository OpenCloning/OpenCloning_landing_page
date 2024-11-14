---
####################### Banner #########################
banner:
  title : "OpenCloneKit"
  content : "A suite of integrated Open Source tools to plan and document your next cloning project"

##################### Feature ##########################
feature:
  enable : true
  feature_item:
    # feature item loop
    - name : "pydna"
      icon : "fas fa-dna"
      content : "Python library to simulate cloning<br>(PCR, Gibson, Golden Gate...)"

    # feature item loop
    - name : "teemi"
      icon : "fas fa-bacterium"
      content : "Pydna extension for strain engineering<br>Jupyter Notebooks as experiment documentation"

    # feature item loop
    - name : "ShareYourCloning"
      icon : "fas fa-window-restore"
      content : "Web application to plan and visualize cloning strategies<br>No need to code!"

    # feature item loop
    - name : "Single data model"
      icon : "fas fa-database"
      content : "All tools produce and understand the same file format"



######################### Service #####################
service:
  enable : true
  service_item:
    # service item loop
    - title : "Pydna"
      panels:
      - path: "./pydna_script1.py"
        title: "Import sequences from multiple sources"
        type: "code"
      - path: "./pydna_script2.py"
        title: "Simulate restriction and ligation"
        type: "code"
      - path: "./pydna_script3.py"
        title: "Design PCR primers"
        type: "code"
      - path: "./pydna_script4.py"
        title: "Design Gibson primers and assemble"
        type: "code"
      - path: "images/documentation.png"
        title: "Excellent documentation with real-world examples"
        type: "image"
        button:
          content: "Visit the docs"
          link: "https://bjornfjohansson.github.io/pydna/getting_started.html"
      content : Built on top of 🐍 Biopython 🧬, pydna is a package providing modules to simulate cloning handle double-stranded DNA. From simulating DNA assemblies to automating complex cloning workflows, pydna empowers you to plan and document your cloning projects 🚀🔬✨
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/BjornFJohansson/pydna"
    # service item loop
    - title : "ShareYourCloning"
      panels:
      - path: "images/genome.gif"
        title: "Access gene sequences from NCBI"
        type: "image"
      - path: "images/repositories.gif"
        title: "Get plasmid sequences from AddGene or SnapGene"
        type: "image"
      - path: "images/supported_cloning.png"
        title: "Support for many cloning methods"
        type: "image"
      - path: "images/templates.gif"
        title: "Use cloning kit templates (MoClo, Gibson...)"
        type: "image"
      - path: "images/primer_design.gif"
        title: "Design primers for Homologous Recombination, Gibson, etc."
        type: "image"
      content : "An Open Source web application to plan and visualize cloning strategies. 🎉No coding required!🎉 It provides an intuitive interface to plan your cloning strategy, export it to an open file format and generate publication-ready figures 📊🔬🎨"
      button:
        enable : true
        label : "Check it out"
        link : "https://shareyourcloning.org"

# service item loop
    - title : "Teemi"
      panels:
      - path: "./teemi_example1.py"
        title: "Example 1"
        type: "code"
      - path: "./teemi_example1.py"
        title: "Example 2"
        type: "code"
      - path: "./teemi_example1.py"
        title: "Example 3"
        type: "code"
      content : "A pydna extension for ⚖️ FAIR ⚖️ microbial strain construction. It covers the entire DBTL (Design-Build-Test-Learn) cycle, allowing users to design genetic libraries, simulate workflows, and track samples efficiently. Boost your metabolic engineering projects with streamlined automation and flexible workflows! 🚀🧬"
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/hiyama341/teemi"

    # service item loop
    - title : "Single data model"
      panels:
      - path: "./syc_model1.json"
        title: "External sequence: AddGene plasmid"
        type: "code"
      - path: "./syc_model2.json"
        title: "External sequence: NCBI genome region with gene of interest"
        type: "code"
      - path: "./syc_model3.json"
        title: "Experiment: Gibson assembly of a plasmid"
        type: "code"
      - path: "./syc_model4.json"
        title: "Experiment: PCR"
        type: "code"
      content : "A simple interoperable data model developed with [LinkML](https://linkml.io/) to represent the provenance of engineered DNA sequences. Currently used in [ShareYourCloning](#shareyourcloning) but to be supported by all other tools soon."
      button:
        enable : true
        label : "Check it out"
        link : "/team/"

#################### Logo section #####################
logo:
  enable : true
  logo_items:
    - image: "https://www.pombase.org/assets/pombase-logo.png"
      link: "https://www.pombase.org"
    - image: "https://www.shareyourgreendesign.com/wp-content/uploads/2023/12/opp_3210.png"
      link: "https://www.dtu.dk/english/"
    - image: "https://www.elabftw.net/img/elabftw-logo.png"
      link: "https://www.elabftw.net/"
    - image: "https://www.embl.org/guidelines/design/wp-content/uploads/2022/02/EMBL_logo_colour_DIGITAL.png"
      link: "https://labid-demo.embl.de/"


##################### Call to action #####################
call_to_action:
  enable : true
  title : "Join our community"
  image : "images/cta.svg"
  content : "Partner with like-minded scientists to improve documentation and reproducibility in cloning"
  button:
    enable : true
    label : "Contact Us"
    link : "contact/"
---
