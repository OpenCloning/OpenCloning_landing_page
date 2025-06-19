---
####################### Banner #########################
banner:
  title : "OpenCloning"
  content : "An Open-Source web application for DNA engineering"

##################### Feature ##########################
feature:
  enable : true
  feature_item:
    # feature item loop
    - name : "Import from anywhere"
      icon : "fas fa-file-import"
      content : "Your files, NCBI, AddGene, SnapGene, iGEM, etc."

    # feature item loop
    - name : "Engineer anything"
      icon : "fas fa-dna"
      content : "PCR, Gibson, Golden Gate, Gateway, In vivo assembly, CRISPR, homologous recombination, etc."

    # feature item loop
    - name : "Automate everything"
      icon : "fas fa-robot"
      content : "Use scripts, notebook, forms and templates to automate repetitive design and engineering tasks"

    # feature item loop
    - name : "Share with anyone"
      icon : "fas fa-users"
      content : "Export your cloning workflow in a well-documented and FAIR Open File Format."



######################### Service #####################
service:
  enable : true
  service_item:
    # service item loop
    - title : "Import from anywhere"
      panels:
      - path: "images/genome.gif"
        title: "Access gene sequences from NCBI"
        type: "image"
      - path: "images/repositories.gif"
        title: "Get plasmid sequences from AddGene or SnapGene"
        type: "image"
      - path: "images/all_repositories.png"
        title: "Many other repositories supported!"
        type: "image"
      content : "From many online repositories and local files."
      # button:
      #   enable : true
      #   label : "Check it out"
      #   link : "https://opencloning.org"

# service item loop
    - title : "Engineer anything"
      panels:
      - path: "images/supported_cloning.png"
        title: "Support for most cloning methods"
        type: "image"

      - path: "images/primer_design.gif"
        title: "Design primers for Homologous Recombination, Gibson, etc."
        type: "image"
      content : "Supports most cloning methods and has powerful primer design capabilities."
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/hiyama341/teemi"

    - title : "Automate everything"
      panels:
      - path: "images/templates.gif"
        title: "Use templates when using cloning kits"
        type: "image"
      content : "Use scripts, notebook, forms and templates to speed up design"
      button:
        enable : true
        label : "Get started"
        link : "https://github.com/hiyama341/teemi"

    # service item loop
    - title : "Share with anyone"
      panels:
      - path: "images/cloning_strategy.png"
        title: "Capture the entire cloning workflow"
        type: "image"
      - path: "./syc_model1.json"
        title: "External sequence: AddGene plasmid"
        type: "code"
      # - path: "./syc_model2.json"
      #   title: "External sequence: NCBI genome region with gene of interest"
      #   type: "code"
      # - path: "./syc_model3.json"
      #   title: "Experiment: Gibson assembly of a plasmid"
      #   type: "code"
      - path: "./syc_model4.json"
        title: "Experiment: PCR"
        type: "code"
      - path: "https://linkml.io/uploads/linkml-logo_color.png"
        title: "Powered by LinkML"
        type: "image"
        content: "LinkML allows you to work with this data model in your stack of choice: Python, SQL, RDF, JSON Schema, TypeScript, etc."
        button:
          content: "Learn more"
          link: "https://linkml.io/"
      content : "You can export full DNA engineering workflows. OpenCloning uses a simple interoperable data model developed with [LinkML](https://linkml.io/) to represent the provenance of engineered DNA sequences."
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/genestorian/ShareYourCloning_LinkML?tab=readme-ov-file"

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
  content : "
  Our goal is to help **adapt** and **implement** these tools in diverse settings: BioFoundries, Electronic Lab Notebooks, Data repositories, research groups, etc.


  Join like-minded scientists in improving documentation and reproducibility in cloning
  "
  button:
    enable : true
    label : "Contact Us"
    link : "contact/"
---
