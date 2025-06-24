---
####################### Banner #########################
banner:
  button:
    enable: false

##################### Feature ##########################
feature:
  enable : true
  feature_item:
    # feature item loop
    - name : "Import from anywhere"
      icon : "fas fa-file-import"
      content : "Your files, NCBI, AddGene, SnapGene, iGEM..."

    # feature item loop
    - name : "Engineer anything"
      icon : "fas fa-dna"
      content : "Gibson, Golden Gate, Gateway, In vivo assembly..."

    # feature item loop
    - name : "Automate everything"
      icon : "fas fa-robot"
      content : "Create scripts, notebooks, templates and forms"

    # feature item loop
    - name : "Share with anyone"
      icon : "fas fa-users"
      content : "Export cloning workflows in FAIR Open File Format."

#################### Button link #####################

button_link:
  enable : true
  title: "Ready to Get Started?"
  label : "▶ Try it here"
  link : "https://app.opencloning.org"


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
        title: "Primer design for Homologous Recombination, Gibson..."
        type: "image"
      content : "Supports most cloning methods and has powerful primer design capabilities."
      # button:
      #   enable : true
      #   label : "Check it out"
      #   link : "https://github.com/hiyama341/teemi"

    - title : "Automate everything"
      panels:
      - path: "images/templates.gif"
        title: "Use cloning kit templates"
        type: "image"
      - path: "./opencloning_script1.py"
        title: "Programmaticly load sequences"
        type: "code"
      - path: "./opencloning_script2.py"
        title: "Programmaticly design cloning strategies"
        type: "code"
      content : "Use scripts, notebook, forms and templates to speed up design"
      button:
        enable : true
        label : "Get started with scripting"
        link : "https://github.com/manulera/OpenCloning_backend/tree/master/examples/scripting"

    # service item loop
    - title : "Share with anyone"
      panels:
      - path: "images/cloning_strategy.png"
        title: "Capture the entire cloning workflow"
        type: "image"
        large_image: true
      - path: "./syc_model1.json"
        title: "Data model for AddGene plasmid"
        type: "code"
      - path: "./syc_model4.json"
        title: "Data model for PCR"
        type: "code"
      - path: "https://linkml.io/uploads/linkml-logo_color.png"
        title: "Powered by LinkML"
        type: "image"
        content: "LinkML allows you to work with this data model in your stack of choice: Python, SQL, RDF, JSON Schema, TypeScript, etc."
      content : "Export full DNA engineering workflows to JSON. OpenCloning uses a simple interoperable data model developed with [LinkML](https://linkml.io/)."
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/OpenCloning/OpenCloning_LinkML"


##################### Call to action #####################
call_to_action:
  enable : true
  title : "Start using OpenCloning"
  image : "images/cta.svg"
  content : "
  Whether you work as a researcher, platform scientist, or in industry, OpenCloning can help you with DNA engineering.
  "
  buttons:
    - enable : true
      label : "Newsletter"
      link : "https://eepurl.com/h9-n71"
    - enable : true
      label : "▶ Try it"
      link : "https://app.opencloning.org"


#################### Logo section #####################
logo:
  enable : true
  title : "Success stories"
  logo_items:
    - image: "https://www.elabftw.net/img/elabftw-logo.png"
      link: "/success-stories/elabftw"




---

